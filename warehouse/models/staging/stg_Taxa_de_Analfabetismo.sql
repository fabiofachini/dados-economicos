-- models/staging/stg_Taxa_de_Analfabetismo.sql

with Taxa_de_Analfabetismo as (
    select * from {{ source('dbo', 'Taxa_de_Analfabetismo') }}
),

-- transformação dos dados
stg_Taxa_de_Analfabetismo as (
    select
        CONVERT(DATE, 
            [Ano (Código)] + '-01-01') AS Data,
        TRY_CAST(
        CASE 
            WHEN [Valor] = '...' THEN NULL
            ELSE [Valor]
        END AS NUMERIC(10,1)) AS Taxa_de_Analfabetismo,
        Sexo,
        [Grupo de idade]
    from Taxa_de_Analfabetismo
)

-- retorno dos dados transformados
select * from stg_Taxa_de_Analfabetismo
