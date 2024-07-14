-- models/marts/fato_energia.sql

with int_energia_joined as (
    select * from {{ ref('int_energia_joined') }}
)

-- transformação dos dados

-- retorno dos dados
select * from int_energia_joined