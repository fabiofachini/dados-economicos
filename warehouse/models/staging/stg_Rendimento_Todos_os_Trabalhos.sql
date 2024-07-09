-- models/staging/stg_Rendimento_Todos_os_Trabalhos.sql

with Rendimento_Todos_os_Trabalhos as (
    select * from {{ source('dbo', 'Rendimento_Todos_os_Trabalhos') }}
),

-- transformação dos dados
stg_Rendimento_Todos_os_Trabalhos as (
    select
        CONVERT(DATE, 
            SUBSTRING(CAST([Trimestre Móvel (Código)] AS VARCHAR(6)), 1, 4) + '-' + 
            SUBSTRING(CAST([Trimestre Móvel (Código)] AS VARCHAR(6)), 5, 2) + '-01') AS Data,
        TRY_CAST(
        CASE 
            WHEN [Valor] = '...' THEN NULL
            ELSE [Valor]
        END AS INT
    ) AS Rendimento_Todos_os_Trabalhos
    from Rendimento_Todos_os_Trabalhos
)

-- retorno dos dados transformados
select * from stg_Rendimento_Todos_os_Trabalhos
