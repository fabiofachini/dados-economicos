-- models/staging/stg_ibge__populacao_anual.sql

with populacao_anual as (
    select * from {{ source('dbo', 'populacao_anual') }}
),

-- transformação dos dados
stg_ibge__populacao_anual as (
    select
        CONVERT(DATE, 
            [Ano (Código)] + '-01-01') AS Data,
        TRY_CAST(
        CASE 
            WHEN [Valor] = '...' THEN NULL
            ELSE [Valor]
        END AS INT) AS Populacao_Anual
    from populacao_anual
)

-- retorno dos dados transformados
select * from stg_ibge__populacao_anual
