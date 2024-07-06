-- models/staging/stg_Custo_CUB_m2.sql

with Custo_CUB_m2 as (
    select * from {{ source('dbo', 'Custo_CUB_m2') }}
),

-- transformação dos dados
stg_Custo_CUB_m2 as (
    select
        cast(data as date) as date,
        cast(valor as numeric) as value
    from Custo_CUB_m2
)

-- retorno dos dados transformados
select * from stg_Custo_CUB_m2
