-- models/intermediate/int_pib_joined.sql

with stg_ibge__pib as (
    select * from {{ ref('stg_ibge__pib') }}
),

stg_ibge__pib_variacao_trimestral as (
    select * from {{ ref('stg_ibge__pib_variacao_trimestral') }}
),

-- transformação dos dados
int_pib_joined as (
    select 
        pib.Data as Data,
        pib.PIB,
        pib_v.PIB_Variacao_Trimestral
        
    from stg_ibge__pib pib

    left join stg_ibge__pib_variacao_trimestral pib_v on pib.Data = pib_v.Data
)

-- retorno dos dados
select * from int_pib_joined