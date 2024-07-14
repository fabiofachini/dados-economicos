-- models/marts/fato_populacao_anual.sql

with stg_ibge__populacao_anual as (
    select * from {{ ref('stg_ibge__populacao_anual') }}
)

-- transformação dos dados

-- retorno dos dados
select * from stg_ibge__populacao_anual