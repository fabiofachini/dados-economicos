-- models/staging/stg_bacen__energia_industrial.sql

with energia_industrial as (
    select * from {{ source('dbo', 'energia_industrial') }}
),

-- transformação dos dados
stg_bacen__energia_industrial as (
    select
        CONVERT(DATE, data, 103) AS Data,
        cast(valor as int) as Energia_Industrial
    from energia_industrial
)

-- retorno dos dados transformados
select * from stg_bacen__energia_industrial
