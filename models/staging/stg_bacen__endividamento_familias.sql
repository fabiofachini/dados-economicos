-- models/staging/stg_bacen__endividamento_familias.sql

with endividamento_familias as (
    select * from {{ source('dbo', 'endividamento_familias') }}
),

-- transformação dos dados
stg_bacen__endividamento_familias as (
    select
        CONVERT(DATE, data, 103) AS Data,
        cast(valor as numeric(10,2)) as Endividamento_Familias
    from endividamento_familias
)

-- retorno dos dados transformados
select * from stg_bacen__endividamento_familias
