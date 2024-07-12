-- models/staging/stg_ibge__rendimento_classe_social.sql

with rendimento_classe_social as (
    select * from {{ source('dbo', 'rendimento_classe_social') }}
),

-- transformação dos dados
stg_ibge__rendimento_classe_social as (
    select
        CONVERT(DATE, 
            [Ano (Código)] + '-01-01') AS Data,
        TRY_CAST(
        CASE 
            WHEN [Valor] = '...' THEN NULL
            ELSE [Valor]
        END AS INT) AS Rendimento_Classe_Social,
        [Classes de percentual das pessoas em ordem crescente de rendimento domiciliar per capita] AS Classes_Sociais_Percentil
    from rendimento_classe_social
)

-- retorno dos dados transformados
select * from stg_ibge__rendimento_classe_social
