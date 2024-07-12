-- models/staging/stg_bacen__energia_outros.sql

with energia_outros as (
    select * from {{ source('dbo', 'energia_outros') }}
),

-- transformação dos dados
stg_bacen__energia_outros as (
    select
        CONVERT(DATE, data, 103) AS Data,
        cast(valor as int) as Energia_Outros
    from energia_outros
)

-- retorno dos dados transformados
select * from stg_bacen__energia_outros
