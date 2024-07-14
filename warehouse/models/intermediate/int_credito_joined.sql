-- models/intermediate/int_credito_joined.sql

with stg_bacen__carteira_de_credito_pf as (
    select * from {{ ref('stg_bacen__carteira_de_credito_pf') }}
),

stg_bacen__carteira_de_credito_pj as (
    select * from {{ ref('stg_bacen__carteira_de_credito_pj') }}
),

stg_bacen__carteira_de_credito as (
    select * from {{ ref('stg_bacen__carteira_de_credito') }}
),

stg_bacen__concessao_de_credito_pf as (
    select * from {{ ref('stg_bacen__concessao_de_credito_pf') }}
),

stg_bacen__concessao_de_credito_pj as (
    select * from {{ ref('stg_bacen__concessao_de_credito_pj') }}
),

stg_bacen__concessao_de_credito as (
    select * from {{ ref('stg_bacen__concessao_de_credito') }}
),

-- transformação dos dados
int_credito_joined as (
    select 
        cc.Data as Data_cc,
        cc.Carteira_de_Credito,       
        pf.Carteira_de_Credito_PF,
        pj.Carteira_de_Credito_PJ,
        ccr.Concessao_de_Credito,
        ccpf.Concessao_de_Credito_PF,
        ccpj.Concessao_de_Credito_PJ

    from stg_bacen__carteira_de_credito cc

    left join stg_bacen__carteira_de_credito_pj pj on cc.Data = pj.Data
    left join stg_bacen__carteira_de_credito_pf pf on cc.Data = pf.Data
    left join stg_bacen__concessao_de_credito_pf ccpf on cc.Data = ccpf.Data
    left join stg_bacen__concessao_de_credito_pj ccpj on cc.Data = ccpj.Data
    left join stg_bacen__concessao_de_credito ccr on cc.Data = ccr.Data
)

-- retorno dos dados
select * from int_credito_joined
