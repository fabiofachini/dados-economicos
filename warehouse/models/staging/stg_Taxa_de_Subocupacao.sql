-- models/staging/stg_Taxa_de_Subocupacao.sql

with Taxa_de_Subocupacao as (
    select * from {{ source('dbo', 'Taxa_de_Subocupacao') }}
),

-- transformação dos dados
stg_Taxa_de_Subocupacao as (
    select
        CONVERT(DATE, 
            SUBSTRING(CAST([Trimestre Móvel (Código)] AS VARCHAR(6)), 1, 4) + '-' + 
            SUBSTRING(CAST([Trimestre Móvel (Código)] AS VARCHAR(6)), 5, 2) + '-01') AS Data,
        TRY_CAST(
        CASE 
            WHEN [Valor] = '...' THEN NULL
            ELSE [Valor]
        END AS NUMERIC(10,1)
    ) AS Taxa_de_Subocupacao
    from Taxa_de_Subocupacao
)

-- retorno dos dados transformados
select * from stg_Taxa_de_Subocupacao
