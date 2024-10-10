-- models/intermediate/int_confianca_joined.sql

with stg_bacen__confianca_industrial as (
    select * from {{ ref('stg_bacen__confianca_industrial') }}
),

stg_bacen__confianca_consumidor as (
    select * from {{ ref('stg_bacen__confianca_consumidor') }}
),

stg_bacen__confianca_servicos as (
    select * from {{ ref('stg_bacen__confianca_servicos') }}
),

-- transformação dos dados
int_confianca_joined as (
    select 
        ind.Data as Data,
        ind.Confianca_Industrial,
        cons.Confianca_Consumidor,
        serv.Confianca_Servicos

    from stg_bacen__confianca_industrial ind

    left join stg_bacen__confianca_consumidor cons on ind.Data = cons.Data
    left join stg_bacen__confianca_servicos serv on ind.Data = serv.Data
)

-- retorno dos dados
select * from int_confianca_joined