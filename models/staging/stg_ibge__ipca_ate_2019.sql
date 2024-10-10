-- models/staging/stg_ibge__ipca_ate_2019.sql

with ipca_ate_2019 as (
    select * from {{ source('dbo', 'ipca_ate_2019') }}
),

-- transformação dos dados
stg_ibge__ipca_ate_2019 as (
    select
        CONVERT(DATE, 
            SUBSTRING(CAST([Mês (Código)] AS VARCHAR(6)), 1, 4) + '-' + 
            SUBSTRING(CAST([Mês (Código)] AS VARCHAR(6)), 5, 2) + '-01') AS Data,
        TRY_CAST(
        CASE 
            WHEN [Valor] = '...' THEN NULL
            ELSE [Valor]
        END AS NUMERIC(10,2)
    ) AS IPCA_ate_2019,
    Variável
    from ipca_ate_2019
)

-- retorno dos dados transformados
select * from stg_ibge__ipca_ate_2019
