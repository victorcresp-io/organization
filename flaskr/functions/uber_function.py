import typing

def AdicionarDiariaUberParaDb(conn: str, valorDiaria: float):
    """
    Adiciona o valor capturado do HTML e o adiciona ao banco de dados.

    Args:

    conn: Conexão com o banco de dados

    valorDiaria: Valor da diária feita na Uber (capturada no HTML)

    Response:

    None
    """ 

    query = "INSERT INTO table VALUES (%s);"
    data = valorDiaria
    conn.execute(query, data)