-- models/marts/fato_pib_anual.sql

with int_pib_anual_joined as (
    select * from {{ ref('int_pib_anual_joined') }}
)

-- transformação dos dados

-- retorno dos dados
select * from int_pib_anual_joined