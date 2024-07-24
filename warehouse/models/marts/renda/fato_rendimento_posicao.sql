-- models/marts/fato_rendimento_posicao.sql

with stg_ibge__rendimento_mensal_posicao as (
    select * from {{ ref('stg_ibge__rendimento_mensal_posicao') }}
),

-- transformação dos dados

rendimento_posicao as (
    SELECT 
        Data,
        SUM(CASE WHEN Posicao_Trabalho = 'Conta própria' THEN Rendimento_Mensal_Posicao ELSE 0 END) AS 'Conta própria',
        SUM(CASE WHEN Posicao_Trabalho = 'Empregado' THEN Rendimento_Mensal_Posicao ELSE 0 END) AS 'Empregado',
        SUM(CASE WHEN Posicao_Trabalho = 'Empregado no setor público' THEN Rendimento_Mensal_Posicao ELSE 0 END) AS 'Empregado no setor público',
        SUM(CASE WHEN Posicao_Trabalho = 'Empregador' THEN Rendimento_Mensal_Posicao ELSE 0 END) AS 'Empregador',
        SUM(CASE WHEN Posicao_Trabalho = 'Total' THEN Rendimento_Mensal_Posicao ELSE 0 END) AS 'Total'
    FROM stg_ibge__rendimento_mensal_posicao
    GROUP BY Data
)


-- retorno dos dados
select * from rendimento_posicao