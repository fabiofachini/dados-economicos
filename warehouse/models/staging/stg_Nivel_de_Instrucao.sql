-- models/staging/stg_Nivel_de_Instrucao.sql

with Nivel_de_Instrucao as (
    select * from {{ source('dbo', 'Nivel_de_Instrucao') }}
),

-- transformação dos dados
stg_Nivel_de_Instrucao as (
    select
        cast(data as date) as date,
        cast(valor as numeric) as value
    from Nivel_de_Instrucao
)

-- retorno dos dados transformados
select * from stg_Nivel_de_Instrucao
