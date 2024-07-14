-- models/marts/fato_piramide_etaria.sql

with stg_ibge__piramide_etaria as (
    select * from {{ ref('stg_ibge__piramide_etaria') }}
)

-- transformação dos dados

-- retorno dos dados
select * from stg_ibge__piramide_etaria