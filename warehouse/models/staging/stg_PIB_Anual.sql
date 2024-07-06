-- models/staging/stg_PIB_Anual.sql

with PIB_Anual as (
    select * from {{ source('dbo', 'PIB_Anual') }}
),

-- transformação dos dados
stg_PIB_Anual as (
    select
        cast(data as date) as date,
        cast(valor as numeric) as value
    from PIB_Anual
)

-- retorno dos dados transformados
select * from stg_PIB_Anual
