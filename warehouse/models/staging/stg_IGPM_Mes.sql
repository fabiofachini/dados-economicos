-- models/staging/stg_IGPM_Mes.sql

with IGPM_Mes as (
    select * from {{ source('dbo', 'IGPM_Mes') }}
),

-- transformação dos dados
stg_IGPM_Mes as (
    select
        cast(data as date) as date,
        cast(valor as numeric) as value
    from IGPM_Mes
)

-- retorno dos dados transformados
select * from stg_IGPM_Mes
