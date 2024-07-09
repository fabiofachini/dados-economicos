-- models/staging/stg_Rendimento_Trabalho_Principal.sql

with Rendimento_Trabalho_Principal as (
    select * from {{ source('dbo', 'Rendimento_Trabalho_Principal') }}
),

-- transformação dos dados
stg_Rendimento_Trabalho_Principal as (
    select
        CONVERT(DATE, 
            SUBSTRING(CAST([Trimestre Móvel (Código)] AS VARCHAR(6)), 1, 4) + '-' + 
            SUBSTRING(CAST([Trimestre Móvel (Código)] AS VARCHAR(6)), 5, 2) + '-01') AS Data,
        TRY_CAST(
        CASE 
            WHEN [Valor] = '...' THEN NULL
            ELSE [Valor]
        END AS INT
    ) AS Rendimento_Trabalho_Principal
    from Rendimento_Trabalho_Principal
)

-- retorno dos dados transformados
select * from stg_Rendimento_Trabalho_Principal
