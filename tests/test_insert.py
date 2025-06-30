import unittest

from flaskr import create_app
from flaskr.db import get_db
from flaskr.functions.uber_function import AdicionarDiariaUberParaDb

'''class TestInsertValuesToDatabase(unittest.TestCase):

    
    def configuracao(self):
        app = create_app()
        self.client = app.test_client()

    def test_post_formulario(self):
        response = self.client.post()

    def test_insert(self):
        app = create_app()
        with app.app_context():
            conn = get_db()
            cursor = conn.cursor()
            in(conn, 123)

            result = cursor.execute("SELECT cost FROM uber_daily_money").fetchall()

            self.assertEqual(result, [(123,)])

#Necessário atualizar este teste'''