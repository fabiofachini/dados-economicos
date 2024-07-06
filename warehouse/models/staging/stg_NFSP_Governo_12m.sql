-- models/staging/stg_NFSP_Governo_12m.sql

with NFSP_Governo_12m as (
    select * from {{ source('dbo', 'NFSP_Governo_12m') }}
),

-- transformação dos dados
stg_NFSP_Governo_12m as (
    select
        cast(data as date) as date,
        cast(valor as numeric) as value
    from NFSP_Governo_12m
)

-- retorno dos dados transformados
select * from stg_NFSP_Governo_12m
