-- models/staging/stg_ibge__indice_de_gini.sql

with indice_de_gini as (
    select * from {{ source('dbo', 'indice_de_gini') }}
),

-- transformação dos dados
stg_ibge__indice_de_gini as (
    select
        CONVERT(DATE, 
            [Ano (Código)] + '-01-01') AS Data,
        TRY_CAST(
        CASE 
            WHEN [Valor] = '...' THEN NULL
            ELSE [Valor]
        END AS NUMERIC(10,4)
    ) AS Indice_de_Gini
    from indice_de_gini
)

-- retorno dos dados transformados
select * from stg_ibge__indice_de_gini
