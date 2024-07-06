-- models/staging/stg_Endividamento_Familias.sql

with Endividamento_Familias as (
    select * from {{ source('dbo', 'Endividamento_Familias') }}
),

-- transformação dos dados
stg_Endividamento_Familias as (
    select
        cast(data as date) as date,
        cast(valor as numeric) as value
    from Endividamento_Familias
)

-- retorno dos dados transformados
select * from stg_Endividamento_Familias
