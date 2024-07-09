-- models/staging/stg_Rendimento_Classe_Social.sql

with Rendimento_Classe_Social as (
    select * from {{ source('dbo', 'Rendimento_Classe_Social') }}
),

-- transformação dos dados
stg_Rendimento_Classe_Social as (
    select
        CONVERT(DATE, 
            [Ano (Código)] + '-01-01') AS Data,
        TRY_CAST(
        CASE 
            WHEN [Valor] = '...' THEN NULL
            ELSE [Valor]
        END AS INT) AS Rendimento_Classe_Social,
        [Classes de percentual das pessoas em ordem crescente de rendimento domiciliar per capita] AS Classes_Sociais_Percentil
    from Rendimento_Classe_Social
)

-- retorno dos dados transformados
select * from stg_Rendimento_Classe_Social
