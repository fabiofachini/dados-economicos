-- models/staging/stg_PIB.sql

with PIB as (
    select * from {{ source('dbo', 'PIB') }}
),

-- transformação dos dados
stg_PIB as (
    select
        cast(data as date) as date,
        cast(valor as numeric) as value
    from PIB
)

-- retorno dos dados transformados
select * from stg_PIB
