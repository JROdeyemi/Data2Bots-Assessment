-- Create table
CREATE TABLE joshodey2178_analytics.agg_public_holiday (
	ingestion_date DATE PRIMARY KEY NOT NULL,
	tt_order_hol_jan INT NOT NULL,
	tt_order_hol_feb INT NOT NULL,
	tt_order_hol_mar INT NOT NULL,
	tt_order_hol_apr INT NOT NULL,
	tt_order_hol_may INT NOT NULL, 
	tt_order_hol_jun INT NOT NULL, 
	tt_order_hol_jul INT NOT NULL,
	tt_order_hol_aug INT NOT NULL,
	tt_order_hol_sep INT NOT NULL,
	tt_order_hol_oct INT NOT NULL,
	tt_order_hol_nov INT NOT NULL,
	tt_order_hol_dec INT NOT NULL)

-- Insert records into table
INSERT INTO joshodey2178_analytics.agg_public_holiday
SELECT
	CAST(CURRENT_DATE AS DATE) AS ingestion_date,
    COUNT(1) FILTER (WHERE EXTRACT(MONTH FROM fo.order_date) = 1) AS january,
    COUNT(1) FILTER (WHERE EXTRACT(MONTH FROM fo.order_date) = 2) AS february,
    COUNT(1) FILTER (WHERE EXTRACT(MONTH FROM fo.order_date) = 3) AS march,
    COUNT(1) FILTER (WHERE EXTRACT(MONTH FROM fo.order_date) = 4) AS april,
    COUNT(1) FILTER (WHERE EXTRACT(MONTH FROM fo.order_date) = 5) AS may,
    COUNT(1) FILTER (WHERE EXTRACT(MONTH FROM fo.order_date) = 6) AS june,
    COUNT(1) FILTER (WHERE EXTRACT(MONTH FROM fo.order_date) = 7) AS july,
	COUNT(1) FILTER (WHERE EXTRACT(MONTH FROM fo.order_date) = 8) AS August,
	COUNT(1) FILTER (WHERE EXTRACT(MONTH FROM fo.order_date) = 9) AS September,
	COUNT(1) FILTER (WHERE EXTRACT(MONTH FROM fo.order_date) = 10) AS October,
	COUNT(1) FILTER (WHERE EXTRACT(MONTH FROM fo.order_date) = 11) AS November,
	COUNT(1) FILTER (WHERE EXTRACT(MONTH FROM fo.order_date) = 12) AS December
	
FROM
    joshodey2178_staging.fact_orders AS fo
WHERE
    fo.order_date IN (
        SELECT calendar_dt
        FROM joshodey2178_staging.dim_dates
        WHERE
            day_of_the_week_num BETWEEN 1 AND 5
            AND working_day = 'false'
            AND calendar_dt BETWEEN '2021-01-01' AND '2021-12-31'
    );






