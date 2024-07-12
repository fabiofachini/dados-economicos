-- models/staging/stg_bacen__nfsp_pib_governo_ano.sql

with nfsp_pib_governo_ano as (
    select * from {{ source('dbo', 'nfsp_pib_governo_ano') }}
),

-- transformação dos dados
stg_bacen__nfsp_pib_governo_ano as (
    select
        CONVERT(DATE, data, 103) AS Data,
        cast(valor as numeric(10,2)) as NFSP_PIB_Governo_Ano
    from nfsp_pib_governo_ano
)

-- retorno dos dados transformados
select * from stg_bacen__nfsp_pib_governo_ano
