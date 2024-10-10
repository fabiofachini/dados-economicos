-- models/intermediate/int_nfsp_pib_setor_publico_joined.sql

with stg_bacen__nfsp_pib_setor_publico_ano as (
    select * from {{ ref('stg_bacen__nfsp_pib_setor_publico_ano') }}
),

stg_bacen__nfsp_pib_setor_publico_mes as (
    select * from {{ ref('stg_bacen__nfsp_pib_setor_publico_mes') }}
),

-- transformação dos dados
int_nfsp_pib_setor_publico_joined as (
    select 
        ano.Data as Data,
        ano.NFSP_PIB_Setor_Publico_Ano,
        mes.NFSP_PIB_Setor_Publico_Mes

    from stg_bacen__nfsp_pib_setor_publico_ano ano

    left join stg_bacen__nfsp_pib_setor_publico_mes mes on ano.Data = mes.Data
)

-- retorno dos dados
select * from int_nfsp_pib_setor_publico_joined
