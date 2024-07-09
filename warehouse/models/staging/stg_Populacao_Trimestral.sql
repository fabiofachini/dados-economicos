-- models/staging/stg_Populacao_Trimestral.sql

with Populacao_Trimestral as (
    select * from {{ source('dbo', 'Populacao_Trimestral') }}
),

-- transformação dos dados
stg_Populacao_Trimestral as (
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
    from Populacao_Trimestral
)

-- retorno dos dados transformados
select * from stg_Populacao_Trimestral
