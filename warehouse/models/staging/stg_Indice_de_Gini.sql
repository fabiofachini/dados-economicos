-- models/staging/stg_Indice_de_Gini.sql

with Indice_de_Gini as (
    select * from {{ source('dbo', 'Indice_de_Gini') }}
),

-- transformação dos dados
stg_Indice_de_Gini as (
    select
        cast(data as date) as date,
        cast(valor as numeric) as value
    from Indice_de_Gini
)

-- retorno dos dados transformados
select * from stg_Indice_de_Gini
