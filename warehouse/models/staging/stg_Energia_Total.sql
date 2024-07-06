-- models/staging/stg_Energia_Total.sql

with Energia_Total as (
    select * from {{ source('dbo', 'Energia_Total') }}
),

-- transformação dos dados
stg_Energia_Total as (
    select
        cast(data as date) as date,
        cast(valor as numeric) as value
    from Energia_Total
)

-- retorno dos dados transformados
select * from stg_Energia_Total
