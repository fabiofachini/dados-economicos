-- models/staging/stg_Envidadamento_Familias_s_Habitacional.sql

with Envidadamento_Familias_s_Habitacional as (
    select * from {{ source('dbo', 'Envidadamento_Familias_s_Habitacional') }}
),

-- transformação dos dados
stg_Envidadamento_Familias_s_Habitacional as (
    select
        CONVERT(DATE, data, 103) AS Data,
        cast(valor as numeric(10,2)) as Envidadamento_Familias_s_Habitacional
    from Envidadamento_Familias_s_Habitacional
)

-- retorno dos dados transformados
select * from stg_Envidadamento_Familias_s_Habitacional
