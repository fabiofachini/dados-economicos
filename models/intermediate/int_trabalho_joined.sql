-- models/intermediate/int_trabalho_joined.sql

with stg_ibge__taxa_de_desalentados as (
    select * from {{ ref('stg_ibge__taxa_de_desalentados') }}
),

stg_ibge__taxa_de_desocupacao as (
    select * from {{ ref('stg_ibge__taxa_de_desocupacao') }}
),

stg_ibge__nivel_de_desocupacao as (
    select * from {{ ref('stg_ibge__nivel_de_desocupacao') }}
),

stg_ibge__taxa_de_informalidade as (
    select * from {{ ref('stg_ibge__taxa_de_informalidade') }}
),

stg_ibge__taxa_de_part_forca_de_trabalho as (
    select * from {{ ref('stg_ibge__taxa_de_part_forca_de_trabalho') }}
),

stg_ibge__taxa_de_subocupacao as (
    select * from {{ ref('stg_ibge__taxa_de_subocupacao') }}
),

-- transformação dos dados
int_trabalho_joined as (
    select 
        d.Data as Data,
        d.Taxa_de_Desalentados,
        de.Taxa_de_Desocupacao,
        des.Nivel_de_Desocupacao,        
        i.Taxa_de_Informalidade,
        p.Taxa_de_Part_Forca_de_Trabalho,
        s.Taxa_de_Subocupacao

    from stg_ibge__taxa_de_desalentados d

    left join stg_ibge__taxa_de_desocupacao de on d.Data = de.Data
    left join stg_ibge__nivel_de_desocupacao des on d.Data = des.Data
    left join stg_ibge__taxa_de_informalidade i on d.Data = i.Data
    left join stg_ibge__taxa_de_part_forca_de_trabalho p on d.Data = p.Data
    left join stg_ibge__taxa_de_subocupacao s on d.Data = s.Data
)

-- retorno dos dados
select * from int_trabalho_joined;
