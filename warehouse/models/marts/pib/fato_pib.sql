-- models/marts/fato_pib.sql

with int_pib_joined as (
    select * from {{ ref('int_pib_joined') }}
)

-- transformação dos dados

-- retorno dos dados
select * from int_pib_joined