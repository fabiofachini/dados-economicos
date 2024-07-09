-- models/staging/stg_IPCA_depois_2019.sql

with IPCA_depois_2019 as (
    select * from {{ source('dbo', 'IPCA_depois_2019') }}
),

-- transformação dos dados
stg_IPCA_depois_2019 as (
    select
        CONVERT(DATE, 
            SUBSTRING(CAST([Mês (Código)] AS VARCHAR(6)), 1, 4) + '-' + 
            SUBSTRING(CAST([Mês (Código)] AS VARCHAR(6)), 5, 2) + '-01') AS Data,
        TRY_CAST(
        CASE 
            WHEN [Valor] = '...' THEN NULL
            ELSE [Valor]
        END AS NUMERIC(10,2)
    ) AS IPCA_depois_2019,
    Variável
    from IPCA_depois_2019
)

-- retorno dos dados transformados
select * from stg_IPCA_depois_2019
