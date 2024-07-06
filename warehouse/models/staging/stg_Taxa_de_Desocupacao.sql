-- models/staging/stg_Taxa_de_Desocupacao.sql

with Taxa_de_Desocupacao as (
    select * from {{ source('dbo', 'Taxa_de_Desocupacao') }}
),

-- transformação dos dados
stg_Taxa_de_Desocupacao as (
    select
        cast(data as date) as date,
        cast(valor as numeric) as value
    from Taxa_de_Desocupacao
)

-- retorno dos dados transformados
select * from stg_Taxa_de_Desocupacao
