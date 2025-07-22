from flaskr import create_app
from flaskr.db import get_db

app = create_app()

with app.app_context():
    conn = get_db()
    cursor = conn.cursor()
    res = cursor.execute("SELECT date FROM uber_daily_cost WHERE date == '20/01/2001'").fetchall()
    exemplo_saida = res[0]
    print(exemplo_saida)
    print(type(exemplo_saida))

'''    cursor.execute("DELETE FROM uber_daily_money")
    conn.commit()'''



'''    res = cursor.execute("""SELECT name FROM sqlite_master WHERE type = 'table'""").fetchall()
'''    