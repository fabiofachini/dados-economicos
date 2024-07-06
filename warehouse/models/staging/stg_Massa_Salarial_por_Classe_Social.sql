-- models/staging/stg_Massa_Salarial_por_Classe_Social.sql

with Massa_Salarial_por_Classe_Social as (
    select * from {{ source('dbo', 'Massa_Salarial_por_Classe_Social') }}
),

-- transformação dos dados
stg_Massa_Salarial_por_Classe_Social as (
    select
        cast(data as date) as date,
        cast(valor as numeric) as value
    from Massa_Salarial_por_Classe_Social
)

-- retorno dos dados transformados
select * from stg_Massa_Salarial_por_Classe_Social
