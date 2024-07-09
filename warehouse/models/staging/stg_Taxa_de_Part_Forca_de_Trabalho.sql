-- models/staging/stg_Taxa_de_Part_Forca_de_Trabalho.sql

with Taxa_de_Part_Forca_de_Trabalho as (
    select * from {{ source('dbo', 'Taxa_de_Part_Forca_de_Trabalho') }}
),

-- transformação dos dados
stg_Taxa_de_Part_Forca_de_Trabalho as (
    select
        CONVERT(DATE, 
            SUBSTRING(CAST([Trimestre (Código)] AS VARCHAR(6)), 1, 4) + '-' + 
            SUBSTRING(CAST([Trimestre (Código)] AS VARCHAR(6)), 5, 2) + '-01') AS Data,
        TRY_CAST(
        CASE 
            WHEN [Valor] = '...' THEN NULL
            ELSE [Valor]
        END AS NUMERIC(10,1)
    ) AS Taxa_de_Part_Forca_de_Trabalho,
    from Taxa_de_Part_Forca_de_Trabalho
)
-- retorno dos dados transformados
select * from stg_Taxa_de_Part_Forca_de_Trabalho
