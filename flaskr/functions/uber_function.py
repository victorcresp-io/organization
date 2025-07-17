import typing
from datetime import datetime, date

from flask import request
    
def capturarDataHtml() -> date:
    """
    Captura a data inserida pelo usuário no formulário do html 'diaria_uber.html'

    Args:

    None

    Response:

    Date: Data enviada pelo formulário convertida para objeto date
    """

    data = request.form.get('data_diaria')

    
    return data

def capturarDiariaHtml() -> float:
    """
    Captura a diária inserida pelo usuário no formulário do html 'diaria_uber.html'

    Args:

    None

    Response:

    Float: Diária enviada pelo formulário convertida para objeto float
    """

    diaria = request.form.get('valor_diaria')
    return diaria

def capturarTempoTotalHtml() -> str:
    """
    Captura o tempo total inserido pelo usuário no formulário do html 'diaria_uber.html'

    Args:

    None

    Response:

    Datetime: Tempo total enviado pelo formulário convertida para objeto datetime
    """

    tempo_total = request.form.get('tempo_total')
    return tempo_total

def inserirValoresDb(conn: object):
    """
    Insere os valores capturados pela função para o DB.

    Args:

    conn: Conexão com o banco de dados


    Response:

    None
    """ 

    dataDiaria = capturarDataHtml()
    diaria = capturarDiariaHtml()
    tempo_total = capturarTempoTotalHtml()
    print(dataDiaria)
    conn.execute("""
    INSERT INTO uber_daily_money VALUES (?, ?, ?)
""", (diaria, dataDiaria, tempo_total))
    conn.commit()