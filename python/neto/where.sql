SELECT Name, Platform, Year, Genre, Publisher
FROM `minha-squad-minha-vida.data.video_game__sales`
WHERE CAST(IF(Year='N/A', '0', Year) AS INTEGER) BETWEEN 2000 AND 2010;