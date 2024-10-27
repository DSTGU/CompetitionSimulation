Symulator składa się z dwóch segmentów:

- generatora danych działającego na postawionej bazie WCA (plik sql) 
- skryptu symulującego w pythonie.

Aby umożliwić pominięcie generowania danych dostarczone zostały pliki tekstowe z danymi. Należy wybrać jeden z nich i zmienić nazwę na outfile.txt

Aby skrypt działał musi istnieć folder Results, ponieważ nie chciało mi się go tworzyć w pythonie.

Wystarczy uruchomić skrypt, a on sam wygeneruje i zapisze wyniki wszystkich symulacji
