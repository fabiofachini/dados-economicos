-- models/intermediate/int_inflacao_joined.sql

with stg_bacen__igpm_mes as (
    select * from {{ ref('stg_bacen__igpm_mes') }}
),

int_inpc_joined as (
    select * from {{ ref('int_inpc_joined') }}
),

int_ipca_joined as (
    select * from {{ ref('int_ipca_joined') }}
),

-- transformação dos dados
int_inflacao_joined as (
    select  
    igpm.Data,
    igpm.IGPM_Mes,
    inpc.INPC_Mes,
    inpc.INPC_Ano,
    inpc.INPC_12M,
    ipca.IPCA_Mes,
    ipca.IPCA_Ano,
    ipca.IPCA_12M

    from stg_bacen__igpm_mes igpm
    
    left join int_inpc_joined inpc on igpm.Data = inpc.Data
    left join int_ipca_joined ipca on igpm.Data = ipca.Data
)

-- retorno dos dados
select * from int_inflacao_joined where Data >= '2012-01-01'