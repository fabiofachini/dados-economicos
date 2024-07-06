-- models/staging/stg_PIB_Variacao_Trimestral.sql

with PIB_Variacao_Trimestral as (
    select * from {{ source('dbo', 'PIB_Variacao_Trimestral') }}
),

-- transformação dos dados
stg_PIB_Variacao_Trimestral as (
    select
        cast(data as date) as date,
        cast(valor as numeric) as value
    from PIB_Variacao_Trimestral
)

-- retorno dos dados transformados
select * from stg_PIB_Variacao_Trimestral
