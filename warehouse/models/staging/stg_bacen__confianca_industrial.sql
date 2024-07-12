-- models/staging/stg_bacen__confianca_industrial.sql

with confianca_industrial as (
    select * from {{ source('dbo', 'confianca_industrial') }}
),

-- transformação dos dados
stg_bacen__confianca_industrial as (
    select
        CONVERT(DATE, data, 103) AS Data,
        cast(valor as numeric(10,2)) as Confianca_Industrial
    from confianca_industrial
)

-- retorno dos dados transformados
select * from stg_bacen__confianca_industrial
