-- models/staging/stg_Envidadamento_Familias_s_Habitacional.sql

with Envidadamento_Familias_s_Habitacional as (
    select * from {{ source('dbo', 'Envidadamento_Familias_s_Habitacional') }}
),

-- transformação dos dados
stg_Envidadamento_Familias_s_Habitacional as (
    select
        cast(data as date) as date,
        cast(valor as numeric) as value
    from Envidadamento_Familias_s_Habitacional
)

-- retorno dos dados transformados
select * from stg_Envidadamento_Familias_s_Habitacional
