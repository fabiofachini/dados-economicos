-- models/staging/stg_Divida_Liquida_PIB_Setor_Publico.sql

with Divida_Liquida_PIB_Setor_Publico as (
    select * from {{ source('dbo', 'Divida_Liquida_PIB_Setor_Publico') }}
),

-- transformação dos dados
stg_Divida_Liquida_PIB_Setor_Publico as (
    select
        CONVERT(DATE, data, 103) AS Data,
        cast(valor as numeric(10,2)) as Divida_Liquida_PIB_Setor_Publico
    from Divida_Liquida_PIB_Setor_Publico
)

-- retorno dos dados transformados
select * from stg_Divida_Liquida_PIB_Setor_Publico
