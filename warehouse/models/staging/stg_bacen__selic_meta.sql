-- models/staging/stg_bacen__selic_meta.sql

with selic_meta as (
    select * from {{ source('dbo', 'selic_meta') }}
),

-- transformação dos dados
stg_bacen__selic_meta as (
    select
        CONVERT(DATE, data, 103) AS Data,
        cast(valor as numeric(10,2)) as Selic_Meta
    from selic_meta
)

-- retorno dos dados transformados
select * from stg_bacen__selic_meta
