with int_classe_social_massa as (
    select * from {{ ref('stg_ibge__massa_salarial_por_classe_social') }}
),

massa_classe_social as (
    SELECT 
        Data,
        SUM(CASE WHEN Classes_Sociais_Percentil = 'Até o P5' THEN Massa_Salarial_por_Classe_Social ELSE 0 END) AS [Até o P5],
        SUM(CASE WHEN Classes_Sociais_Percentil = 'Maior que o P5 até o P10' THEN Massa_Salarial_por_Classe_Social ELSE 0 END) AS [P5 até o P10],
        SUM(CASE WHEN Classes_Sociais_Percentil = 'Maior que o P10 até o P20' THEN Massa_Salarial_por_Classe_Social ELSE 0 END) AS [P10 até o P20],
        SUM(CASE WHEN Classes_Sociais_Percentil = 'Maior que o P20 até o P30' THEN Massa_Salarial_por_Classe_Social ELSE 0 END) AS [P20 até o P30],
        SUM(CASE WHEN Classes_Sociais_Percentil = 'Maior que o P30 até o P40' THEN Massa_Salarial_por_Classe_Social ELSE 0 END) AS [P30 até o P40],
        SUM(CASE WHEN Classes_Sociais_Percentil = 'Maior que o P40 até o P50' THEN Massa_Salarial_por_Classe_Social ELSE 0 END) AS [P40 até o P50],
        SUM(CASE WHEN Classes_Sociais_Percentil = 'Maior que o P50 até o P60' THEN Massa_Salarial_por_Classe_Social ELSE 0 END) AS [P50 até o P60],
        SUM(CASE WHEN Classes_Sociais_Percentil = 'Maior que o P60 até o P70' THEN Massa_Salarial_por_Classe_Social ELSE 0 END) AS [P60 até o P70],
        SUM(CASE WHEN Classes_Sociais_Percentil = 'Maior que o P70 até o P80' THEN Massa_Salarial_por_Classe_Social ELSE 0 END) AS [P70 até o P80],
        SUM(CASE WHEN Classes_Sociais_Percentil = 'Maior que o P80 até o P90' THEN Massa_Salarial_por_Classe_Social ELSE 0 END) AS [P80 até o P90],
        SUM(CASE WHEN Classes_Sociais_Percentil = 'Maior que o P90 até o P95' THEN Massa_Salarial_por_Classe_Social ELSE 0 END) AS [P90 até o P95],
        SUM(CASE WHEN Classes_Sociais_Percentil = 'Maior que o P95 até o P99' THEN Massa_Salarial_por_Classe_Social ELSE 0 END) AS [P95 até o P99],
        SUM(CASE WHEN Classes_Sociais_Percentil = 'Maior que o P99' THEN Massa_Salarial_por_Classe_Social ELSE 0 END) AS [Maior que o P99]
    FROM int_classe_social_massa
    GROUP BY Data
)

select * from massa_classe_social