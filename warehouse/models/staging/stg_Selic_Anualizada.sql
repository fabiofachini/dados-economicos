-- models/staging/stg_Selic_Anualizada.sql

with Selic_Anualizada as (
    select * from {{ source('dbo', 'Selic_Anualizada') }}
),

-- transformação dos dados
stg_Selic_Anualizada as (
    select
        CONVERT(DATE, data, 103) AS Data,
        cast(valor as numeric(10,2)) as Selic_Anualizada
    from Selic_Anualizada
)

-- retorno dos dados transformados
select * from stg_Selic_Anualizada
