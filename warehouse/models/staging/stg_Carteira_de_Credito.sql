-- models/staging/stg_Carteira_de_Credito.sql

with Carteira_de_Credito as (
    select * from {{ source('dbo', 'Carteira_de_Credito') }}
),

-- transformação dos dados
stg_Carteira_de_Credito as (
    select
        cast(data as date) as date,
        cast(valor as numeric) as value
    from Carteira_de_Credito
)

-- retorno dos dados transformados
select * from stg_Carteira_de_Credito
