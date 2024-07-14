-- models/marts/fato_trabalho.sql

with int_trabalho_joined as (
    select * from {{ ref('int_trabalho_joined') }}
)

-- transformação dos dados

-- retorno dos dados
select * from int_trabalho_joined