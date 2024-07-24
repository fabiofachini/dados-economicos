-- models/marts/fato_contas_publicas.sql

with int_contas_publicas_joined as (
    select * from {{ ref('int_contas_publicas_joined') }}
)

-- transformação dos dados

-- retorno dos dados
select Data, NFSP_Setor_Publico_Ano, NFSP_Setor_Publico_Mes from int_contas_publicas_joined