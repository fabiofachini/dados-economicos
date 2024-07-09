-- models/staging/Carteira_de_Credito_PJ.sql

with Carteira_de_Credito_PJ as (
    select * from {{ source('dbo', 'Carteira_de_Credito_PJ') }}
),

-- transformação dos dados
stg_Carteira_de_Credito_PJ as (
    select
        CONVERT(DATE, data, 103) AS Data,
        cast(valor as int) as Carteira_de_Credito_PJ
    from Carteira_de_Credito_PJ
)

-- retorno dos dados transformados
select * from stg_Carteira_de_Credito_PJ
