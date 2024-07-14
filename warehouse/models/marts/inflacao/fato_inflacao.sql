-- models/marts/inflacao.sql

with int_inflacao_joined as (
    select * from {{ ref('int_inflacao_joined') }}
)

-- transformação dos dados

-- retorno dos dados
select * from int_inflacao_joined