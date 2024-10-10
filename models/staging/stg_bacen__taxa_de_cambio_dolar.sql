-- models/staging/stg_bacen__taxa_de_cambio_dolar.sql

with taxa_de_cambio_dolar as (
    select * from {{ source('dbo', 'taxa_de_cambio_dolar') }}
),

-- transformação dos dados
stg_bacen__taxa_de_cambio_dolar as (
    select
        CONVERT(DATE, data, 103) AS Data,
        cast(valor as numeric(10,5)) as Taxa_de_Cambio_Dolar
    from taxa_de_cambio_dolar
)

-- retorno dos dados transformados
select * from stg_bacen__taxa_de_cambio_dolar
