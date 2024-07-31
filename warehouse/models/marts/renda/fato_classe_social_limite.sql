with int_classe_social_joined as (
    select * from {{ ref('stg_ibge__limites_classe_social') }}
),

limite_classe_social as (
    SELECT 
        Data,
        SUM(CASE WHEN Classes_Sociais_Percentil = 'P5' THEN Limites_Classe_Social ELSE 0 END) AS [P5],
        SUM(CASE WHEN Classes_Sociais_Percentil = 'P10' THEN Limites_Classe_Social ELSE 0 END) AS [P10],
        SUM(CASE WHEN Classes_Sociais_Percentil = 'P20' THEN Limites_Classe_Social ELSE 0 END) AS [P20],
        SUM(CASE WHEN Classes_Sociais_Percentil = 'P30' THEN Limites_Classe_Social ELSE 0 END) AS [P30],
        SUM(CASE WHEN Classes_Sociais_Percentil = 'P40' THEN Limites_Classe_Social ELSE 0 END) AS [P40],
        SUM(CASE WHEN Classes_Sociais_Percentil = 'P50' THEN Limites_Classe_Social ELSE 0 END) AS [P50],
        SUM(CASE WHEN Classes_Sociais_Percentil = 'P60' THEN Limites_Classe_Social ELSE 0 END) AS [P60],
        SUM(CASE WHEN Classes_Sociais_Percentil = 'P70' THEN Limites_Classe_Social ELSE 0 END) AS [P70],
        SUM(CASE WHEN Classes_Sociais_Percentil = 'P80' THEN Limites_Classe_Social ELSE 0 END) AS [P80],
        SUM(CASE WHEN Classes_Sociais_Percentil = 'P90' THEN Limites_Classe_Social ELSE 0 END) AS [P90],
        SUM(CASE WHEN Classes_Sociais_Percentil = 'P95' THEN Limites_Classe_Social ELSE 0 END) AS [P95],
        SUM(CASE WHEN Classes_Sociais_Percentil = 'P99' THEN Limites_Classe_Social ELSE 0 END) AS [P99]
    FROM int_classe_social_joined
    GROUP BY Data
)

select * from limite_classe_social