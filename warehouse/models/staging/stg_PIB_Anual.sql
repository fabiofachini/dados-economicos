-- models/staging/stg_PIB_Anual.sql

with PIB_Anual as (
    select * from {{ source('dbo', 'PIB_Anual') }}
),

-- transformação dos dados
stg_PIB_Anual as (
    select
        CONVERT(DATE, 
            [Ano (Código)] + '-01-01') AS Data,
        TRY_CAST(
        CASE 
            WHEN [Valor] = '...' THEN NULL
            ELSE [Valor]
        END AS NUMERIC(10,2)) AS PIB_Anual,
        Variável
    from PIB_Anual
)

-- retorno dos dados transformados
select * from stg_PIB_Anual
