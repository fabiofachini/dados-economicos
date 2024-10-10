-- models/staging/stg_bacen__concessao_de_credito.sql

with concessao_de_credito as (
    select * from {{ source('dbo', 'concessao_de_credito') }}
),

-- transformação dos dados
stg_bacen__concessao_de_credito as (
    select
        CONVERT(DATE, data, 103) AS Data,
        cast(valor as int) as Concessao_de_Credito
    from concessao_de_credito
)

-- retorno dos dados transformados
select * from stg_bacen__concessao_de_credito
