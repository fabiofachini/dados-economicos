-- models/staging/stg_ibge__pib_anual.sql

with pib_anual as (
    select * from {{ source('dbo', 'pib_anual') }}
),

-- transformação dos dados
stg_ibge__pib_anual as (
    select
        CONVERT(DATE, 
            [Ano (Código)] + '-01-01') AS Data,
        TRY_CAST(
        CASE 
            WHEN [Valor] = '...' THEN NULL
            ELSE [Valor]
        END AS NUMERIC(10,2)) AS PIB_Anual,
        Variável
    from pib_anual
)

-- retorno dos dados transformados
select * from stg_ibge__pib_anual
