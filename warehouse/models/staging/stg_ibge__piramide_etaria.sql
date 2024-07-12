-- models/staging/stg_ibge__piramide_etaria.sql

with piramide_etaria as (
    select * from {{ source('dbo', 'piramide_etaria') }}
),

-- transformação dos dados
stg_ibge__piramide_etaria as (
    select
        CONVERT(DATE, 
            [Ano (Código)] + '-01-01') AS Data,
        TRY_CAST(
        CASE 
            WHEN [Valor] = '...' THEN NULL
            ELSE [Valor]
        END AS INT) AS Piramide_Etaria,
        Sexo,
        [Grupo de idade]
    from piramide_etaria
)

-- retorno dos dados transformados
select * from stg_ibge__piramide_etaria
