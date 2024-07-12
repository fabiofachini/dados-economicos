-- models/staging/stg_bacen__divida_liquida_pib_setor_publico.sql

with divida_liquida_pib_setor_publico as (
    select * from {{ source('dbo', 'divida_liquida_pib_setor_publico') }}
),

-- transformação dos dados
stg_bacen__divida_liquida_pib_setor_publico as (
    select
        CONVERT(DATE, data, 103) AS Data,
        cast(valor as numeric(10,2)) as Divida_Liquida_PIB_Setor_Publico
    from divida_liquida_pib_setor_publico
)

-- retorno dos dados transformados
select * from stg_bacen__divida_liquida_pib_setor_publico
