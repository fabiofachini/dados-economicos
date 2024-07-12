-- models/staging/stg_ibge__populacao_trimestral.sql

with populacao_trimestral as (
    select * from {{ source('dbo', 'populacao_trimestral') }}
),

-- transformação dos dados
stg_ibge__populacao_trimestral as (
    select
        CONVERT(DATE, 
            SUBSTRING(CAST([Trimestre Móvel (Código)] AS VARCHAR(6)), 1, 4) + '-' + 
            SUBSTRING(CAST([Trimestre Móvel (Código)] AS VARCHAR(6)), 5, 2) + '-01') AS Data,
        TRY_CAST(
        CASE 
            WHEN [Valor] = '...' THEN NULL
            ELSE [Valor]
        END AS INT
    ) AS Populacao_Trimestral
    from populacao_trimestral
)

-- retorno dos dados transformados
select * from stg_ibge__populacao_trimestral
