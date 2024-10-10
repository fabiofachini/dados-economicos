-- models/staging/stg_bacen__confianca_consumidor.sql

with confianca_consumidor as (
    select * from {{ source('dbo', 'confianca_consumidor') }}
),

-- transformação dos dados
stg_bacen__confianca_consumidor as (
    select
        CONVERT(DATE, data, 103) AS Data,
        cast(valor as numeric(10,2)) as Confianca_Consumidor
    from confianca_consumidor
)

-- retorno dos dados transformados
select * from stg_bacen__confianca_consumidor
