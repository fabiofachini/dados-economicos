-- models/staging/stg_Taxa_de_Informalidade.sql

with Taxa_de_Informalidade as (
    select * from {{ source('dbo', 'Taxa_de_Informalidade') }}
),

-- transformação dos dados
stg_Taxa_de_Informalidade as (
    select
        cast(data as date) as date,
        cast(valor as numeric) as value
    from Taxa_de_Informalidade
)

-- retorno dos dados transformados
select * from stg_Taxa_de_Informalidade
