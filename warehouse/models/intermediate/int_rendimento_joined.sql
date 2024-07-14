-- models/intermediate/int_rendimento_joined.sql

with stg_ibge__rendimento_todos_os_trabalhos as (
    select * from {{ ref('stg_ibge__rendimento_todos_os_trabalhos') }}
),

stg_ibge__rendimento_trabalho_principal as (
    select * from {{ ref('stg_ibge__rendimento_trabalho_principal') }}
),

stg_ibge__massa_salarial_efetivamente as (
    select * from {{ ref('stg_ibge__massa_salarial_efetivamente') }}
),

stg_ibge__massa_salarial_habitualmente as (
    select * from {{ ref('stg_ibge__massa_salarial_habitualmente') }}
),

-- transformação dos dados
int_rendimento_joined as (
    select 
        rtt.Data as Data,
        rtt.Rendimento_Todos_os_Trabalhos,
        rtp.Rendimento_Trabalho_Principal,
        mse.Massa_Salarial_Efetivamente,
        msh.Massa_Salarial_Habitualmente
        
    from stg_ibge__rendimento_todos_os_trabalhos rtt

    left join stg_ibge__rendimento_trabalho_principal rtp on rtt.Data = rtp.Data
    left join stg_ibge__massa_salarial_efetivamente mse on rtt.Data = mse.Data
    left join stg_ibge__massa_salarial_habitualmente msh on rtt.Data = msh.Data
)

-- retorno dos dados
select * from int_rendimento_joined