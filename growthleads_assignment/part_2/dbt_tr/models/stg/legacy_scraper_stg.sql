-- models/stg/your_seed_file_stg.sql
{{ config(materialized='table', schema='stg') }}
-- Create the staging table
with tps_data as (
    select
    coalesce(account_id, null) as account_id, --1
    coalesce(username, null) as username, --2
    coalesce(brand, null) as brand,--3
    coalesce(operator_name, null) as operator, --5
    coalesce(date, null) as date,--7
    coalesce(marketing_source, null) as marketing_source, --8
    null::text as country,
    coalesce(clicks::integer, null::integer) as clicks, --10
    null::integer as downloads,
    coalesce(nrcs::integer, null::integer) as nrcs, --11
    coalesce(ndcs::integer, null::integer) as ndcs,--12
    coalesce(qndcs::integer, null::integer) as qndcs, --13
    coalesce(deposits_eur::float, null::float) as deposits_eur,--14
    coalesce(net_revenue_eur::float, null::float) as net_revenue_eur,--15
    coalesce(revshare_eur::float, null::float) as revshare_eur,--16
    coalesce(cpa_eur::float, null::float) as cpa_eur,--17
    coalesce(total_commission_eur::float, null::float) as total_commission_eur

    from {{ref('SAMPLE_postgres_legacy_scraper')}}
),

final as (

select
    *
    from tps_data
)

select * from final
