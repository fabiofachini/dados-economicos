-- models/staging/stg_ibge__pib_variacao_trimestral.sql

with pib_variacao_trimestral as (
    select * from {{ source('dbo', 'pib_variacao_trimestral') }}
),

-- transformação dos dados
stg_ibge__pib_variacao_trimestral AS (
    SELECT
    CASE 
        WHEN SUBSTRING(CAST([Trimestre (Código)] AS VARCHAR(6)), 5, 2) = '01' THEN CONVERT(DATE, LEFT(CAST([Trimestre (Código)] AS VARCHAR(6)), 4) + '-03-01')
        WHEN SUBSTRING(CAST([Trimestre (Código)] AS VARCHAR(6)), 5, 2) = '02' THEN CONVERT(DATE, LEFT(CAST([Trimestre (Código)] AS VARCHAR(6)), 4) + '-06-01')
        WHEN SUBSTRING(CAST([Trimestre (Código)] AS VARCHAR(6)), 5, 2) = '03' THEN CONVERT(DATE, LEFT(CAST([Trimestre (Código)] AS VARCHAR(6)), 4) + '-09-01')
        WHEN SUBSTRING(CAST([Trimestre (Código)] AS VARCHAR(6)), 5, 2) = '04' THEN CONVERT(DATE, LEFT(CAST([Trimestre (Código)] AS VARCHAR(6)), 4) + '-12-01')
        ELSE NULL
    END AS Data,
    TRY_CAST(
        CASE 
            WHEN [Valor] = '...' THEN NULL
            ELSE [Valor]
        END AS NUMERIC(10,2)
    ) AS PIB_Variacao_Trimestral
    FROM pib_variacao_trimestral)

-- retorno dos dados transformados
select * from stg_ibge__pib_variacao_trimestral
