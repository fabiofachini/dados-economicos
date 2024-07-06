-- models/staging/stg_CDI_Anualizada.sql

with CDI_Anualizada as (
    select * from {{ source('dbo', 'CDI_Anualizada') }}
),

-- transformação dos dados
stg_CDI_Anualizada as (
    select
        cast(data as date) as date,
        cast(valor as numeric) as value
    from CDI_Anualizada
)

-- retorno dos dados transformados
select * from stg_CDI_Anualizada
