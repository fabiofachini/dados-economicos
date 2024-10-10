-- models/marts/fato_analfabetismo.sql

with int_analfabetismo_joined as (
    select * from {{ ref('int_analfabetismo_joined') }}
)

-- transformação dos dados

-- retorno dos dados
select * from int_analfabetismo_joined