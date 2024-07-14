-- models/staging/stg_bacen__nfsp_governo_mes.sql

with nfsp_governo_mes as (
    select * from {{ source('dbo', 'nfsp_governo_mes') }}
),

-- transformação dos dados
stg_bacen__nfsp_governo_mes as (
    select
        CONVERT(DATE, data, 103) AS Data,
        cast(valor as numeric(10,2)) as NFSP_Governo_Mes
    from nfsp_governo_mes
)

-- retorno dos dados transformados
select * from stg_bacen__nfsp_governo_mes