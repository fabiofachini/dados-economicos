-- models/staging/stg_Selic_Meta.sql

with Selic_Meta as (
    select * from {{ source('dbo', 'Selic_Meta') }}
),

-- transformação dos dados
stg_Selic_Meta as (
    select
        CONVERT(DATE, data, 103) AS Data,
        cast(valor as numeric(10,2)) as Selic_Meta
    from Selic_Meta
)

-- retorno dos dados transformados
select * from stg_Selic_Meta
