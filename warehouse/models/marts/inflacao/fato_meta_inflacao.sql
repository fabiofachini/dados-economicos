-- models/marts/fato_meta_inflacao.sql

with stg_bacen__selic_meta as (
    select * from {{ ref('stg_bacen__selic_meta') }}
)

-- transformação dos dados

-- retorno dos dados
select * from stg_bacen__selic_meta