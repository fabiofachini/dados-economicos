-- models/staging/stg_Divida_Liquida_PIB_Governo.sql

with Divida_Liquida_PIB_Governo as (
    select * from {{ source('dbo', 'Divida_Liquida_PIB_Governo') }}
),

-- transformação dos dados
stg_Divida_Liquida_PIB_Governo as (
    select
        cast(data as date) as date,
        cast(valor as numeric) as value
    from Divida_Liquida_PIB_Governo
)

-- retorno dos dados transformados
select * from stg_Divida_Liquida_PIB_Governo
