-- models/staging/stg_Custo_CUB_m2.sql

with Custo_CUB_m2 as (
    select * from {{ source('dbo', 'Custo_CUB_m2') }}
),

-- transformação dos dados
stg_Custo_CUB_m2 as (
    select
        CONVERT(DATE, 
            SUBSTRING(CAST([Mês (Código)] AS VARCHAR(6)), 1, 4) + '-' + 
            SUBSTRING(CAST([Mês (Código)] AS VARCHAR(6)), 5, 2) + '-01') AS Data,
        TRY_CAST(
        CASE 
            WHEN [Valor] = '...' THEN NULL
            ELSE [Valor]
        END AS NUMERIC(10,2)
    ) AS Custo_CUB_m2
    from Custo_CUB_m2
)

-- retorno dos dados transformados
select * from stg_Custo_CUB_m2
