-- models/marts/fato_rendimento_atividade.sql

with stg_ibge__rendimento_mensal_atividade as (
    select * from {{ ref('stg_ibge__rendimento_mensal_atividade') }}
),

-- transformação dos dados

rendimento_atividade as (
    SELECT 
        Data,
        SUM(CASE WHEN Trabalho_Principal = 'Agricultura, pecuária, produção florestal, pesca e aquicultura' THEN Rendimento_Mensal_Atividade ELSE 0 END) AS 'Agricultura',
        SUM(CASE WHEN Trabalho_Principal = 'Indústria geral' THEN Rendimento_Mensal_Atividade ELSE 0 END) AS 'Indústria',
        SUM(CASE WHEN Trabalho_Principal = 'Construção' THEN Rendimento_Mensal_Atividade ELSE 0 END) AS 'Construção',
        SUM(CASE WHEN Trabalho_Principal = 'Comércio, reparação de veículos automotores e motocicletas' THEN Rendimento_Mensal_Atividade ELSE 0 END) AS 'Comércio',
        SUM(CASE WHEN Trabalho_Principal = 'Transporte, armazenagem e correio' THEN Rendimento_Mensal_Atividade ELSE 0 END) AS 'Transporte',
        SUM(CASE WHEN Trabalho_Principal = 'Alojamento e alimentação' THEN Rendimento_Mensal_Atividade ELSE 0 END) AS 'Alojamento',
        SUM(CASE WHEN Trabalho_Principal = 'Informação, comunicação e atividades financeiras, imobiliárias, profissionais e administrativas' THEN Rendimento_Mensal_Atividade ELSE 0 END) AS 'Informação, Comunicação, Financeira, Administrativas',
        SUM(CASE WHEN Trabalho_Principal = 'Administração pública, defesa, seguridade social, educação, saúde humana e serviços sociais' THEN Rendimento_Mensal_Atividade ELSE 0 END) AS 'Administração Pública, Saúde, Educação',
        SUM(CASE WHEN Trabalho_Principal = 'Outros serviços' THEN Rendimento_Mensal_Atividade ELSE 0 END) AS 'Outros Serviços',
        SUM(CASE WHEN Trabalho_Principal = 'Serviços domésticos' THEN Rendimento_Mensal_Atividade ELSE 0 END) AS 'Serviços Domésticos',
        SUM(CASE WHEN Trabalho_Principal = 'Total' THEN Rendimento_Mensal_Atividade ELSE 0 END) AS 'Total'
    FROM stg_ibge__rendimento_mensal_atividade
    GROUP BY Data
)

-- retorno dos dados
select * from rendimento_atividade