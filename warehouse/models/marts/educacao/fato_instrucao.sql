-- models/marts/fato_instrucao.sql

with stg_ibge__nivel_de_instrucao as (
    select * from {{ ref('stg_ibge__nivel_de_instrucao') }}
)

-- transformação dos dados

-- retorno dos dados
select * from stg_ibge__nivel_de_instrucao