-- models/staging/stg_bacen__taxa_de_cambio_libra.sql

with taxa_de_cambio_libra as (
    select * from {{ source('dbo', 'taxa_de_cambio_libra') }}
),

-- transformação dos dados
stg_bacen__taxa_de_cambio_libra as (
    select
        CONVERT(DATE, data, 103) AS Data,
        cast(valor as numeric(10,5)) as Taxa_de_Cambio_Libra
    from taxa_de_cambio_libra
)

-- retorno dos dados transformados
select * from stg_bacen__taxa_de_cambio_libra
