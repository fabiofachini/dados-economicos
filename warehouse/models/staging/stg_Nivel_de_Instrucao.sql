-- models/staging/stg_Nivel_de_Instrucao.sql

with Nivel_de_Instrucao as (
    select * from {{ source('dbo', 'Nivel_de_Instrucao') }}
),

-- transformação dos dados
stg_Nivel_de_Instrucao as (
    select
        CONVERT(DATE, 
            [Ano (Código)] + '-01-01') AS Data,
        TRY_CAST(
        CASE 
            WHEN [Valor] = '...' THEN NULL
            ELSE [Valor]
        END AS INT) AS Mil_Pessoas,
        Sexo,
        [Nível de instrução] AS Nivel_de_Instrucao
    from Nivel_de_Instrucao
)

-- retorno dos dados transformados
select * from stg_Nivel_de_Instrucao
