-- models/staging/stg_Energia_Comercial.sql

with Energia_Comercial as (
    select * from {{ source('dbo', 'Energia_Comercial') }}
),

-- transformação dos dados
stg_Energia_Comercial as (
    select
        cast(data as date) as date,
        cast(valor as numeric) as value
    from Energia_Comercial
)

-- retorno dos dados transformados
select * from stg_Energia_Comercial
