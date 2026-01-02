import typing
from datetime import datetime, date

from flask import request
    
def data_despesa(form) -> date:
    """
        Função responsável por capturar a data do formulário de despesa
    """

    data_despesa = form.data_despesa.data

    return data_despesa

def descricao_gasto(form) -> str:
    """
    Função responsável por capturar o campo de 'descricao_despesa'
    """

    descricao_despesa = form.descricao_despesa.data

    return descricao_despesa

def itens_despesa(form) -> str:
    """
    Função responsável por capturar o valor da label itens_despesa
    """

    itens_despesa = form.itens_despesa.data

    return itens_despesa

def motivo_despesa(form) -> str:
    """
    Função responsável por capturar o valor da label 'motivo_despesa'
    """

    motivo_despesa = form.motivo_despesa.data

    return motivo_despesa

def valor_total_despesa(form) -> str:
    """
    Função responsável por capturar o valor da label 'valor_total_despesa'
    """

    valor_total_despesa = float(form.valor_total_despesa.data)

    return valor_total_despesa


def inserir_despesas_para_db(conn: object, form):
    """
    Insere os valores capturados pela função para o DB.

    Args:

    conn: Conexão com o banco de dados


    Response:

    None
    """ 
    data_desp = data_despesa(form)
    dsc_gasto = descricao_gasto(form)
    dsc_despesa = itens_despesa(form)
    desc_mot = motivo_despesa(form)
    valo_tot = valor_total_despesa(form)

    print(data_desp)
    print(dsc_gasto)
    print(dsc_despesa)
    print(desc_mot)
    print(valo_tot)

    conn.execute("""
    INSERT INTO despesas2 (data, tipo_despesa, explicacao_despesa, item_despesa, valor_total_despesa) 
                 VALUES (?, ?, ?, ?, ?)
""", (data_desp, desc_mot, dsc_gasto, dsc_despesa, valo_tot))
    
    conn.commit()
    conn.close()
    print('dados inseridos no banco de dados')