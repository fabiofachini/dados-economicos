-- models/staging/stg_Concessao_de_Credito_PJ.sql

with Concessao_de_Credito_PJ as (
    select * from {{ source('dbo', 'Concessao_de_Credito_PJ') }}
),

-- transformação dos dados
stg_Concessao_de_Credito_PJ as (
    select
        cast(data as date) as date,
        cast(valor as numeric) as value
    from Concessao_de_Credito_PJ
)

-- retorno dos dados transformados
select * from stg_Concessao_de_Credito_PJ
