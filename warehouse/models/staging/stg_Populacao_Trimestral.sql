-- models/staging/stg_Populacao_Trimestral.sql

with Populacao_Trimestral as (
    select * from {{ source('dbo', 'Populacao_Trimestral') }}
),

-- transformação dos dados
stg_Populacao_Trimestral as (
    select
        cast(data as date) as date,
        cast(valor as numeric) as value
    from Populacao_Trimestral
)

-- retorno dos dados transformados
select * from stg_Populacao_Trimestral
