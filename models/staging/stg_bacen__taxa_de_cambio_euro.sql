-- models/staging/stg_bacen__taxa_de_cambio_euro.sql

with taxa_de_cambio_euro as (
    select * from {{ source('dbo', 'taxa_de_cambio_euro') }}
),

-- transformação dos dados
stg_bacen__taxa_de_cambio_euro as (
    select
        CONVERT(DATE, data, 103) AS Data,
        cast(valor as numeric(10,5)) as Taxa_de_Cambio_Euro
    from taxa_de_cambio_euro
)

-- retorno dos dados transformados
select * from stg_bacen__taxa_de_cambio_euro
