-- models/staging/stg_cambio_dolar.sql

with cambio_dolar as (
    select
        data,
        valor
    from {{ source('raw', 'Taxa_de_Cambio_Dolar') }}
),

-- Renamed and transformed data
renamed_cambio_dolar as (
    select
        data as date,
        valor as value
    from cambio_dolar
)

-- Select statement to return final transformed data
select * from renamed_cambio_dolar
