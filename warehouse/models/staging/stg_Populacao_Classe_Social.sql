-- models/staging/stg_Populacao_Classe_Social.sql

with Populacao_Classe_Social as (
    select * from {{ source('dbo', 'Populacao_Classe_Social') }}
),

-- transformação dos dados
stg_Populacao_Classe_Social as (
    select
        cast(data as date) as date,
        cast(valor as numeric) as value
    from Populacao_Classe_Social
)

-- retorno dos dados transformados
select * from stg_Populacao_Classe_Social
