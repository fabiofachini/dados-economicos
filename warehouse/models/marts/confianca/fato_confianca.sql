-- models/marts/fato_confianca.sql

with int_confianca_joined as (
    select * from {{ ref('int_confianca_joined') }}
)

-- transformação dos dados

-- retorno dos dados
select * from int_confianca_joined