-- models/stg/your_seed_file_stg.sql
{{ config(materialized='table', schema='stg') }}
-- Create the staging table
with tps_data as (
    select *
    from {{ref('SAMPLE_marketing_source')}}
),

final as (

select
    *
    from tps_data
)

select * from final
