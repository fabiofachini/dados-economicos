-- models/marts/fato_gini.sql

with stg_ibge__indice_de_gini as (
    select * from {{ ref('stg_ibge__indice_de_gini') }}
)

-- transformação dos dados

-- retorno dos dados
select * from stg_ibge__indice_de_gini