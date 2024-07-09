-- models/staging/stg_Populacao_Anual.sql

with Populacao_Anual as (
    select * from {{ source('dbo', 'Populacao_Anual') }}
),

-- transformação dos dados
stg_Populacao_Anual as (
    select
        CONVERT(DATE, 
            [Ano (Código)] + '-01-01') AS Data,
        TRY_CAST(
        CASE 
            WHEN [Valor] = '...' THEN NULL
            ELSE [Valor]
        END AS INT) AS Populacao_Anual,
        Variável
    from Populacao_Anual
)

-- retorno dos dados transformados
select * from stg_Populacao_Anual
