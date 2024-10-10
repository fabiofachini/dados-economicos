-- models/staging/stg_bacen__carteira_de_credito_pj.sql

with carteira_de_credito_pj as (
    select * from {{ source('dbo', 'carteira_de_credito_pj') }}
),

-- transformação dos dados
stg_bacen__carteira_de_credito_pj as (
    select
        CONVERT(DATE, data, 103) AS Data,
        cast(valor as int) as Carteira_de_Credito_PJ
    from carteira_de_credito_pj
)

-- retorno dos dados transformados
select * from stg_bacen__carteira_de_credito_pj
