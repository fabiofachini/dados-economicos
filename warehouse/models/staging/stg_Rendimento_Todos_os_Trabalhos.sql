-- models/staging/stg_Rendimento_Todos_os_Trabalhos.sql

with Rendimento_Todos_os_Trabalhos as (
    select * from {{ source('dbo', 'Rendimento_Todos_os_Trabalhos') }}
),

-- transformação dos dados
stg_Rendimento_Todos_os_Trabalhos as (
    select
        cast(data as date) as date,
        cast(valor as numeric) as value
    from Rendimento_Todos_os_Trabalhos
)

-- retorno dos dados transformados
select * from stg_Rendimento_Todos_os_Trabalhos
