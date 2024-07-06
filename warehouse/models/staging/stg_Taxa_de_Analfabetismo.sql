-- models/staging/stg_Taxa_de_Analfabetismo.sql

with Taxa_de_Analfabetismo as (
    select * from {{ source('dbo', 'Taxa_de_Analfabetismo') }}
),

-- transformação dos dados
stg_Taxa_de_Analfabetismo as (
    select
        cast(data as date) as date,
        cast(valor as numeric) as value
    from Taxa_de_Analfabetismo
)

-- retorno dos dados transformados
select * from stg_Taxa_de_Analfabetismo
