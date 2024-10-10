-- models/staging/stg_bacen__igpm_mes.sql

with igpm_mes as (
    select * from {{ source('dbo', 'igpm_mes') }}
),

-- transformação dos dados
stg_bacen__igpm_mes as (
    select
        CONVERT(DATE, data, 103) AS Data,
        cast(valor as numeric(10,2)) as IGPM_Mes
    from igpm_mes
)

-- retorno dos dados transformados
select * from stg_bacen__igpm_mes
