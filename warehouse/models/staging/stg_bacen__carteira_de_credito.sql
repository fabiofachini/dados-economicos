-- models/staging/stg_bacen__carteira_de_credito.sql

with carteira_de_credito as (
    select * from {{ source('dbo', 'carteira_de_credito') }}
),

-- transformação dos dados
stg_bacen__carteira_de_credito as (
    select
        CONVERT(DATE, data, 103) AS Data,
        cast(valor as int) as Carteira_de_Credito
    from carteira_de_credito
)

-- retorno dos dados transformados
select * from stg_bacen__carteira_de_credito
