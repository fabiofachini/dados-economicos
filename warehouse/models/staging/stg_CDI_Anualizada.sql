-- models/staging/stg_CDI_Anualizada.sql

with CDI_Anualizada as (
    select * from {{ source('dbo', 'CDI_Anualizada') }}
),

-- transformação dos dados
stg_CDI_Anualizada as (
    select
        CONVERT(DATE, data, 103) AS Data,
        cast(valor as numeric(10,2)) as CDI_Anualizada
    from CDI_Anualizada
)

-- retorno dos dados transformados
select * from stg_CDI_Anualizada
