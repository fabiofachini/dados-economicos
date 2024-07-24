-- models/marts/fato_rendimento.sql

with int_rendimento_joined as (
    select * from {{ ref('int_rendimento_joined') }}
)

-- transformação dos dados

-- retorno dos dados
select Data, Rendimento_Trabalho_Principal from int_rendimento_joined