-- models/staging/stg_ibge__rendimento_mensal_atividade.sql

with rendimento_mensal_atividade as (
    select * from {{ source('dbo', 'rendimento_mensal_atividade') }}
),

-- transformação dos dados
stg_ibge__rendimento_mensal_atividade as (
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
    from rendimento_mensal_atividade
)
-- retorno dos dados transformados
select * from stg_ibge__rendimento_mensal_atividade
