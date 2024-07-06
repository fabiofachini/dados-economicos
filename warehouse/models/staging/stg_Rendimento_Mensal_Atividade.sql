-- models/staging/stg_Rendimento_Mensal_Atividade.sql

with Rendimento_Mensal_Atividade as (
    select * from {{ source('dbo', 'Rendimento_Mensal_Atividade') }}
),

-- transformação dos dados
stg_Rendimento_Mensal_Atividade as (
    select
        cast(data as date) as date,
        cast(valor as numeric) as value
    from Rendimento_Mensal_Atividade
)

-- retorno dos dados transformados
select * from stg_Rendimento_Mensal_Atividade
