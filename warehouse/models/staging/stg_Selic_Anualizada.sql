-- models/staging/stg_Selic_Anualizada.sql

with Selic_Anualizada as (
    select * from {{ source('dbo', 'Selic_Anualizada') }}
),

-- transformação dos dados
stg_Selic_Anualizada as (
    select
        cast(data as date) as date,
        cast(valor as numeric) as value
    from Selic_Anualizada
)

-- retorno dos dados transformados
select * from stg_Selic_Anualizada
