-- models/staging/stg_Confianca_Consumidor.sql

with Confianca_Consumidor as (
    select * from {{ source('dbo', 'Confianca_Consumidor') }}
),

-- transformação dos dados
stg_Confianca_Consumidor as (
    select
        cast(data as date) as date,
        cast(valor as numeric) as value
    from Confianca_Consumidor
)

-- retorno dos dados transformados
select * from stg_Confianca_Consumidor
