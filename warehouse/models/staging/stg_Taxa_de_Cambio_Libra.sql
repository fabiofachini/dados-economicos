-- models/staging/stg_Taxa_de_Cambio_Libra.sql

with Taxa_de_Cambio_Libra as (
    select * from {{ source('dbo', 'Taxa_de_Cambio_Libra') }}
),

-- transformação dos dados
stg_Taxa_de_Cambio_Libra as (
    select
        CONVERT(DATE, data, 103) AS Data,
        cast(valor as numeric(10,5)) as Taxa_de_Cambio_Libra
    from Taxa_de_Cambio_Libra
)

-- retorno dos dados transformados
select * from stg_Taxa_de_Cambio_Libra
