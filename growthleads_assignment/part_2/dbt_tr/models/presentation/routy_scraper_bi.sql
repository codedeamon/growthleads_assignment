{{ config(materialized='view', schema='presentation') }}


with legacy as (
    select *
    from {{ref('legacy_scraper_stg')}}
),

tps as (
    select *
    from {{ref('tps_data_stg')}}
),

sheet as (
    select *
    from {{ref('sheet_stake_data_stg')}}
),

ms as (
    select *
    from {{ref('marketing_source_stg')}}
),


concatenated as (

    select *
    from legacy

    union all

    select *
    from tps

--    union all
--
--    select *
--    from sheet
),

final_data as (
    select
        c.*,
        ms.product,
        ms.project_xero,
        ms.extra,
        ms.operator_mapped,
        ms.ppc_website,
        ms.portfolio,
        ms.website,
        ms.channel,
        0 as scraper_id,
        null as backend_name,
        null as backend_software_name,
        null as friendlyname,
        0 as cpa_deal,
        0 as rs_deal,
        null as tracker1


    from concatenated c
    left join ms
    on c.marketing_source = ms.marketing_source
)

select * from final_data