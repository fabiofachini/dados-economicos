-- models/staging/stg_bacen__energia_comercial.sql

with energia_comercial as (
    select * from {{ source('dbo', 'energia_comercial') }}
),

-- transformação dos dados
stg_bacen__energia_comercial as (
    select
        CONVERT(DATE, data, 103) AS Data,
        cast(valor as int) as Energia_Comercial
    from energia_comercial
)

-- retorno dos dados transformados
select * from stg_bacen__energia_comercial
