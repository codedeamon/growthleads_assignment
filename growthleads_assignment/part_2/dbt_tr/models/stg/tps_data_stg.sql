-- models/stg/your_seed_file_stg.sql
{{ config(materialized='table', schema='stg') }}

-- Create the staging table
with tps_data as (
    select
    coalesce(t."accountId", null) as account_id,
    null as username,
    coalesce(t.brand,null) as brand,
    null as operator,
    coalesce(t.date, null) as date,
    coalesce(t.tracker, null) as marketing_source,
    coalesce(t.country::text, null) as country,
    coalesce(t.visits::integer, null::integer) as visits,
    coalesce(t.downloads::integer, null::integer) as downloads,
    null::integer as nrcs,
    coalesce(t."firstTimeDeposits"::integer, null::integer) as ndcs,
    null::integer as qndc,
    case
        when lower(t."currencyCode") like 'eur%' then t."depositAmount"::float
        else null::float
    end as deposits_eur,
    case
        when lower(t."currencyCode") like 'eur%' then t."netRevenue"::float
        else null::float
    end as net_revenue_eur,
    case
        when lower(t."currencyCode") like 'eur%' then t."revShareCommission"::float
        else null::float
    end as revshare_eur,
    case
        when lower(t."currencyCode") like 'eur%' then t."cpaCommission"
        else null::float
    end as cpa_eur,
    case
        when lower(t."currencyCode") like 'eur%' then t."calculatedCommission"::float
        else null::float
    end as total_commission_eur
    from {{ref('SAMPLE_postgres_tps_data')}} t
),

final as (

select
    *
    from tps_data
)

select * from final
