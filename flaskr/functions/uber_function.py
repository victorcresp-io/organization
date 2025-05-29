import typing

def AdicionarDiariaUberParaDb(conn: object, valorDiaria: float):
    """
    Captura o valor do HTML e o adiciona ao banco de dados.

    Args:

    conn: Conexão com o banco de dados

    valorDiaria: Valor da diária feita na Uber (capturada no HTML)

    Response:

    None
    """ 

    query = "INSERT INTO table VALUES (%s);"
    data = (valorDiaria,)
    conn.execute(query, data)