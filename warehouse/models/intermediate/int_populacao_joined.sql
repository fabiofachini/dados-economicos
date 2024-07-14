-- models/intermediate/int_populacao_joined.sql

with stg_ibge__populacao_economicamente_ativa_f as (
    select * from {{ ref('stg_ibge__populacao_economicamente_ativa') }}
    where Condição_Forca_Trabalho = 'Força de Trabalho'
),

stg_ibge__populacao_economicamente_ativa_fto as (
    select * from {{ ref('stg_ibge__populacao_economicamente_ativa') }}
    where Condição_Forca_Trabalho = 'Força de Trabalho - ocupada'
),

stg_ibge__populacao_economicamente_ativa_ftd as (
    select * from {{ ref('stg_ibge__populacao_economicamente_ativa') }}
    where Condição_Forca_Trabalho = 'Força de Trabalho - desocupada'
),

stg_ibge__populacao_economicamente_ativa_fo as (
    select * from {{ ref('stg_ibge__populacao_economicamente_ativa') }}
    where Condição_Forca_Trabalho = 'Fora da força de trabalho'
),

stg_ibge__populacao_economicamente_ativa_t as (
    select * from {{ ref('stg_ibge__populacao_economicamente_ativa') }}
    where Condição_Forca_Trabalho = 'Total'
),

stg_ibge__populacao_mensal as (
    select * from {{ ref('stg_ibge__populacao_mensal') }}
),

-- transformação dos dados
int_populacao_joined as (
    select 
        f.Data as Data,
        f.Populacao_Economicamente_Ativa as Forca_Trabalho,
        fto.Populacao_Economicamente_Ativa as Forca_Trabalho_Ocupada,
        ftd.Populacao_Economicamente_Ativa as Forca_Trabalho_Desocupada,
        fo.Populacao_Economicamente_Ativa as Fora_Forca_Trabalho,
        t.Populacao_Economicamente_Ativa as Forca_Trabalho_Total,
        pp.Populacao as População_Total
        
        
    from stg_ibge__populacao_economicamente_ativa_f f

    left join stg_ibge__populacao_economicamente_ativa_fto fto on f.Data = fto.Data
    left join stg_ibge__populacao_economicamente_ativa_ftd ftd on f.Data = ftd.Data
    left join stg_ibge__populacao_economicamente_ativa_fo fo on f.Data = fo.Data
    left join stg_ibge__populacao_economicamente_ativa_t t on f.Data = t.Data
    left join stg_ibge__populacao_mensal pp on f.Data = pp.Data
)

-- retorno dos dados
select * from int_populacao_joined