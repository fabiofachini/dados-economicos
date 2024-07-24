with int_confianca_joined as (
    select * from {{ ref('int_confianca_joined') }}
)

-- transformação dos dados

-- retorno dos dados ordenados por data
select * 
from int_confianca_joined