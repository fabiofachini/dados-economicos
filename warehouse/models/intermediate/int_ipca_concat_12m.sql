-- models/intermediate/int_ipca_concat_12m.sql

with stg_ibge__ipca_ate_2019 as (
    select * from {{ ref('stg_ibge__ipca_ate_2019') }}
),

stg_ibge__ipca_depois_2019 as (
    select * from {{ ref('stg_ibge__ipca_depois_2019') }}
),

-- transformação dos dados
stg_ibge__ipca_concat as (
    select * from stg_ibge__ipca_ate_2019
    UNION ALL
    select * from stg_ibge__ipca_depois_2019
),

int_ipca_concat_12m as (
    select * from stg_ibge__ipca_concat
    where Variável = 'IPCA - Variação acumulada em 12 meses'
)

-- retorno dos dados
select * from int_ipca_concat_12m