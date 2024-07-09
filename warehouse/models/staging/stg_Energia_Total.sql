-- models/staging/stg_Energia_Total.sql

with Energia_Total as (
    select * from {{ source('dbo', 'Energia_Total') }}
),

-- transformação dos dados
stg_Energia_Total as (
    select
        CONVERT(DATE, data, 103) AS Data,
        cast(valor as int) as Energia_Total
    from Energia_Total
)

-- retorno dos dados transformados
select * from stg_Energia_Total
