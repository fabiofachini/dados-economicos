-- models/staging/stg_ibge__nivel_de_desocupacao.sql

with nivel_de_desocupacao as (
    select * from {{ source('dbo', 'nivel_de_desocupacao') }}
),

-- transformação dos dados
stg_ibge__nivel_de_desocupacao as (
    select
        CONVERT(DATE, 
            SUBSTRING(CAST([Trimestre Móvel (Código)] AS VARCHAR(6)), 1, 4) + '-' + 
            SUBSTRING(CAST([Trimestre Móvel (Código)] AS VARCHAR(6)), 5, 2) + '-01') AS Data,
        TRY_CAST(
        CASE 
            WHEN [Valor] = '...' THEN NULL
            ELSE [Valor]
        END AS NUMERIC(10,1)
    ) AS Nivel_de_Desocupacao
    from nivel_de_desocupacao
)

-- retorno dos dados transformados
select * from stg_ibge__nivel_de_desocupacao