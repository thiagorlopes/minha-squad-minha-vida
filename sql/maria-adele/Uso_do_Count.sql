SELECT COUNT(1) AS Brazil FROM `minha-squad-minha-vida.data.covid__country_regions` a

INNER JOIN `minha-squad-minha-vida.data.covid__global_reports` b 

on a.country_region_id = b.country_region_id

WHERE a.country_region='Brazil'