-- models/staging/stg_Nivel_de_Desocupacao.sql

with Nivel_de_Desocupacao as (
    select * from {{ source('dbo', 'Nivel_de_Desocupacao') }}
),

-- transformação dos dados
stg_Nivel_de_Desocupacao as (
    select
        CONVERT(DATE, 
            SUBSTRING(CAST([Mês (Código)] AS VARCHAR(6)), 1, 4) + '-' + 
            SUBSTRING(CAST([Mês (Código)] AS VARCHAR(6)), 5, 2) + '-01') AS Data,
        TRY_CAST(
        CASE 
            WHEN [Valor] = '...' THEN NULL
            ELSE [Valor]
        END AS NUMERIC(10,1)
    ) AS Nivel_de_Desocupacao
    from Nivel_de_Desocupacao

)

-- retorno dos dados transformados
select * from stg_Nivel_de_Desocupacao
