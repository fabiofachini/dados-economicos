-- models/staging/stg_ibge__populacao_classe_social.sql

with populacao_classe_social as (
    select * from {{ source('dbo', 'populacao_classe_social') }}
),

-- transformação dos dados
stg_ibge__populacao_classe_social as (
    select
        CONVERT(DATE, 
            [Ano (Código)] + '-01-01') AS Data,
        TRY_CAST(
        CASE 
            WHEN [Valor] = '...' THEN NULL
            ELSE [Valor]
        END AS NUMERIC(10,1)) AS Populacao_Classe_Social,
        [Classes de percentual das pessoas em ordem crescente de rendimento domiciliar per capita] AS Classes_Sociais_Percentil
    from populacao_classe_social
)

-- retorno dos dados transformados
select * from stg_ibge__populacao_classe_social
