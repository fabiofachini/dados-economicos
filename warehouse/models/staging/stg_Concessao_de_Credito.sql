-- models/staging/stg_Concessao_de_Credito.sql

with Concessao_de_Credito as (
    select * from {{ source('dbo', 'Concessao_de_Credito') }}
),

-- transformação dos dados
stg_Concessao_de_Credito as (
    select
        cast(data as date) as date,
        cast(valor as numeric) as value
    from Concessao_de_Credito
)

-- retorno dos dados transformados
select * from stg_Concessao_de_Credito
