-- models/stg/your_seed_file_stg.sql
{{ config(materialized='table', schema='stg') }}
-- Create the staging table
with tps_data as (
    select
        coalesce(ms.marketing_source, null) as marketing_source,
        ms.product,
        ms.project_xero,
        ms.extra,
        ms.operator_mapped,
        ms.ppc_website,
        ms.portfolio,
        ms.website,
        ms.acq_channel as channel

    from {{ref('SAMPLE_marketing_source')}} ms
    where ms.marketing_source is not null
),

final as (

select
    *
    from tps_data
)

select * from final
