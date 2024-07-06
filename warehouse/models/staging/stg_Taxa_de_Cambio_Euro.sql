-- models/staging/stg_Taxa_de_Cambio_Euro.sql

with Taxa_de_Cambio_Euro as (
    select * from {{ source('dbo', 'Taxa_de_Cambio_Euro') }}
),

-- transformação dos dados
stg_Taxa_de_Cambio_Euro as (
    select
        cast(data as date) as date,
        cast(valor as numeric) as value
    from Taxa_de_Cambio_Euro
)

-- retorno dos dados transformados
select * from stg_Taxa_de_Cambio_Euro
