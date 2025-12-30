-- Select Glam rock bands and calculate their lifespan using 2024 as the current year
SELECT 
    band_name,
    IFNULL(split, 2024) - formed AS lifespan
FROM 
    metal_bands
WHERE 
    FIND_IN_SET('Glam rock', style) > 0
ORDER BY 
    lifespan DESC;
