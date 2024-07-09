-- models/staging/stg_IGPM_Mes.sql

with IGPM_Mes as (
    select * from {{ source('dbo', 'IGPM_Mes') }}
),

-- transformação dos dados
stg_IGPM_Mes as (
    select
        CONVERT(DATE, data, 103) AS Data,
        cast(valor as numeric(10,2)) as IGPM_Mes
    from IGPM_Mes
)

-- retorno dos dados transformados
select * from stg_IGPM_Mes
