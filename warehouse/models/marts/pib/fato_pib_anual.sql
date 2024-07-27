-- models/marts/fato_pib_anual.sql

with stg_ibge__pib_anual as (
    select * from {{ ref('stg_ibge__pib_anual') }}
)

-- retorno dos dados
select * from stg_ibge__pib_anual