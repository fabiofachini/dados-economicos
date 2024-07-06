-- models/staging/stg_Populacao_Anual.sql

with Populacao_Anual as (
    select * from {{ source('dbo', 'Populacao_Anual') }}
),

-- transformação dos dados
stg_Populacao_Anual as (
    select
        cast(data as date) as date,
        cast(valor as numeric) as value
    from Populacao_Anual
)

-- retorno dos dados transformados
select * from stg_Populacao_Anual
