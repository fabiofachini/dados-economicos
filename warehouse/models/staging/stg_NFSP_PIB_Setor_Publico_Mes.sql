-- models/staging/stg_NFSP_PIB_Setor_Publico_Mes.sql

with NFSP_PIB_Setor_Publico_Mes as (
    select * from {{ source('dbo', 'NFSP_PIB_Setor_Publico_Mes') }}
),

-- transformação dos dados
stg_NFSP_PIB_Setor_Publico_Mes as (
    select
        cast(data as date) as date,
        cast(valor as numeric) as value
    from NFSP_PIB_Setor_Publico_Mes
)

-- retorno dos dados transformados
select * from stg_NFSP_PIB_Setor_Publico_Mes
