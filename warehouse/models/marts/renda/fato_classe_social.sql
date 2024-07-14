-- models/marts/fato_classe_social.sql

with int_classe_social_joined as (
    select * from {{ ref('int_classe_social_joined') }}
)

-- transformação dos dados

-- retorno dos dados
select * from int_classe_social_joined