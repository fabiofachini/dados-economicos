-- models/intermediate/int_contas_publicas_joined.sql

with stg_bacen__nfsp_governo_12m as (
    select * from {{ ref('stg_bacen__nfsp_governo_12m') }}
),

stg_bacen__nfsp_governo_ano as (
    select * from {{ ref('stg_bacen__nfsp_governo_ano') }}
),

stg_bacen__nfsp_governo_mes as (
    select * from {{ ref('stg_bacen__nfsp_governo_mes') }}
),

stg_bacen__nfsp_pib_governo_12m as (
    select * from {{ ref('stg_bacen__nfsp_pib_governo_12m') }}
),

stg_bacen__nfsp_pib_governo_ano as (
    select * from {{ ref('stg_bacen__nfsp_pib_governo_ano') }}
),

stg_bacen__nfsp_pib_governo_mes as (
    select * from {{ ref('stg_bacen__nfsp_pib_governo_mes') }}
),

stg_bacen__nfsp_pib_setor_publico_12m as (
    select * from {{ ref('stg_bacen__nfsp_pib_setor_publico_12m') }}
),

stg_bacen__nfsp_pib_setor_publico_ano as (
    select * from {{ ref('stg_bacen__nfsp_pib_setor_publico_ano') }}
),

stg_bacen__nfsp_pib_setor_publico_mes as (
    select * from {{ ref('stg_bacen__nfsp_pib_setor_publico_mes') }}
),

stg_bacen__nfsp_setor_publico_12m as (
    select * from {{ ref('stg_bacen__nfsp_setor_publico_12m') }}
),

stg_bacen__nfsp_setor_publico_ano as (
    select * from {{ ref('stg_bacen__nfsp_setor_publico_ano') }}
),

stg_bacen__nfsp_setor_publico_mes as (
    select * from {{ ref('stg_bacen__nfsp_setor_publico_mes') }}
),

-- transformação dos dados
int_contas_publicas_joined as (
    select 
        ng12m.Data as Data,
        ng12m.NFSP_Governo_12M,
        nga.NFSP_Governo_Ano,
        ngm.NFSP_Governo_Mes,
        np12m.NFSP_PIB_Governo_12M,
        npa.NFSP_PIB_Governo_Ano,
        npm.NFSP_PIB_Governo_Mes,
        nsp12m.NFSP_PIB_Setor_Publico_12M,
        nspa.NFSP_PIB_Setor_Publico_Ano,
        nspm.NFSP_PIB_Setor_Publico_Mes,
        nsp12m_sp.NFSP_Setor_Publico_12M,
        nspa_sp.NFSP_Setor_Publico_Ano,
        nspm_sp.NFSP_Setor_Publico_Mes

    from stg_bacen__nfsp_governo_12m ng12m

    left join stg_bacen__nfsp_governo_ano nga on ng12m.Data = nga.Data
    left join stg_bacen__nfsp_governo_mes ngm on ng12m.Data = ngm.Data
    left join stg_bacen__nfsp_pib_governo_12m np12m on ng12m.Data = np12m.Data
    left join stg_bacen__nfsp_pib_governo_ano npa on ng12m.Data = npa.Data
    left join stg_bacen__nfsp_pib_governo_mes npm on ng12m.Data = npm.Data
    left join stg_bacen__nfsp_pib_setor_publico_12m nsp12m on ng12m.Data = nsp12m.Data
    left join stg_bacen__nfsp_pib_setor_publico_ano nspa on ng12m.Data = nspa.Data
    left join stg_bacen__nfsp_pib_setor_publico_mes nspm on ng12m.Data = nspm.Data
    left join stg_bacen__nfsp_setor_publico_12m nsp12m_sp on ng12m.Data = nsp12m_sp.Data
    left join stg_bacen__nfsp_setor_publico_ano nspa_sp on ng12m.Data = nspa_sp.Data
    left join stg_bacen__nfsp_setor_publico_mes nspm_sp on ng12m.Data = nspm_sp.Data
)

-- retorno dos dados
select * from int_contas_publicas_joined