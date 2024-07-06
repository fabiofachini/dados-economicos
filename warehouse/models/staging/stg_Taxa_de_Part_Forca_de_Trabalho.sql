-- models/staging/stg_Taxa_de_Part_Forca_de_Trabalho.sql

with Taxa_de_Part_Forca_de_Trabalho as (
    select * from {{ source('dbo', 'Taxa_de_Part_Forca_de_Trabalho') }}
),

-- transformação dos dados
stg_Taxa_de_Part_Forca_de_Trabalho as (
    select
        cast(data as date) as date,
        cast(valor as numeric) as value
    from Taxa_de_Part_Forca_de_Trabalho
)

-- retorno dos dados transformados
select * from stg_Taxa_de_Part_Forca_de_Trabalho
