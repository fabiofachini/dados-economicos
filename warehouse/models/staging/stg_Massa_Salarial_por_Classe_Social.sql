-- models/staging/stg_Massa_Salarial_por_Classe_Social.sql

with Massa_Salarial_por_Classe_Social as (
    select * from {{ source('dbo', 'Massa_Salarial_por_Classe_Social') }}
),

-- transformação dos dados
stg_Massa_Salarial_por_Classe_Social as (
    select
        CONVERT(DATE, 
            [Ano (Código)] + '-01-01') AS Data,
        TRY_CAST(
        CASE 
            WHEN [Valor] = '...' THEN NULL
            ELSE [Valor]
        END AS NUMERIC(10,4)
    ) AS Massa_Salarial_por_Classe_Social,
        [Classes de percentual das pessoas em ordem crescente de rendimento domiciliar per capita] AS Classes_Sociais_Percentil
    from Massa_Salarial_por_Classe_Social
)  
-- retorno dos dados transformados
select * from stg_Massa_Salarial_por_Classe_Social
