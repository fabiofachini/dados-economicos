-- models/marts/fato_pib.sql

with stg_ibge__pib as (
    select * from {{ ref('stg_ibge__pib') }}
)

-- transformação dos dados

-- retorno dos dados
select * from stg_ibge__pib