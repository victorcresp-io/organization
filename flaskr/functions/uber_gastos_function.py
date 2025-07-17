import typing
from datetime import datetime, date

from flask import request
    
def capturarDataHtmlGastos() -> date:
    """
    Captura a data inserida pelo usuário no formulário do html 'diaria_uber.html'

    Args:

    None

    Response:

    Date: Data enviada pelo formulário convertida para objeto date
    """

    data = request.form.get('data_diaria')

    return data

def capturarDiariaHtmlGastos() -> float:
    """
    Captura a diária inserida pelo usuário no formulário do html 'diaria_uber.html'

    Args:

    None

    Response:

    Float: Diária enviada pelo formulário convertida para objeto float
    """

    diaria = request.form.get('valor_gasto')
    print('oi')
    print(diaria)
    diaria_formatada = float(diaria)
    return diaria_formatada

def capturarTempoTotalHtmlGastos() -> str:
    """
    Captura o com o que foi gasto 

    Args:

    None

    Response:

    """

    descricao_gasto = request.form.get('descricao_gasto')
    return descricao_gasto

def inserirValoresDbGastos(conn: object):
    """
    Insere os valores capturados pela função para o DB.

    Args:

    conn: Conexão com o banco de dados


    Response:

    None
    """ 

    dataDiaria = capturarDataHtmlGastos()
    diaria = capturarDiariaHtmlGastos()
    tempo_total = capturarTempoTotalHtmlGastos()
    print(tempo_total)
    print(dataDiaria)
    conn.execute("""
    INSERT INTO uber_daily_cost VALUES (?, ?, ?)
""", (diaria, dataDiaria, tempo_total))
    conn.commit()