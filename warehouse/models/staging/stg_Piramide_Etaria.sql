-- models/staging/stg_Piramide_Etaria.sql

with Piramide_Etaria as (
    select * from {{ source('dbo', 'Piramide_Etaria') }}
),

-- transformação dos dados
stg_Piramide_Etaria as (
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
    from Piramide_Etaria
)

-- retorno dos dados transformados
select * from stg_Piramide_Etaria
