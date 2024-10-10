-- models/intermediate/int_ipca_joined.sql

with int_ipca_concat_mes as (
    select * from {{ ref('int_ipca_concat_mes') }}
),

int_ipca_concat_ano as (
    select * from {{ ref('int_ipca_concat_ano') }}
),

int_ipca_concat_12m as (
    select * from {{ ref('int_ipca_concat_12m') }}
),

-- transformação dos dados
int_ipca_concat_transformed as (
    select  
    ipca_m.Data,
    ipca_m.IPCA_ate_2019 AS IPCA_Mes,
    ipca_a.IPCA_ate_2019 AS IPCA_Ano,
    ipca_12.IPCA_ate_2019 AS IPCA_12M

    from int_ipca_concat_mes ipca_m
    
    left join int_ipca_concat_ano ipca_a on ipca_m.Data = ipca_a.Data
    left join int_ipca_concat_12m ipca_12 on ipca_m.Data = ipca_12.Data
)

-- retorno dos dados
select * from int_ipca_concat_transformed