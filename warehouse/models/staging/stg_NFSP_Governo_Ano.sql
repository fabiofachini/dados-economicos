-- models/staging/stg_NFSP_Governo_Ano.sql

with NFSP_Governo_Ano as (
    select * from {{ source('dbo', 'NFSP_Governo_Ano') }}
),

-- transformação dos dados
stg_NFSP_Governo_Ano as (
    select
        CONVERT(DATE, data, 103) AS Data,
        cast(valor as numeric(10,2)) as NFSP_Governo_Ano
    from NFSP_Governo_Ano
)

-- retorno dos dados transformados
select * from stg_NFSP_Governo_Ano
