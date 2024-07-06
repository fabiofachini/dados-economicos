-- models/staging/stg_Piramide_Etaria.sql

with Piramide_Etaria as (
    select * from {{ source('dbo', 'Piramide_Etaria') }}
),

-- transformação dos dados
stg_Piramide_Etaria as (
    select
        cast(data as date) as date,
        cast(valor as numeric) as value
    from Piramide_Etaria
)

-- retorno dos dados transformados
select * from stg_Piramide_Etaria
