-- models/staging/stg_bacen__energia_total.sql

with energia_total as (
    select * from {{ source('dbo', 'energia_total') }}
),

-- transformação dos dados
stg_bacen__energia_total as (
    select
        CONVERT(DATE, data, 103) AS Data,
        cast(valor as int) as Energia_Total
    from energia_total
)

-- retorno dos dados transformados
select * from stg_bacen__energia_total
