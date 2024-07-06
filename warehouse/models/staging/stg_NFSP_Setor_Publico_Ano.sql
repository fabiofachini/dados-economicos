-- models/staging/stg_NFSP_Setor_Publico_Ano.sql

with NFSP_Setor_Publico_Ano as (
    select * from {{ source('dbo', 'NFSP_Setor_Publico_Ano') }}
),

-- transformação dos dados
stg_NFSP_Setor_Publico_Ano as (
    select
        cast(data as date) as date,
        cast(valor as numeric) as value
    from NFSP_Setor_Publico_Ano
)

-- retorno dos dados transformados
select * from stg_NFSP_Setor_Publico_Ano
