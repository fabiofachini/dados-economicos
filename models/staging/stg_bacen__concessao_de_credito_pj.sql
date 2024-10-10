-- models/staging/stg_bacen__concessao_de_credito_pj.sql

with concessao_de_credito_pj as (
    select * from {{ source('dbo', 'concessao_de_credito_pj') }}
),

-- transformação dos dados
stg_bacen__concessao_de_credito_pj as (
    select
        CONVERT(DATE, data, 103) AS Data,
        cast(valor as int) as Concessao_de_Credito_PJ
    from concessao_de_credito_pj
)

-- retorno dos dados transformados
select * from stg_bacen__concessao_de_credito_pj
