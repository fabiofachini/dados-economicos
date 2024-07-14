-- models/intermediate/int_pib_anual_joined.sql

with stg_ibge__pib_anual_pr as (
    select * from {{ ref('stg_ibge__pib_anual') }}
    where Variável = 'População residente'
),

stg_ibge__pib_anual_pvc as (
    select * from {{ ref('stg_ibge__pib_anual') }}
    where Variável = 'PIB - valores correntes'
),

stg_ibge__pib_anual_pvv as (
    select * from {{ ref('stg_ibge__pib_anual') }}
    where Variável = 'PIB - variação em volume'
),

stg_ibge__pib_anual_pcvc as (
    select * from {{ ref('stg_ibge__pib_anual') }}
    where Variável = 'PIB per capita - valores correntes'
),

stg_ibge__pib_anual_pcvv as (
    select * from {{ ref('stg_ibge__pib_anual') }}
    where Variável = 'PIB per capita - variação em volume'
),

-- transformação dos dados
int_pib_anual_joined as (
    select 
        pr.Data as Data,
        pr.PIB_Anual as Populacao_Residente,
        pvc.PIB_Anual as PIB_Valores_Correntes,
        pvv.PIB_Anual as PIB_Variacao_Volume,
        pcvc.PIB_Anual as PIB_Per_Capita_Valores_Correntes,
        pcvv.PIB_Anual as PIB_Per_Capita_Variacao_Volume
        
    from stg_ibge__pib_anual_pr pr

    left join stg_ibge__pib_anual_pvc pvc on pr.Data = pvc.Data
    left join stg_ibge__pib_anual_pvv pvv on pr.Data = pvv.Data
    left join stg_ibge__pib_anual_pcvc pcvc on pr.Data = pcvc.Data
    left join stg_ibge__pib_anual_pcvv pcvv on pr.Data = pcvv.Data
)

-- retorno dos dados
select * from int_pib_anual_joined