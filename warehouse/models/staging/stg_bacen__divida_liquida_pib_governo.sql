-- models/staging/stg_bacen__divida_liquida_pib_governo.sql

with divida_liquida_pib_governo as (
    select * from {{ source('dbo', 'divida_liquida_pib_governo') }}
),

-- transformação dos dados
stg_bacen__divida_liquida_pib_governo as (
    select
        CONVERT(DATE, data, 103) AS Data,
        cast(valor as numeric(10,2)) as Divida_Liquida_PIB_Governo
    from divida_liquida_pib_governo
)

-- retorno dos dados transformados
select * from stg_bacen__divida_liquida_pib_governo
