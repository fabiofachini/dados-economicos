-- models/marts/int_populacao_joined.sql

with int_populacao_joined as (
    select * from {{ ref('int_populacao_joined') }}
)

-- transformação dos dados

-- retorno dos dados
select * from int_populacao_joined