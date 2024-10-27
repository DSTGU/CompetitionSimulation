import os
import random
def weighted_random_choice(arr):
    # Create weights for each item in the array
    weights = [i*i + 1 for i in range(len(arr))]

    # Randomly choose an item with the adjusted weights
    chosen_item = random.choices(arr, weights=weights, k=1)[0]
    return chosen_item

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

x = open("outfile.txt", "r").readlines()

maxiters = 10000
results = {}
events = []
for line in x:
    linedata = line.strip().split("\t")

    if linedata[1] not in results.keys():
        results[linedata[1]] = {}
        if linedata[1] not in ["333bf", "333mbf", "444bf", "555bf", "333mbo", "magic", "mmagic", "333ft"]:
            events.append(linedata[1])

    if int(linedata[3]) > 0:
        if linedata[0] not in results[linedata[1]].keys():
            results[linedata[1]][linedata[0]] = []
        if linedata[1] not in ["333bf", "333mbf", "444bf", "555bf"]:

            results[linedata[1]][linedata[0]].append(int(linedata[3]))
        #else:
        #    results[linedata[0]].append(int(linedata[2]))

def parsePrc(i):
    return str(i)[:4] + "%"

def runResults(iter, event, winners, podiumers, showAll=False):
    if(iter == 0): return
    print("event: ", event)
    print("iterations: ", iter, "/", maxiters)

    winnerprob = [(x, winners.count(x)) for x in set(winners)]
    sortedwinners = sorted(winnerprob, key=(lambda a: a[1]), reverse=True)
    print( "\nWinners:\n" )

    if showAll:
        outfile = open('results/' + event +"_win.txt", "w")
        for i in range(0, len(sortedwinners)):
            print(sortedwinners[i][0], parsePrc(sortedwinners[i][1] / iter * 100))
            outfile.write(sortedwinners[i][0] + "\t" + parsePrc(sortedwinners[i][1]/iter*100) +"\n")
        outfile.close()

    else:
        for i in range(0,min(len(sortedwinners), 5)):
            print(sortedwinners[i][0], parsePrc(sortedwinners[i][1]/iter*100))

    podiumProb = [(x, podiumers.count(x)) for x in set(podiumers)]
    sortedPodiumers = sorted(podiumProb, key=(lambda a: a[1]), reverse=True)
    print( "\nPodiumers:\n" )

    if showAll:
        outfile = open('results/' + event + "_podium.txt", "w")
        for i in range(0, len(sortedPodiumers)):
            print(sortedPodiumers[i][0], parsePrc(sortedPodiumers[i][1] / iter * 100))
            outfile.write(sortedPodiumers[i][0] + "\t" + parsePrc(sortedPodiumers[i][1] / iter * 100) + "\n")
        outfile.close()
    else:
        for i in range(0,min(len(sortedPodiumers), 5)):
            print(sortedPodiumers[i][0], parsePrc(sortedPodiumers[i][1]/iter*100))




winners = []
podiumers = []

for event in events:
    print(event)
    for i in range(0,maxiters):
        res = []
        for key in results[event].keys():
            a = weighted_random_choice(results[event][key])
            res.append((a, key))
        res.sort(key=lambda tup: tup[0])
        winners.append(res[0][1])
        podiumers.append(res[0][1])
        podiumers.append(res[1][1])
        podiumers.append(res[2][1])
        if i % 1000 == 0:
            runResults(i, event, winners, podiumers)

    runResults(maxiters, event, winners, podiumers, True)

    winners = []
    podiumers = []