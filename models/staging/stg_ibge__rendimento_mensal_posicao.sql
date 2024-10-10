-- models/staging/stg_ibge__rendimento_mensal_posicao.sql

with rendimento_mensal_posicao as (
    select * from {{ source('dbo', 'rendimento_mensal_posicao') }}
),

-- transformação dos dados
stg_ibge__rendimento_mensal_posicao as (
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
    from rendimento_mensal_posicao
)
-- retorno dos dados transformados
select * from stg_ibge__rendimento_mensal_posicao
