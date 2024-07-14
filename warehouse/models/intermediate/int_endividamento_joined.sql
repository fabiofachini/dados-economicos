-- models/intermediate/int_endividamento_joined.sql

with stg_bacen__endividamento_familias as (
    select * from {{ ref('stg_bacen__endividamento_familias') }}
),

stg_bacen__endividamento_familias_s_habitacional as (
    select * from {{ ref('stg_bacen__endividamento_familias_s_habitacional') }}
),

-- transformação dos dadosS
int_endividamento_joined as (
    select 
        endiv.Data as Data,
        endiv.Endividamento_Familias,
        endiv_sh.Endividamento_Familias_S_Habitacional

    from stg_bacen__endividamento_familias endiv

    left join stg_bacen__endividamento_familias_s_habitacional endiv_sh on endiv.Data = endiv_sh.Data
)

-- retorno dos dados
select * from int_endividamento_joined;
