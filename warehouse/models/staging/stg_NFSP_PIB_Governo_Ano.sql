-- models/staging/stg_NFSP_PIB_Governo_Ano.sql

with NFSP_PIB_Governo_Ano as (
    select * from {{ source('dbo', 'NFSP_PIB_Governo_Ano') }}
),

-- transformação dos dados
stg_NFSP_PIB_Governo_Ano as (
    select
        cast(data as date) as date,
        cast(valor as numeric) as value
    from NFSP_PIB_Governo_Ano
)

-- retorno dos dados transformados
select * from stg_NFSP_PIB_Governo_Ano
