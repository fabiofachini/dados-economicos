-- models/staging/stg_Divida_Liquida_PIB_Governo.sql

with Divida_Liquida_PIB_Governo as (
    select * from {{ source('dbo', 'Divida_Liquida_PIB_Governo') }}
),

-- transformação dos dados
stg_Divida_Liquida_PIB_Governo as (
    select
        CONVERT(DATE, data, 103) AS Data,
        cast(valor as numeric(10,2)) as Divida_Liquida_PIB_Governo
    from Divida_Liquida_PIB_Governo
)

-- retorno dos dados transformados
select * from stg_Divida_Liquida_PIB_Governo
