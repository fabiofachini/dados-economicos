-- models/staging/stg_NFSP_PIB_Governo_Ano.sql

with NFSP_PIB_Governo_Ano as (
    select * from {{ source('dbo', 'NFSP_PIB_Governo_Ano') }}
),

-- transformação dos dados
stg_NFSP_PIB_Governo_Ano as (
    select
        CONVERT(DATE, data, 103) AS Data,
        cast(valor as numeric(10,2)) as NFSP_PIB_Governo_Ano
    from NFSP_PIB_Governo_Ano
)

-- retorno dos dados transformados
select * from stg_NFSP_PIB_Governo_Ano
