-- models/staging/stg_Divida_Liquida_PIB_Setor_Publico.sql

with Divida_Liquida_PIB_Setor_Publico as (
    select * from {{ source('dbo', 'Divida_Liquida_PIB_Setor_Publico') }}
),

-- transformação dos dados
stg_Divida_Liquida_PIB_Setor_Publico as (
    select
        cast(data as date) as date,
        cast(valor as numeric) as value
    from Divida_Liquida_PIB_Setor_Publico
)

-- retorno dos dados transformados
select * from stg_Divida_Liquida_PIB_Setor_Publico
