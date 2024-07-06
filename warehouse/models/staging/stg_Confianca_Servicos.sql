-- models/staging/stg_Confianca_Servicos.sql

with Confianca_Servicos as (
    select * from {{ source('dbo', 'Confianca_Servicos') }}
),

-- transformação dos dados
stg_Confianca_Servicos as (
    select
        cast(data as date) as date,
        cast(valor as numeric) as value
    from Confianca_Servicos
)

-- retorno dos dados transformados
select * from stg_Confianca_Servicos
