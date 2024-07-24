-- models/marts/fato_cambio.sql

with int_cambio_joined as (
    select * from {{ ref('int_cambio_joined') }}
)

-- transformação dos dados

-- retorno dos dados
select * from int_cambio_joined where Data >= '2000-01-01'