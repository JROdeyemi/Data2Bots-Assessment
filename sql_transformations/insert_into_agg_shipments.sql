-- Transform and insert data into table
INSERT INTO joshodey2178_analytics.agg_shipments
SELECT
	CURRENT_DATE AS ingestion_date,
    COUNT(1) FILTER (WHERE s.delivery_date IS NULL AND s.shipment_date IS NOT NULL AND (CAST(s.shipment_date AS DATE) - CAST(o.order_date AS DATE)) >= 6) AS late_shipments,
    COUNT(1) FILTER (WHERE s.delivery_date IS NULL AND s.shipment_date IS NULL AND ('2022-09-05' - CAST(o.order_date AS DATE)) = 15) AS undelivered_shipments
FROM
    joshodey2178_staging.fact_shipment_deliveries AS s
    JOIN joshodey2178_staging.fact_orders AS o ON s.order_id = o.order_id;
	
