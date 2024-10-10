-- models/staging/stg_ibge__nivel_de_instrucao.sql

with nivel_de_instrucao as (
    select * from {{ source('dbo', 'nivel_de_instrucao') }}
),

-- transformação dos dados
stg_ibge__nivel_de_instrucao as (
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
    from nivel_de_instrucao
)

-- retorno dos dados transformados
select * from stg_ibge__nivel_de_instrucao
