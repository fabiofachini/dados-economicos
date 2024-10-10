-- models/marts/fato_instrucao.sql

with stg_ibge__nivel_de_instrucao as (
    select * from {{ ref('stg_ibge__nivel_de_instrucao') }}
),

-- transformação dos dados
instrucao as (
    SELECT 
        Data,
        SUM(CASE WHEN Nivel_de_Instrucao = 'Sem instrução e fundamental incompleto ou equivalente' THEN Mil_Pessoas ELSE 0 END) AS 'Sem Instrução',
        SUM(CASE WHEN Nivel_de_Instrucao = 'Fundamental completo e médio incompleto ou equivalente' THEN Mil_Pessoas ELSE 0 END) AS 'Fundamental',
        SUM(CASE WHEN Nivel_de_Instrucao = 'Médio completo ou equivalente e superior incompleto' THEN Mil_Pessoas ELSE 0 END) AS 'Médio',
        SUM(CASE WHEN Nivel_de_Instrucao = 'Superior completo' THEN Mil_Pessoas ELSE 0 END) AS 'Superior'
    FROM stg_ibge__nivel_de_instrucao 
    WHERE Sexo = 'Total'
    GROUP BY Data
)

-- retorno dos dados
select * from instrucao