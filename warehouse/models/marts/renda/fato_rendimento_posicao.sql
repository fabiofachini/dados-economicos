-- models/marts/fato_rendimento_posicao.sql

with stg_ibge__rendimento_mensal_posicao as (
    select * from {{ ref('stg_ibge__rendimento_mensal_posicao') }}
)

-- transformação dos dados

-- retorno dos dados
select * from stg_ibge__rendimento_mensal_posicao