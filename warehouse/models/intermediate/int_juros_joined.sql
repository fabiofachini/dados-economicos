-- models/intermediate/int_juros_joined.sql

with stg_bacen__cdi_anualizada as (
    select * from {{ ref('stg_bacen__cdi_anualizada') }}
),

stg_bacen__selic_anualizada as (
    select * from {{ ref('stg_bacen__selic_anualizada') }}
),

stg_bacen__selic_meta as (
    select * from {{ ref('stg_bacen__selic_meta') }}
),

-- transformação dos dados
int_juros_joined as (
    select 
        cdi.Data as Data,
        cdi.CDI_Anualizada,
        selic_a.Selic_Anualizada,
        selic_m.Selic_Meta

    from stg_bacen__cdi_anualizada cdi

    left join stg_bacen__selic_anualizada selic_a on cdi.Data = selic_a.Data
    left join stg_bacen__selic_meta selic_m on cdi.Data = selic_m.Data
)

-- retorno dos dados
select * from int_juros_joined