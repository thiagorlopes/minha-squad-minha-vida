SELECT  Rank, Name, Platform, Year, Genre, Publisher, NA_Sales, EU_Sales, JP_Sales, Other_Sales, Global_Sales

FROM `minha-squad-minha-vida.data.video_game__sales`

ORDER BY Name ASC,Year ASC,Global_Sales DESC