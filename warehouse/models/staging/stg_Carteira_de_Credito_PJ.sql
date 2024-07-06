-- models/staging/Carteira_de_Credito_PJ.sql

with Carteira_de_Credito_PJ as (
    select * from {{ source('dbo', 'Carteira_de_Credito_PJ') }}
),

-- transformação dos dados
stg_Carteira_de_Credito_PJ as (
    select
        cast(data as date) as date,
        cast(valor as numeric) as value
    from Carteira_de_Credito_PJ
)

-- retorno dos dados transformados
select * from stg_Carteira_de_Credito_PJ
