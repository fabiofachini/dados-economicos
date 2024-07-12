-- models/staging/stg_ibge__limites_classe_social.sql

with limites_classe_social as (
    select * from {{ source('dbo', 'limites_classe_social') }}
),

-- transformação dos dados
stg_ibge__limites_classe_social as (
    select
        CONVERT(DATE, 
            [Ano (Código)] + '-01-01') AS Data,
        TRY_CAST(
        CASE 
            WHEN [Valor] = '...' THEN NULL
            ELSE [Valor]
        END AS NUMERIC(10,4)
    ) AS Limites_Classe_Social,
        [Classes de percentual das pessoas em ordem crescente de rendimento domiciliar per capita] AS Classes_Sociais_Percentil
    from limites_classe_social
)  

-- retorno dos dados transformados
select * from stg_ibge__limites_classe_social
