-- models/staging/stg_Rendimento_Mensal_Posicao.sql

with Rendimento_Mensal_Posicao as (
    select * from {{ source('dbo', 'Rendimento_Mensal_Posicao') }}
),

-- transformação dos dados
stg_Rendimento_Mensal_Posicao as (
    select
        cast(data as date) as date,
        cast(valor as numeric) as value
    from Rendimento_Mensal_Posicao
)

-- retorno dos dados transformados
select * from stg_Rendimento_Mensal_Posicao
