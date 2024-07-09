-- models/staging/stg_Confianca_Servicos.sql

with Confianca_Servicos as (
    select * from {{ source('dbo', 'Confianca_Servicos') }}
),

-- transformação dos dados
stg_Confianca_Servicos as (
    select
        CONVERT(DATE, data, 103) AS Data,
        cast(valor as numeric(10,2)) as Confianca_Servicos
    from Confianca_Servicos
)

-- retorno dos dados transformados
select * from stg_Confianca_Servicos
