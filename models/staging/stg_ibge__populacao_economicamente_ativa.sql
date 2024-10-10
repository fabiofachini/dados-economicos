-- models/staging/stg_ibge__populacao_economicamente_ativa.sql

with populacao_economicamente_ativa as (
    select * from {{ source('dbo', 'populacao_economicamente_ativa') }}
),

-- transformação dos dados
stg_ibge__populacao_economicamente_ativa as (
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
    from populacao_economicamente_ativa
)

-- retorno dos dados transformados
select * from stg_ibge__populacao_economicamente_ativa
