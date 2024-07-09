-- models/staging/stg_Indice_de_Gini.sql

with Indice_de_Gini as (
    select * from {{ source('dbo', 'Indice_de_Gini') }}
),

-- transformação dos dados
stg_Indice_de_Gini as (
    select
        CONVERT(DATE, 
            [Ano (Código)] + '-01-01') AS Data,
        TRY_CAST(
        CASE 
            WHEN [Valor] = '...' THEN NULL
            ELSE [Valor]
        END AS NUMERIC(10,4)
    ) AS Indice_de_Gini
    from Indice_de_Gini
)

-- retorno dos dados transformados
select * from stg_Indice_de_Gini
