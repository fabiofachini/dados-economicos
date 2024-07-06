-- models/staging/stg_Rendimento_Classe_Social.sql

with Rendimento_Classe_Social as (
    select * from {{ source('dbo', 'Rendimento_Classe_Social') }}
),

-- transformação dos dados
stg_Rendimento_Classe_Social as (
    select
        cast(data as date) as date,
        cast(valor as numeric) as value
    from Rendimento_Classe_Social
)

-- retorno dos dados transformados
select * from stg_Rendimento_Classe_Social
