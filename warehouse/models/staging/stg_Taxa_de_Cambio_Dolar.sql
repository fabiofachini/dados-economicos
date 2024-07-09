-- models/staging/stg_Taxa_de_Cambio_Dolar.sql

with Taxa_de_Cambio_Dolar as (
    select * from {{ source('dbo', 'Taxa_de_Cambio_Dolar') }}
),

-- transformação dos dados
stg_Taxa_de_Cambio_Dolar as (
    select
        CONVERT(DATE, data, 103) AS Data,
        cast(valor as numeric(10,5)) as Taxa_de_Cambio_Dolar
    from Taxa_de_Cambio_Dolar
)

-- retorno dos dados transformados
select * from stg_Taxa_de_Cambio_Dolar
