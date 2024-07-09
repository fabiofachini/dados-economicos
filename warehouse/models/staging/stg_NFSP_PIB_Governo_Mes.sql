-- models/staging/stg_NFSP_PIB_Governo_Mes.sql

with NFSP_PIB_Governo_Mes as (
    select * from {{ source('dbo', 'NFSP_PIB_Governo_Mes') }}
),

-- transformação dos dados
stg_NFSP_PIB_Governo_Mes as (
    select
        CONVERT(DATE, data, 103) AS Data,
        cast(valor as numeric(10,2)) as NFSP_PIB_Governo_Mes
    from NFSP_PIB_Governo_Mes
)

-- retorno dos dados transformados
select * from stg_NFSP_PIB_Governo_Mes
