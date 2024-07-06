-- models/staging/stg_NSFP_Governo_Mes.sql

with NSFP_Governo_Mes as (
    select * from {{ source('dbo', 'NSFP_Governo_Mes') }}
),

-- transformação dos dados
stg_NSFP_Governo_Mes as (
    select
        cast(data as date) as date,
        cast(valor as numeric) as value
    from NSFP_Governo_Mes
)

-- retorno dos dados transformados
select * from stg_NSFP_Governo_Mes
