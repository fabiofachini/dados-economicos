-- models/staging/stg_bacen__energia_residencial.sql

with energia_residencial as (
    select * from {{ source('dbo', 'energia_residencial') }}
),

-- transformação dos dados
stg_bacen__energia_residencial as (
    select
        CONVERT(DATE, data, 103) AS Data,
        cast(valor as int) as Energia_Residencial
    from energia_residencial
)

-- retorno dos dados transformados
select * from stg_bacen__energia_residencial
