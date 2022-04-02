SELECT gr.country_region_id,count(*) AS quantidade
    FROM `minha-squad-minha-vida.data.covid__global_reports` AS gr
    WHERE country_region_id= '000124'
    GROUP BY country_region_id