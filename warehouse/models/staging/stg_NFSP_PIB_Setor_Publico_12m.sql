-- models/staging/stg_NFSP_PIB_Setor_Publico_12m.sql

with NFSP_PIB_Setor_Publico_12m as (
    select * from {{ source('dbo', 'NFSP_PIB_Setor_Publico_12m') }}
),

-- transformação dos dados
stg_NFSP_PIB_Setor_Publico_12m as (
    select
        CONVERT(DATE, data, 103) AS Data,
        cast(valor as numeric(10,2)) as NFSP_PIB_Setor_Publico_12m
    from NFSP_PIB_Setor_Publico_12m
)

-- retorno dos dados transformados
select * from stg_NFSP_PIB_Setor_Publico_12m
