-- models/staging/stg_Energia_Comercial.sql

with Energia_Comercial as (
    select * from {{ source('dbo', 'Energia_Comercial') }}
),

-- transformação dos dados
stg_Energia_Comercial as (
    select
        CONVERT(DATE, data, 103) AS Data,
        cast(valor as int) as Energia_Comercial
    from Energia_Comercial
)

-- retorno dos dados transformados
select * from stg_Energia_Comercial
