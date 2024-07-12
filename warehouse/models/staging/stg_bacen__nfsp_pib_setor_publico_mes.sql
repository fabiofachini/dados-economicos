-- models/staging/stg_bacen__nfsp_pib_setor_publico_mes.sql

with nfsp_pib_setor_publico_mes as (
    select * from {{ source('dbo', 'nfsp_pib_setor_publico_mes') }}
),

-- transformação dos dados
stg_bacen__nfsp_pib_setor_publico_mes as (
    select
        CONVERT(DATE, data, 103) AS Data,
        cast(valor as numeric(10,2)) as NFSP_PIB_Setor_Publico_Mes
    from nfsp_pib_setor_publico_mes
)

-- retorno dos dados transformados
select * from stg_bacen__nfsp_pib_setor_publico_mes
