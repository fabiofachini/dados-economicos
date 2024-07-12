-- models/staging/stg_bacen__nfsp_pib_setor_publico_12m.sql

with nfsp_pib_setor_publico_12m as (
    select * from {{ source('dbo', 'nfsp_pib_setor_publico_12m') }}
),

-- transformação dos dados
stg_bacen__nfsp_pib_setor_publico_12m as (
    select
        CONVERT(DATE, data, 103) AS Data,
        cast(valor as numeric(10,2)) as NFSP_PIB_Setor_Publico_12m
    from nfsp_pib_setor_publico_12m
)

-- retorno dos dados transformados
select * from stg_bacen__nfsp_pib_setor_publico_12m
