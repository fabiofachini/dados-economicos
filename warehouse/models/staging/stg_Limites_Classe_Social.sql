-- models/staging/stg_Limites_Classe_Social.sql

with Limites_Classe_Social as (
    select * from {{ source('dbo', 'Limites_Classe_Social') }}
),

-- transformação dos dados
stg_Limites_Classe_Social as (
    select
        cast(data as date) as date,
        cast(valor as numeric) as value
    from Limites_Classe_Social
)

-- retorno dos dados transformados
select * from stg_Limites_Classe_Social
