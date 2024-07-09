-- models/staging/stg_Concessao_de_Credito_PF.sql

with Concessao_de_Credito_PF as (
    select * from {{ source('dbo', 'Concessao_de_Credito_PF') }}
),

-- transformação dos dados
stg_Concessao_de_Credito_PF as (
    select
        CONVERT(DATE, data, 103) AS Data,
        cast(valor as int) as Concessao_de_Credito_PF
    from Concessao_de_Credito_PF
)

-- retorno dos dados transformados
select * from stg_Concessao_de_Credito_PF
