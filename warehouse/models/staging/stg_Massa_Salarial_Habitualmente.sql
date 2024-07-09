-- models/staging/stg_Massa_Salarial_Habitualmente.sql

with Massa_Salarial_Habitualmente as (
    select * from {{ source('dbo', 'Massa_Salarial_Habitualmente') }}
),

-- transformação dos dados
stg_Massa_Salarial_Habitualmente as (
    select
        CONVERT(DATE, 
            SUBSTRING(CAST([Trimestre Móvel (Código)] AS VARCHAR(6)), 1, 4) + '-' + 
            SUBSTRING(CAST([Trimestre Móvel (Código)] AS VARCHAR(6)), 5, 2) + '-01') AS Data,
        TRY_CAST(
        CASE 
            WHEN [Valor] = '...' THEN NULL
            ELSE [Valor]
        END AS INT
    ) AS Massa_Salarial_Habitualmente
    from Massa_Salarial_Habitualmente
)

-- retorno dos dados transformados
select * from stg_Massa_Salarial_Habitualmente
