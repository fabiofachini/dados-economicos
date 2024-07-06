-- models/staging/stg_Taxa_de_Cambio_Libra.sql

with Taxa_de_Cambio_Libra as (
    select * from {{ source('dbo', 'Taxa_de_Cambio_Libra') }}
),

-- transformação dos dados
stg_Taxa_de_Cambio_Libra as (
    select
        cast(data as date) as date,
        cast(valor as numeric) as value
    from Taxa_de_Cambio_Libra
)

-- retorno dos dados transformados
select * from stg_Taxa_de_Cambio_Libra
