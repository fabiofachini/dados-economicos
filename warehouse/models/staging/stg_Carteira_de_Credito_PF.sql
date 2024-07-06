-- models/staging/stg_Carteira_de_Credito_PF.sql

with Carteira_de_Credito_PF as (
    select * from {{ source('dbo', 'Carteira_de_Credito_PF') }}
),

-- transformação dos dados
stg_Carteira_de_Credito_PF as (
    select
        cast(data as date) as date,
        cast(valor as numeric) as value
    from Carteira_de_Credito_PF
)

-- retorno dos dados transformados
select * from stg_Carteira_de_Credito_PF
