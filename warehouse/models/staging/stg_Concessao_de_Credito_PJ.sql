-- models/staging/stg_Concessao_de_Credito_PJ.sql

with Concessao_de_Credito_PJ as (
    select * from {{ source('dbo', 'Concessao_de_Credito_PJ') }}
),

-- transformação dos dados
stg_Concessao_de_Credito_PJ as (
    select
        CONVERT(DATE, data, 103) AS Data,
        cast(valor as int) as Concessao_de_Credito_PJ
    from Concessao_de_Credito_PJ
)

-- retorno dos dados transformados
select * from stg_Concessao_de_Credito_PJ
