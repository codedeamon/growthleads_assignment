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

    select
    account_id, --1
    username,--2
    brand,--3
    operator_name as operator,--5
    date,--7
    marketing_source,--8
    null as country,
    clicks,--10
    null as downloads,
    nrcs,--11
    ndcs,--12
    qndcs,--13
    deposits_eur,--14
    net_revenue_eur,--15
    revshare_eur,--16
    cpa_eur,--17
    total_commission_eur
    from legacy

    union all

    select
    t."accountId" as account_id,
    null as username,
    t.brand,
    null as operator,
    t.date,
    t.tracker as marketing_source,
    t.country,
    t.visits as clicks,
    t.downloads,
    null as nrcs,
    t."firstTimeDeposits" as ndcs,
    null as qndc,
    t."depositAmount" as deposits_eur,
    t."netRevenue" as net_revenue_eur,
    t."revShareCommission" as revshare_eur,
    t."cpaCommission" as cpa_eur,
    t."calculatedCommission" as total_commission_eur

    from tps t

    union all

    select
    null as account_id,
    null as username,
    "Brand" as brand,
    "Operator" as operator,
    "Date" as date,
    marketing_source,
    null as country,
    null as clicks,
    null as downloads,
    "NRCs" as nrcs,
    "NDCs" as ndcs,
    "QNDCs" as qndcs,
    "Deposits" as deposits,
    "Net Revenue" as net_revenue_eur,
    "Revshare" as revshare_eur,
    "CPA" as cpa_eur,
    "Total Commission" as total_commission_eur

--    Portfolio,Date,Week_End,Month,Operator,Brand,marketing_source,NRCs,NDCs,QNDCs,Deposits,Net Revenue,Revshare,CPA,Total Commission
    from sheet
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
        ms.acq_channel,
        0 as scraper_id,
        null as backend_name,
        null as backend_software_name,
        null as friendlyname,
        0 as cpa_deal,
        0 as rs_deal,
        null as tracker1

--        product,project_xero,country,extra,operator_mapped,promocode,ppc_website,website,market,acq_channel,portfolio



    from concatenated c
    left join ms
    on c.marketing_source = ms.marketing_source
)

--final_data as (
--    select
--       *
--    from concatenated c
--)

select * from final_data