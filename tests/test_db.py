import unittest

from flaskr import create_app
from flaskr.db import get_db

class TestStringMethods(unittest.TestCase):

    def test_db(self):
        app = create_app()
        with app.app_context():
            conn = get_db()
            cursor = conn.cursor()
            result = cursor.execute("SELECT name FROM sqlite_master WHERE type='table';").fetchall()
            self.assertEqual(result, [('uber_daily_money',), ('uber_daily_cost',)])

if __name__ == '__main__':
    unittest.main()