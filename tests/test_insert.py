import unittest

from flaskr import create_app
from flaskr.db import get_db
from flaskr.functions.uber_function import AdicionarDiariaUberParaDb

class TestInsertValuesToDatabase(unittest.TestCase):

    def test_insert(self):
        app = create_app()
        with app.app_context():
            conn = get_db()
            cursor = conn.cursor()
            AdicionarDiariaUberParaDb(conn, 123)

            result = cursor.execute("SELECT cost FROM uber_daily_money").fetchall()

            self.assertEqual(result, [(123,)])

#Necessário atualizar este teste