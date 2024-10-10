-- models/marts/fato_endividamento.sql

with int_endividamento_joined as (
    select * from {{ ref('int_endividamento_joined') }}
)

-- transformação dos dados

-- retorno dos dados
select * from int_endividamento_joined