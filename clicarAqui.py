from flaskr import create_app
from flaskr.db import get_db

app = create_app()

with app.app_context():
    conn = get_db()
    cursor = conn.cursor()


    res = cursor.execute("""SELECT * FROM uber_daily_cost""").fetchall()
    print(res)

"""
Teste feito para verificar se os dados estão sendo
inseridos no banco de dados. As funções estão funcionando
perfeitamente. É NECESSÁRIO organizar o código e fazer os testes.

Este módulo foi criado como um teste de inserção do db.

Precisa-se saber como fazer test com formulários.

"""