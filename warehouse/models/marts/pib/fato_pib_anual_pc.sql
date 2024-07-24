-- models/marts/fato_pib_anual.sql

with stg_ibge__pib_anual_pc as (
    select * from {{ ref('stg_ibge__pib_anual_pc') }}
)

-- transformação dos dados

-- retorno dos dados
select * from stg_ibge__pib_anual_pc