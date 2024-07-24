-- models/staging/stg_ibge__pib.sql

with pib as (
    select * from {{ source('dbo', 'pib') }}
),

-- transformação dos dados
stg_ibge__pib AS (
    SELECT
    CASE 
        WHEN SUBSTRING(CAST([Trimestre (Código)] AS VARCHAR(6)), 5, 2) = '01' THEN CONVERT(DATE, LEFT(CAST([Trimestre (Código)] AS VARCHAR(6)), 4) + '-03-01')
        WHEN SUBSTRING(CAST([Trimestre (Código)] AS VARCHAR(6)), 5, 2) = '02' THEN CONVERT(DATE, LEFT(CAST([Trimestre (Código)] AS VARCHAR(6)), 4) + '-06-01')
        WHEN SUBSTRING(CAST([Trimestre (Código)] AS VARCHAR(6)), 5, 2) = '03' THEN CONVERT(DATE, LEFT(CAST([Trimestre (Código)] AS VARCHAR(6)), 4) + '-09-01')
        WHEN SUBSTRING(CAST([Trimestre (Código)] AS VARCHAR(6)), 5, 2) = '04' THEN CONVERT(DATE, LEFT(CAST([Trimestre (Código)] AS VARCHAR(6)), 4) + '-12-01')
        ELSE NULL
    END AS Data,
    CAST(Valor AS NUMERIC(10,2)) AS PIB
    FROM pib)

-- retorno dos dados transformados
select * from stg_ibge__pib
