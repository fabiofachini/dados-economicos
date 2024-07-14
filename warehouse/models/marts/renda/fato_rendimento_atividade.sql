-- models/marts/fato_rendimento_atividade.sql

with stg_ibge__rendimento_mensal_atividade as (
    select * from {{ ref('stg_ibge__rendimento_mensal_atividade') }}
)

-- transformação dos dados

-- retorno dos dados
select * from stg_ibge__rendimento_mensal_atividade