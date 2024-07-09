-- models/staging/stg_Taxa_de_Cambio_Euro.sql

with Taxa_de_Cambio_Euro as (
    select * from {{ source('dbo', 'Taxa_de_Cambio_Euro') }}
),

-- transformação dos dados
stg_Taxa_de_Cambio_Euro as (
    select
        CONVERT(DATE, data, 103) AS Data,
        cast(valor as numeric(10,5)) as Taxa_de_Cambio_Euro
    from Taxa_de_Cambio_Euro
)

-- retorno dos dados transformados
select * from stg_Taxa_de_Cambio_Euro
