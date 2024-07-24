-- models/marts/fato_pib_anual.sql

with stg_ibge__pib_variacao_trimestral as (
    select * from {{ ref('stg_ibge__pib_variacao_trimestral') }}
)

-- transformação dos dados

-- retorno dos dados
select * from stg_ibge__pib_variacao_trimestral