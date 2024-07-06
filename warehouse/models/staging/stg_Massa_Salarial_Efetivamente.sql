-- models/staging/stg_Massa_Salarial_Efetivamente.sql

with Massa_Salarial_Efetivamente as (
    select * from {{ source('dbo', 'Massa_Salarial_Efetivamente') }}
),

-- transformação dos dados
stg_Massa_Salarial_Efetivamente as (
    select
        cast(data as date) as date,
        cast(valor as numeric) as value
    from Massa_Salarial_Efetivamente
)

-- retorno dos dados transformados
select * from stg_Massa_Salarial_Efetivamente
