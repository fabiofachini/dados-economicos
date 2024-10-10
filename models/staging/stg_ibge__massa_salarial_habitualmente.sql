-- models/staging/stg_ibge__massa_salarial_habitualmente.sql

with massa_salarial_habitualmente as (
    select * from {{ source('dbo', 'massa_salarial_habitualmente') }}
),

-- transformação dos dados
stg_ibge__massa_salarial_habitualmente as (
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
    from massa_salarial_habitualmente
)

-- retorno dos dados transformados
select * from stg_ibge__massa_salarial_habitualmente
