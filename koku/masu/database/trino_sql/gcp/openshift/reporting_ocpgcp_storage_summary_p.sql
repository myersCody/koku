-- Populate the daily aggregate line item data
INSERT INTO postgres.{{schema_name | sqlsafe}}.reporting_ocpgcp_storage_summary_p (
    id,
    cluster_id,
    cluster_alias,
    usage_start,
    usage_end,
    usage_amount,
    unit,
    account_id,
    service_id,
    service_alias,
    unblended_cost,
    markup_cost,
    currency,
    source_uuid,
    credit_amount,
    invoice_month
)
    SELECT uuid() as id,
        cluster_id,
        cluster_alias,
        usage_start,
        usage_end,
        CASE
            WHEN max(unit) IN ('gibibyte month', 'gibibyte', 'gibibyte hour')
            THEN cast(sum(usage_amount) * 1.073741824 AS decimal(24,9)) -- Convert to gigabyte
            ELSE cast(sum(usage_amount) AS decimal(24,9))
        END as usage_amount,
        CASE max(unit)
            WHEN 'hour' THEN 'Hrs'
            WHEN 'gibibyte' THEN 'GB'
            WHEN 'gibibyte month' THEN 'GB-Mo'
            WHEN 'gibibyte hour' THEN 'GB-Hours'
            ELSE max(unit)
        END as unit,
        account_id,
        service_id,
        service_alias,
        sum(unblended_cost) as unblended_cost,
        sum(markup_cost) as markup_cost,
        max(currency) as currency,
        cast({{gcp_source_uuid}} as uuid) as source_uuid,
        sum(credit_amount) as credit_amount,
        invoice_month
    FROM hive.{{schema_name | sqlsafe}}.reporting_ocpgcpcostlineitem_project_daily_summary
    -- Get data for this month or last month
    WHERE gcp_source = {{gcp_source_uuid}}
        AND ocp_source = {{ocp_source_uuid}}
        AND invoice_month = {{invoice_month}}
        AND year = {{year}}
        AND lpad(month, 2, '0') = {{month}} -- Zero pad the month when fewer than 2 characters
        AND day in {{days | inclause}}
        AND usage_start >= {{start_date}}
        AND usage_start <= date_add('day', 1, {{end_date}})
        AND service_alias IN ('Filestore', 'Storage', 'Cloud Storage', 'Data Transfer')
    GROUP BY cluster_id,
        cluster_alias,
        usage_start,
        usage_end,
        account_id,
        service_id,
        service_alias,
        invoice_month
