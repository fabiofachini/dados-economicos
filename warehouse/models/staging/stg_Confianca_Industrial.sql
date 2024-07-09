-- models/staging/stg_Confianca_Industrial.sql

with Confianca_Industrial as (
    select * from {{ source('dbo', 'Confianca_Industrial') }}
),

-- transformação dos dados
stg_Confianca_Industrial as (
    select
        CONVERT(DATE, data, 103) AS Data,
        cast(valor as numeric(10,2)) as Confianca_Industrial
    from Confianca_Industrial
)

-- retorno dos dados transformados
select * from stg_Confianca_Industrial
