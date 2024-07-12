-- models/staging/stg_bacen__selic_anualizada.sql

with selic_anualizada as (
    select * from {{ source('dbo', 'selic_anualizada') }}
),

-- transformação dos dados
stg_bacen__selic_anualizada as (
    select
        CONVERT(DATE, data, 103) AS Data,
        cast(valor as numeric(10,2)) as Selic_Anualizada
    from selic_anualizada
)

-- retorno dos dados transformados
select * from stg_bacen__selic_anualizada
