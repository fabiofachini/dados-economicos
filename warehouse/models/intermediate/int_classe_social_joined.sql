-- models/intermediate/int_classe_social_joined.sql

with stg_ibge__populacao_classe_social as (
    select * from {{ ref('stg_ibge__populacao_classe_social') }}
),

stg_ibge__rendimento_classe_social as (
    select * from {{ ref('stg_ibge__rendimento_classe_social') }}
),

stg_ibge__massa_salarial_por_classe_social as (
    select * from {{ ref('stg_ibge__massa_salarial_por_classe_social') }}
),

-- transformação dos dados
int_classe_social_joined as (
    select 
        pcs.Data as Data,
        pcs.Classes_Sociais_Percentil,
        pcs.Populacao_Classe_Social,
        rcs.Rendimento_Classe_Social,
        mscs.Massa_Salarial_Por_Classe_Social
        
    from stg_ibge__populacao_classe_social pcs

    left join stg_ibge__rendimento_classe_social rcs 
    on pcs.Data = rcs.Data and pcs.Classes_Sociais_Percentil = rcs.Classes_Sociais_Percentil

    left join stg_ibge__massa_salarial_por_classe_social mscs 
    on pcs.Data = mscs.Data and pcs.Classes_Sociais_Percentil = mscs.Classes_Sociais_Percentil
)

-- retorno dos dados
select * from int_classe_social_joined