-- models/staging/stg_bacen__concessao_de_credito_pf.sql

with concessao_de_credito_pf as (
    select * from {{ source('dbo', 'concessao_de_credito_pf') }}
),

-- transformação dos dados
stg_bacen__concessao_de_credito_pf as (
    select
        CONVERT(DATE, data, 103) AS Data,
        cast(valor as int) as Concessao_de_Credito_PF
    from concessao_de_credito_pf
)

-- retorno dos dados transformados
select * from stg_bacen__concessao_de_credito_pf
