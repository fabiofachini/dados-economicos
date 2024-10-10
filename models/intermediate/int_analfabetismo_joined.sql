-- models/intermediate/int_analfabetismo_joined.sql

with stg_ibge__taxa_de_analfabetismo as (
    select * from {{ ref('stg_ibge__taxa_de_analfabetismo') }}
),

-- transformação dos dados
stg_ibge__taxa_de_analfabetismo_m as (
    select 
        Data,
        Taxa_de_Analfabetismo as Taxa_de_Analfabetismo_Mulheres
    from stg_ibge__taxa_de_analfabetismo
    where Sexo = 'Mulheres'
),

stg_ibge__taxa_de_analfabetismo_h as (
    select 
        Data,
        Taxa_de_Analfabetismo as Taxa_de_Analfabetismo_Homens
    from stg_ibge__taxa_de_analfabetismo
    where Sexo = 'Homens'
),

stg_ibge__taxa_de_analfabetismo_t as (
    select 
        Data,
        Taxa_de_Analfabetismo as Taxa_de_Analfabetismo_Total
    from stg_ibge__taxa_de_analfabetismo
    where Sexo = 'Total'
),

int_analfabetismo_joined as (
    select 
        m.Data as Data,
        m.Taxa_de_Analfabetismo_Mulheres,
        h.Taxa_de_Analfabetismo_Homens,
        t.Taxa_de_Analfabetismo_Total
        
    from stg_ibge__taxa_de_analfabetismo_m m

    left join stg_ibge__taxa_de_analfabetismo_h h on m.Data = h.Data
    left join stg_ibge__taxa_de_analfabetismo_t t on m.Data = t.Data
)

-- retorno dos dados
select * from int_analfabetismo_joined;
