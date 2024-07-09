-- models/staging/stg_Populacao_Economicamente_Ativa.sql

with Populacao_Economicamente_Ativa as (
    select * from {{ source('dbo', 'Populacao_Economicamente_Ativa') }}
),

-- transformação dos dados
stg_Populacao_Economicamente_Ativa as (
    select
        CONVERT(DATE, 
            SUBSTRING(CAST([Trimestre Móvel (Código)] AS VARCHAR(6)), 1, 4) + '-' + 
            SUBSTRING(CAST([Trimestre Móvel (Código)] AS VARCHAR(6)), 5, 2) + '-01') AS Data,
        TRY_CAST(
        CASE 
            WHEN [Valor] = '...' THEN NULL
            ELSE [Valor]
        END AS INT
    ) AS Populacao_Economicamente_Ativa,
    [Condição em relação à força de trabalho e condição de ocupação] AS Condição_Forca_Trabalho
    from Populacao_Economicamente_Ativa
)

-- retorno dos dados transformados
select * from stg_Populacao_Economicamente_Ativa
