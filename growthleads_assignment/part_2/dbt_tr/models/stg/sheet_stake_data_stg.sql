-- models/stg/your_seed_file_stg.sql
{{ config(materialized='table', schema='stg') }}
-- Create the staging table
with tps_data as (
    select
    null as account_id,
    null as username,
    coalesce("Brand", null) as brand,
    coalesce("Operator", null) as operator,
    coalesce("Date", null) as date,
    coalesce(marketing_source, null) as marketing_source,
    null as country,
    null as clicks,
    null as downloads,
    coalesce("NRCs", null) as nrcs,
    coalesce("NDCs", null) as ndcs,
    coalesce("QNDCs", null) as qndcs,
    coalesce("Deposits", null) as deposits,
    coalesce("Net Revenue", null) as net_revenue_eur,
    coalesce("Revshare", null) as revshare_eur,
    coalesce("CPA", null) as cpa_eur,
    coalesce("Total Commission", null) as total_commission_eur
    from {{ref('SAMPLE_sheet_stake_data')}}
),

final as (

select
    *
    from tps_data
)

select * from final
