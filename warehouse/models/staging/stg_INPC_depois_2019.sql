-- models/staging/stg_INPC_depois_2019.sql

with INPC_depois_2019 as (
    select * from {{ source('dbo', 'INPC_depois_2019') }}
),

-- transformação dos dados
stg_INPC_depois_2019 as (
    select
        cast(data as date) as date,
        cast(valor as numeric) as value
    from INPC_depois_2019
)

-- retorno dos dados transformados
select * from stg_INPC_depois_2019
