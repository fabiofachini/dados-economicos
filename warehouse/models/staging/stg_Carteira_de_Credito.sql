-- models/staging/stg_Carteira_de_Credito.sql

with Carteira_de_Credito as (
    select * from {{ source('dbo', 'Carteira_de_Credito') }}
),

-- transformação dos dados
stg_Carteira_de_Credito as (
    select
        CONVERT(DATE, data, 103) AS Data,
        cast(valor as int) as Carteira_de_Credito
    from Carteira_de_Credito
)

-- retorno dos dados transformados
select * from stg_Carteira_de_Credito
