-- models/staging/stg_Meta_Inflacao.sql

with Meta_Inflacao as (
    select * from {{ source('dbo', 'Meta_Inflacao') }}
),

-- transformação dos dados
stg_Meta_Inflacao as (
    select
        cast(data as date) as date,
        cast(valor as numeric) as value
    from Meta_Inflacao
)

-- retorno dos dados transformados
select * from stg_Meta_Inflacao
