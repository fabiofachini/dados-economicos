-- models/marts/juros.sql

with int_juros_joined as (
    select * from {{ ref('int_juros_joined') }}
)

-- transformação dos dados

-- retorno dos dados
select * from int_juros_joined where Data >= '2000-01-01'