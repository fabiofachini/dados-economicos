-- models/staging/stg_ibge__massa_salarial_efetivamente.sql

with massa_salarial_efetivamente as (
    select * from {{ source('dbo', 'massa_salarial_efetivamente') }}
),

-- transformação dos dados
stg_ibge__massa_salarial_efetivamente as (
    select
        CONVERT(DATE, 
            SUBSTRING(CAST([Trimestre Móvel (Código)] AS VARCHAR(6)), 1, 4) + '-' + 
            SUBSTRING(CAST([Trimestre Móvel (Código)] AS VARCHAR(6)), 5, 2) + '-01') AS Data,
        TRY_CAST(
        CASE 
            WHEN [Valor] = '...' THEN NULL
            ELSE [Valor]
        END AS INT
    ) AS Massa_Salarial_Efetivamente
    from massa_salarial_efetivamente
)

-- retorno dos dados transformados
select * from stg_ibge__massa_salarial_efetivamente
