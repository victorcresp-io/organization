from flaskr.functions.uber_function import AdicionarDiariaUberParaDb
from unittest.mock import MagicMock
import pytest

def test_AdicionarDiariaUberParaDb():
    # Cria um mock para a conexão
    mock_conn = MagicMock()

    # Valor fictício para o teste
    valor_teste = 123.45

    # Chama a função passando o mock ao invés da conexão real
    AdicionarDiariaUberParaDb(mock_conn, valor_teste)

    # Verifica se o método execute foi chamado com os parâmetros esperados
    mock_conn.execute.assert_called_once_with("INSERT INTO table VALUES (%s);", valor_teste)
