-- models/staging/stg_Confianca_Consumidor.sql

with Confianca_Consumidor as (
    select * from {{ source('dbo', 'Confianca_Consumidor') }}
),

-- transformação dos dados
stg_Confianca_Consumidor as (
    select
        CONVERT(DATE, data, 103) AS Data,
        cast(valor as numeric(10,2)) as Confianca_Consumidor
    from Confianca_Consumidor
)

-- retorno dos dados transformados
select * from stg_Confianca_Consumidor
