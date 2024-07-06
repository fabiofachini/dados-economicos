-- models/staging/stg_Taxa_de_Desalentados.sql

with Taxa_de_Desalentados as (
    select * from {{ source('dbo', 'Taxa_de_Desalentados') }}
),

-- transformação dos dados
stg_Taxa_de_Desalentados as (
    select
        cast(data as date) as date,
        cast(valor as numeric) as value
    from Taxa_de_Desalentados
)

-- retorno dos dados transformados
select * from stg_Taxa_de_Desalentados
