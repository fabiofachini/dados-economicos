-- models/staging/stg_Massa_Salarial_Habitualmente.sql

with Massa_Salarial_Habitualmente as (
    select * from {{ source('dbo', 'Massa_Salarial_Habitualmente') }}
),

-- transformação dos dados
stg_Massa_Salarial_Habitualmente as (
    select
        cast(data as date) as date,
        cast(valor as numeric) as value
    from Massa_Salarial_Habitualmente
)

-- retorno dos dados transformados
select * from stg_Massa_Salarial_Habitualmente
