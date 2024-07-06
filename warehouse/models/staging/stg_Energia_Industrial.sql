-- models/staging/stg_Energia_Industrial.sql

with Energia_Industrial as (
    select * from {{ source('dbo', 'Energia_Industrial') }}
),

-- transformação dos dados
stg_Energia_Industrial as (
    select
        cast(data as date) as date,
        cast(valor as numeric) as value
    from Energia_Industrial
)

-- retorno dos dados transformados
select * from stg_cambio_dolar
