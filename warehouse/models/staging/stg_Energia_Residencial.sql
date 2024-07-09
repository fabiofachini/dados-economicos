-- models/staging/stg_Energia_Residencial.sql

with Energia_Residencial as (
    select * from {{ source('dbo', 'Energia_Residencial') }}
),

-- transformação dos dados
stg_Energia_Residencial as (
    select
        CONVERT(DATE, data, 103) AS Data,
        cast(valor as int) as Energia_Residencial
    from Energia_Residencial
)

-- retorno dos dados transformados
select * from stg_Energia_Residencial
