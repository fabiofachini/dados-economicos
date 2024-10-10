-- models/staging/stg_bacen__confianca_servicos.sql

with confianca_servicos as (
    select * from {{ source('dbo', 'confianca_servicos') }}
),

-- transformação dos dados
stg_bacen__confianca_servicos as (
    select
        CONVERT(DATE, data, 103) AS Data,
        cast(valor as numeric(10,2)) as Confianca_Servicos
    from confianca_servicos
)

-- retorno dos dados transformados
select * from stg_bacen__confianca_servicos
