Select personId, eventId, best, average 
from Results r
JOIN competitions c on c.id = r.competitionId
WHERE personID in (SELECT wca_id from users u
JOIN Registrations r on r.user_id = u.id
where r.competition_id = 'PolishChampionship2024' and r.deleted_at is null)
ORDER BY c.end_date
INTO outfile "C:/Resources/outfile.txt"