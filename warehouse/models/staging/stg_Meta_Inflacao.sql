-- models/staging/stg_Meta_Inflacao.sql

with Meta_Inflacao as (
    select * from {{ source('dbo', 'Meta_Inflacao') }}
),

-- transformação dos dados
stg_Meta_Inflacao as (
    select
        CONVERT(DATE, data, 103) AS Data,
        cast(valor as numeric(10,2)) as Meta_Inflacao
    from Meta_Inflacao
)

-- retorno dos dados transformados
select * from stg_Meta_Inflacao
