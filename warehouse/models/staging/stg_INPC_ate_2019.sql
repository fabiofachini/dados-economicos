-- models/staging/stg_INPC_ate_2019.sql

with INPC_ate_2019 as (
    select * from {{ source('dbo', 'INPC_ate_2019') }}
),

-- transformação dos dados
stg_INPC_ate_2019 as (
    select
        cast(data as date) as date,
        cast(valor as numeric) as value
    from INPC_ate_2019
)

-- retorno dos dados transformados
select * from stg_cambio_dolar
