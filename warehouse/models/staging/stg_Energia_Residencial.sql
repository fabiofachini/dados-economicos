-- models/staging/stg_Energia_Residencial.sql

with Energia_Residencial as (
    select * from {{ source('dbo', 'Energia_Residencial') }}
),

-- transformação dos dados
stg_Energia_Residencial as (
    select
        cast(data as date) as date,
        cast(valor as numeric) as value
    from Energia_Residencial
)

-- retorno dos dados transformados
select * from stg_Energia_Residencial
