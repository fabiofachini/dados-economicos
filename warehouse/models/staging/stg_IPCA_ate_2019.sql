-- models/staging/stg_IPCA_ate_2019.sql

with IPCA_ate_2019 as (
    select * from {{ source('dbo', 'IPCA_ate_2019') }}
),

-- transformação dos dados
stg_IPCA_ate_2019 as (
    select
        cast(data as date) as date,
        cast(valor as numeric) as value
    from IPCA_ate_2019
)

-- retorno dos dados transformados
select * from stg_IPCA_ate_2019
