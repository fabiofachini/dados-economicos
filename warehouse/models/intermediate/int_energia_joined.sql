-- models/intermediate/int_energia_joined.sql

with stg_bacen__energia_comercial as (
    select * from {{ ref('stg_bacen__energia_comercial') }}
),

stg_bacen__energia_industrial as (
    select * from {{ ref('stg_bacen__energia_industrial') }}
),

stg_bacen__energia_outros as (
    select * from {{ ref('stg_bacen__energia_outros') }}
),

stg_bacen__energia_residencial as (
    select * from {{ ref('stg_bacen__energia_residencial') }}
),

stg_bacen__energia_total as (
    select * from {{ ref('stg_bacen__energia_total') }}
),

-- transformação dos dados
int_energia_joined as (
    select 
        ec.Data as Data,
        ec.Energia_Comercial,       
        ei.Energia_Industrial,
        eo.Energia_Outros,
        er.Energia_Residencial,
        et.Energia_Total

    from stg_bacen__energia_comercial ec

    left join stg_bacen__energia_industrial ei on ec.Data = ei.Data
    left join stg_bacen__energia_outros eo on ec.Data = eo.Data
    left join stg_bacen__energia_residencial er on ec.Data = er.Data
    left join stg_bacen__energia_total et on ec.Data = et.Data
)

-- retorno dos dados
select * from int_energia_joined
