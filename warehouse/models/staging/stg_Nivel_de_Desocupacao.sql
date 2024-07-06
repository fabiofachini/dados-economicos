-- models/staging/stg_Nivel_de_Desocupacao.sql

with Nivel_de_Desocupacao as (
    select * from {{ source('dbo', 'Nivel_de_Desocupacao') }}
),

-- transformação dos dados
stg_Nivel_de_Desocupacao as (
    select
        cast(data as date) as date,
        cast(valor as numeric) as value
    from Nivel_de_Desocupacao
)

-- retorno dos dados transformados
select * from stg_Nivel_de_Desocupacao
