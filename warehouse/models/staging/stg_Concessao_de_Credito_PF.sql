-- models/staging/stg_Concessao_de_Credito_PF.sql

with Concessao_de_Credito_PF as (
    select * from {{ source('dbo', 'Concessao_de_Credito_PF') }}
),

-- transformação dos dados
stg_Concessao_de_Credito_PF as (
    select
        cast(data as date) as date,
        cast(valor as numeric) as value
    from Concessao_de_Credito_PF
)

-- retorno dos dados transformados
select * from stg_Concessao_de_Credito_PF
