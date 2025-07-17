
def capturar_data(form):
    data = form.data.data
    data_string = data.strftime("%d/%m/%Y")
    return data_string

def capturar_diaria_feita(form):
    diaria = float(form.valor.data)
    return diaria

def capturar_tempo_gasto(form):
    tempo_gasto = (form.tempo.data)
    tempo_gasto_string = tempo_gasto.strftime("%H:%M:%S")
    return tempo_gasto_string

def inserir_db(conn, form):
    diaria = capturar_diaria_feita(form)
    data_diaria = capturar_data(form)
    tempo_total = capturar_tempo_gasto(form)

    conn.execute("""
    INSERT INTO uber_daily_money VALUES (?, ?, ?)
""", (diaria, data_diaria, tempo_total))
    conn.commit()
    conn.close()