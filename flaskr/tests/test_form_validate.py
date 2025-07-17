import unittest

from functions.model import DiariaUber
from wtforms import Form

class TestFormValidate:
    def test_validate_form():

        dados = {
            'valor': 150.00,
            'data' : '2025-07-11',
            'tempo': '02:30'
        }

        form = DiariaUber(data=dados)

        assert form.validate()

if __name__ == '__main__':
    unittest.main()
