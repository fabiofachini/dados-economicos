-- models/marts/fato_classe_social_limites.sql

with stg_ibge__limites_classe_social as (
    select * from {{ ref('stg_ibge__limites_classe_social') }}
)

-- transformação dos dados

-- retorno dos dados
select * from stg_ibge__limites_classe_social