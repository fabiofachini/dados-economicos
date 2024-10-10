-- models/staging/stg_bacen__endividamento_familias_s_habitacional.sql

with endividamento_familias_s_habitacional as (
    select * from {{ source('dbo', 'endividamento_familias_s_habitacional') }}
),

-- transformação dos dados
stg_bacen__endividamento_familias_s_habitacional as (
    select
        CONVERT(DATE, data, 103) AS Data,
        cast(valor as numeric(10,2)) as Endividamento_Familias_s_Habitacional
    from endividamento_familias_s_habitacional
)

-- retorno dos dados transformados
select * from stg_bacen__endividamento_familias_s_habitacional
