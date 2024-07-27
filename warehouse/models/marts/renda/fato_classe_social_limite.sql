with int_classe_social_joined as (
    select * from {{ ref('stg_ibge__limites_classe_social') }}
),

populacao_classe_social as (
    SELECT 
        Data,
        SUM(CASE WHEN Classes_Sociais_Percentil = 'Até o P5' THEN Limites_Classe_Social ELSE 0 END) AS [Até o P5],
        SUM(CASE WHEN Classes_Sociais_Percentil = 'Maior que o P5 até o P10' THEN Limites_Classe_Social ELSE 0 END) AS [Maior que o P5 até o P10],
        SUM(CASE WHEN Classes_Sociais_Percentil = 'Maior que o P10 até o P20' THEN Limites_Classe_Social ELSE 0 END) AS [Maior que o P10 até o P20],
        SUM(CASE WHEN Classes_Sociais_Percentil = 'Maior que o P20 até o P30' THEN Limites_Classe_Social ELSE 0 END) AS [Maior que o P20 até o P30],
        SUM(CASE WHEN Classes_Sociais_Percentil = 'Maior que o P30 até o P40' THEN Limites_Classe_Social ELSE 0 END) AS [Maior que o P30 até o P40],
        SUM(CASE WHEN Classes_Sociais_Percentil = 'Maior que o P40 até o P50' THEN Limites_Classe_Social ELSE 0 END) AS [Maior que o P40 até o P50],
        SUM(CASE WHEN Classes_Sociais_Percentil = 'Maior que o P50 até o P60' THEN Limites_Classe_Social ELSE 0 END) AS [Maior que o P50 até o P60],
        SUM(CASE WHEN Classes_Sociais_Percentil = 'Maior que o P60 até o P70' THEN Limites_Classe_Social ELSE 0 END) AS [Maior que o P60 até o P70],
        SUM(CASE WHEN Classes_Sociais_Percentil = 'Maior que o P70 até o P80' THEN Limites_Classe_Social ELSE 0 END) AS [Maior que o P70 até o P80],
        SUM(CASE WHEN Classes_Sociais_Percentil = 'Maior que o P80 até o P90' THEN Limites_Classe_Social ELSE 0 END) AS [Maior que o P80 até o P90],
        SUM(CASE WHEN Classes_Sociais_Percentil = 'Maior que o P90 até o P95' THEN Limites_Classe_Social ELSE 0 END) AS [Maior que o P90 até o P95],
        SUM(CASE WHEN Classes_Sociais_Percentil = 'Maior que o P95 até o P99' THEN Limites_Classe_Social ELSE 0 END) AS [Maior que o P95 até o P99],
        SUM(CASE WHEN Classes_Sociais_Percentil = 'Maior que o P99' THEN Limites_Classe_Social ELSE 0 END) AS [Maior que o P99]
    FROM int_classe_social_joined
    GROUP BY Data
)

select * from populacao_classe_social