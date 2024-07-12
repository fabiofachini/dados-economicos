-- models/staging/stg_ibge__massa_salarial_por_classe_social.sql

with massa_salarial_por_classe_social as (
    select * from {{ source('dbo', 'massa_salarial_por_classe_social') }}
),

-- transformação dos dados
stg_ibge__massa_salarial_por_classe_social as (
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
    from massa_salarial_por_classe_social
)  
-- retorno dos dados transformados
select * from stg_ibge__massa_salarial_por_classe_social
