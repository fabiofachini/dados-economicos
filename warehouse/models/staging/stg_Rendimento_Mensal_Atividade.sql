-- models/staging/stg_Rendimento_Mensal_Atividade.sql

with Rendimento_Mensal_Atividade as (
    select * from {{ source('dbo', 'Rendimento_Mensal_Atividade') }}
),

-- transformação dos dados
stg_Rendimento_Mensal_Atividade as (
    select
        CONVERT(DATE, 
            SUBSTRING(CAST([Trimestre Móvel (Código)] AS VARCHAR(6)), 1, 4) + '-' + 
            SUBSTRING(CAST([Trimestre Móvel (Código)] AS VARCHAR(6)), 5, 2) + '-01') AS Data,
        TRY_CAST(
        CASE 
            WHEN [Valor] = '...' THEN NULL
            ELSE [Valor]
        END AS INT
    ) AS Rendimento_Mensal_Atividade,
    [Grupamento de atividade no trabalho principal] AS Trabalho_Principal
    from Rendimento_Mensal_Atividade
)
-- retorno dos dados transformados
select * from stg_Rendimento_Mensal_Atividade
