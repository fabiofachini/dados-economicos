-- models/intermediate/int_inpc_joined.sql

with int_inpc_concat_mes as (
    select * from {{ ref('int_inpc_concat_mes') }}
),

int_inpc_concat_ano as (
    select * from {{ ref('int_inpc_concat_ano') }}
),

int_inpc_concat_12m as (
    select * from {{ ref('int_inpc_concat_12m') }}
),

-- transformação dos dados
int_inpc_concat_transformed as (
    select  
    inpc_m.Data,
    inpc_m.INPC_ate_2019 AS INPC_Mes,
    inpc_a.INPC_ate_2019 AS INPC_Ano,
    inpc_12.INPC_ate_2019 AS INPC_12M

    from int_inpc_concat_mes inpc_m
    
    left join int_inpc_concat_ano inpc_a on inpc_m.Data = inpc_a.Data
    left join int_inpc_concat_12m inpc_12 on inpc_m.Data = inpc_12.Data
)

-- retorno dos dados
select * from int_inpc_concat_transformed