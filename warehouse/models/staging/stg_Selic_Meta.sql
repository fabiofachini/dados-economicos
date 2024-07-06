-- models/staging/stg_Selic_Meta.sql

with Selic_Meta as (
    select * from {{ source('dbo', 'Selic_Meta') }}
),

-- transformação dos dados
stg_Selic_Meta as (
    select
        cast(data as date) as date,
        cast(valor as numeric) as value
    from Selic_Meta
)

-- retorno dos dados transformados
select * from stg_Selic_Meta
