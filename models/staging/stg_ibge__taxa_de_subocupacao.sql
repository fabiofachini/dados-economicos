-- models/staging/stg_ibge__taxa_de_subocupacao.sql

with taxa_de_subocupacao as (
    select * from {{ source('dbo', 'taxa_de_subocupacao') }}
),

-- transformação dos dados
stg_ibge__taxa_de_subocupacao as (
    select
        CONVERT(DATE, 
            SUBSTRING(CAST([Trimestre Móvel (Código)] AS VARCHAR(6)), 1, 4) + '-' + 
            SUBSTRING(CAST([Trimestre Móvel (Código)] AS VARCHAR(6)), 5, 2) + '-01') AS Data,
        TRY_CAST(
        CASE 
            WHEN [Valor] = '...' THEN NULL
            ELSE [Valor]
        END AS NUMERIC(10,1)
    ) AS Taxa_de_Subocupacao
    from taxa_de_subocupacao
)

-- retorno dos dados transformados
select * from stg_ibge__taxa_de_subocupacao
