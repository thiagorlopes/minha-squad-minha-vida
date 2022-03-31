SELECT* FROM `minha-squad-minha-vida.data.covid__country_regions` a 
INNER JOIN `minha-squad-minha-vida.data.covid__global_reports` b 
ON a.country_region_id=b.country_region_id;