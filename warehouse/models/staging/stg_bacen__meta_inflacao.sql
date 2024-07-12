-- models/staging/stg_bacen__meta_inflacao.sql

with meta_inflacao as (
    select * from {{ source('dbo', 'meta_inflacao') }}
),

-- transformação dos dados
stg_bacen__meta_inflacao as (
    select
        CONVERT(DATE, data, 103) AS Data,
        cast(valor as numeric(10,2)) as Meta_Inflacao
    from meta_inflacao
)

-- retorno dos dados transformados
select * from stg_bacen__meta_inflacao
