-- models/staging/stg_ibge__taxa_de_analfabetismo.sql

with taxa_de_analfabetismo as (
    select * from {{ source('dbo', 'taxa_de_analfabetismo') }}
),

-- transformação dos dados
stg_ibge__taxa_de_analfabetismo as (
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
    from taxa_de_analfabetismo
)

-- retorno dos dados transformados
select * from stg_ibge__taxa_de_analfabetismo
