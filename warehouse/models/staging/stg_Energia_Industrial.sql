-- models/staging/stg_Energia_Industrial.sql

with Energia_Industrial as (
    select * from {{ source('dbo', 'Energia_Industrial') }}
),

-- transformação dos dados
stg_Energia_Industrial as (
    select
        CONVERT(DATE, data, 103) AS Data,
        cast(valor as int) as Energia_Industrial
    from Energia_Industrial
)

-- retorno dos dados transformados
select * from stg_cambio_dolar
