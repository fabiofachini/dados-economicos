-- models/marts/fato_meta_inflacao.sql

with stg_bacen__meta_inflacao as (
    select * from {{ ref('stg_bacen__meta_inflacao') }}
)

-- transformação dos dados

-- retorno dos dados
select * from stg_bacen__meta_inflacao