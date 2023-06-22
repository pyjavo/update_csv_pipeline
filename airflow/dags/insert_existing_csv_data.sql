LOAD DATA 
INFILE '/var/lib/mysql-files/archivo.csv' 
INTO TABLE raw_data 
FIELDS TERMINATED BY ',' 
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(@preferred_delivery_date)
SET preferred_delivery_date = NULLIF(@preferred_delivery_date,'');