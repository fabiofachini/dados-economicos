-- models/staging/stg_Rendimento_Trabalho_Principal.sql

with Rendimento_Trabalho_Principal as (
    select * from {{ source('dbo', 'Rendimento_Trabalho_Principal') }}
),

-- transformação dos dados
stg_Rendimento_Trabalho_Principal as (
    select
        cast(data as date) as date,
        cast(valor as numeric) as value
    from Rendimento_Trabalho_Principal
)

-- retorno dos dados transformados
select * from stg_Rendimento_Trabalho_Principal
