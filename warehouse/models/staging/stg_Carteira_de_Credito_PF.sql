-- models/staging/stg_Carteira_de_Credito_PF.sql

with Carteira_de_Credito_PF as (
    select * from {{ source('dbo', 'Carteira_de_Credito_PF') }}
),

-- transformação dos dados
stg_Carteira_de_Credito_PF as (
    select
        CONVERT(DATE, data, 103) AS Data,
        cast(valor as int) as Carteira_de_Credito_PF
    from Carteira_de_Credito_PF
)

-- retorno dos dados transformados
select * from stg_Carteira_de_Credito_PF
