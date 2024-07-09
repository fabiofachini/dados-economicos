-- models/staging/stg_Energia_Outros.sql

with Energia_Outros as (
    select * from {{ source('dbo', 'Energia_Outros') }}
),

-- transformação dos dados
stg_Energia_Outros as (
    select
        CONVERT(DATE, data, 103) AS Data,
        cast(valor as int) as Energia_Outros
    from Energia_Outros
)

-- retorno dos dados transformados
select * from stg_Energia_Outros
