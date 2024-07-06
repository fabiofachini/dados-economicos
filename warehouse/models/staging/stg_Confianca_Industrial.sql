-- models/staging/stg_Confianca_Industrial.sql

with Confianca_Industrial as (
    select * from {{ source('dbo', 'Confianca_Industrial') }}
),

-- transformação dos dados
stg_Confianca_Industrial as (
    select
        cast(data as date) as date,
        cast(valor as numeric) as value
    from Confianca_Industrial
)

-- retorno dos dados transformados
select * from stg_Confianca_Industrial
