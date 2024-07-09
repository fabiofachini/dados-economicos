-- models/staging/stg_Limites_Classe_Social.sql

with Limites_Classe_Social as (
    select * from {{ source('dbo', 'Limites_Classe_Social') }}
),

-- transformação dos dados
stg_Limites_Classe_Social as (
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
    from Limites_Classe_Social
)  

-- retorno dos dados transformados
select * from stg_Limites_Classe_Social
