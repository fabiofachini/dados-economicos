-- models/intermediate/int_cambio_joined.sql

with stg_bacen__taxa_de_cambio_dolar as (
    select * from {{ ref('stg_bacen__taxa_de_cambio_dolar') }}
),

stg_bacen__taxa_de_cambio_euro as (
    select * from {{ ref('stg_bacen__taxa_de_cambio_euro') }}
),

stg_bacen__taxa_de_cambio_libra as (
    select * from {{ ref('stg_bacen__taxa_de_cambio_libra') }}
),

-- transformação dos dados
int_cambio_joined as (
    select 
        dolar.Data as Data,
        dolar.Taxa_de_Cambio_Dolar,
        euro.Taxa_de_Cambio_Euro,
        libra.Taxa_de_Cambio_Libra

    from stg_bacen__taxa_de_cambio_dolar dolar

    left join stg_bacen__taxa_de_cambio_euro euro on dolar.Data = euro.Data
    left join stg_bacen__taxa_de_cambio_libra libra on dolar.Data = libra.Data
)

-- retorno dos dados
select * from int_cambio_joined