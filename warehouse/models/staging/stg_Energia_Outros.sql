-- models/staging/stg_Energia_Outros.sql

with Energia_Outros as (
    select * from {{ source('dbo', 'Energia_Outros') }}
),

-- transformação dos dados
stg_Energia_Outros as (
    select
        cast(data as date) as date,
        cast(valor as numeric) as value
    from Energia_Outros
)

-- retorno dos dados transformados
select * from stg_Energia_Outros
