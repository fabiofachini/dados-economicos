-- models/staging/stg_Taxa_de_Cambio_Dolar.sql

with Taxa_de_Cambio_Dolar as (
    select * from {{ source('dbo', 'Taxa_de_Cambio_Dolar') }}
),

-- transformação dos dados
stg_Taxa_de_Cambio_Dolar as (
    select
        cast(data as date) as date,
        cast(valor as numeric) as value
    from Taxa_de_Cambio_Dolar
)

-- retorno dos dados transformados
select * from stg_Taxa_de_Cambio_Dolar
