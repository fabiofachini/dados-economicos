-- models/staging/stg_Taxa_de_Subocupacao.sql

with Taxa_de_Subocupacao as (
    select * from {{ source('dbo', 'Taxa_de_Subocupacao') }}
),

-- transformação dos dados
stg_Taxa_de_Subocupacao as (
    select
        cast(data as date) as date,
        cast(valor as numeric) as value
    from Taxa_de_Subocupacao
)

-- retorno dos dados transformados
select * from stg_Taxa_de_Subocupacao
