-- models/staging/stg_Rendimento_Mensal_Posicao.sql

with Rendimento_Mensal_Posicao as (
    select * from {{ source('dbo', 'Rendimento_Mensal_Posicao') }}
),

-- transformação dos dados
stg_Rendimento_Mensal_Posicao as (
    select
        CONVERT(DATE, 
            SUBSTRING(CAST([Trimestre Móvel (Código)] AS VARCHAR(6)), 1, 4) + '-' + 
            SUBSTRING(CAST([Trimestre Móvel (Código)] AS VARCHAR(6)), 5, 2) + '-01') AS Data,
        TRY_CAST(
        CASE 
            WHEN [Valor] = '-' THEN NULL
            ELSE [Valor]
        END AS INT
    ) AS Rendimento_Mensal_Posicao,
    [Posição na ocupação e categoria do emprego no trabalho principal] AS Posicao_Trabalho
    from Rendimento_Mensal_Posicao
)
-- retorno dos dados transformados
select * from stg_Rendimento_Mensal_Posicao
