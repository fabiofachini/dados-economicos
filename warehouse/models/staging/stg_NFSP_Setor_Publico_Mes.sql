-- models/staging/stg_NFSP_Setor_Publico_Mes.sql

with NFSP_Setor_Publico_Mes as (
    select * from {{ source('dbo', 'NFSP_Setor_Publico_Mes') }}
),

-- transformação dos dados
stg_NFSP_Setor_Publico_Mes as (
    select
        CONVERT(DATE, data, 103) AS Data,
        cast(valor as numeric(10,2)) as NFSP_Setor_Publico_Mes
    from NFSP_Setor_Publico_Mes
)

-- retorno dos dados transformados
select * from stg_NFSP_Setor_Publico_Mes
