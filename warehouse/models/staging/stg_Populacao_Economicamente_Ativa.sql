-- models/staging/stg_Populacao_Economicamente_Ativa.sql

with Populacao_Economicamente_Ativa as (
    select * from {{ source('dbo', 'Populacao_Economicamente_Ativa') }}
),

-- transformação dos dados
stg_Populacao_Economicamente_Ativa as (
    select
        cast(data as date) as date,
        cast(valor as numeric) as value
    from Populacao_Economicamente_Ativa
)

-- retorno dos dados transformados
select * from stg_Populacao_Economicamente_Ativa
