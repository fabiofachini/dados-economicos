-- models/staging/stg_NFSP_Setor_Publico_Ano.sql

with NFSP_Setor_Publico_Ano as (
    select * from {{ source('dbo', 'NFSP_Setor_Publico_Ano') }}
),

-- transformação dos dados
stg_NFSP_Setor_Publico_Ano as (
    select
        CONVERT(DATE, data, 103) AS Data,
        cast(valor as numeric(10,2)) as NFSP_Setor_Publico_Ano
    from NFSP_Setor_Publico_Ano
)

-- retorno dos dados transformados
select * from stg_NFSP_Setor_Publico_Ano
