-- models/staging/stg_bacen__cdi_anualizada.sql

with cdi_anualizada as (
    select * from {{ source('dbo', 'cdi_anualizada') }}
),

-- transformação dos dados
stg_bacen__cdi_anualizada as (
    select
        CONVERT(DATE, data, 103) AS Data,
        cast(valor as numeric(10,2)) as CDI_Anualizada
    from cdi_anualizada
)

-- retorno dos dados transformados
select * from stg_bacen__cdi_anualizada
