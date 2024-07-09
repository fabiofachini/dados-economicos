-- models/staging/stg_Endividamento_Familias.sql

with Endividamento_Familias as (
    select * from {{ source('dbo', 'Endividamento_Familias') }}
),

-- transformação dos dados
stg_Endividamento_Familias as (
    select
        CONVERT(DATE, data, 103) AS Data,
        cast(valor as numeric(10,2)) as Endividamento_Familias
    from Endividamento_Familias
)

-- retorno dos dados transformados
select * from stg_Endividamento_Familias
