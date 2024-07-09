-- models/staging/stg_Concessao_de_Credito.sql

with Concessao_de_Credito as (
    select * from {{ source('dbo', 'Concessao_de_Credito') }}
),

-- transformação dos dados
stg_Concessao_de_Credito as (
    select
        CONVERT(DATE, data, 103) AS Data,
        cast(valor as int) as Concessao_de_Credito
    from Concessao_de_Credito
)

-- retorno dos dados transformados
select * from stg_Concessao_de_Credito
