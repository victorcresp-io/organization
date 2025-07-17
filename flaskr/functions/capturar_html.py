# Funções para a rota "diária"
def capturar_data(form):
    data = form.data.data
    data_string = data.strftime("%d/%m/%Y")
    return data_string

def capturar_valor(form):
    diaria = float(form.valor.data)
    return diaria

def capturar_tempo_gasto(form):
    tempo_gasto = form.tempo.data
    tempo_gasto_string = tempo_gasto.strftime("%H:%M:%S")
    return tempo_gasto_string

def inserir_db_diaria(conn, form):
    diaria = capturar_valor(form)
    data_diaria = capturar_data(form)
    tempo_total = capturar_tempo_gasto(form)

    conn.execute("""
    INSERT INTO uber_daily_money VALUES (?, ?, ?)
""", (diaria, data_diaria, tempo_total))
    conn.commit()
    conn.close()

# Funções para a rota "Gastos"
def capturar_gastos(form):
    gasto = float(form.gasto.data)
    return gasto

def capturar_descricao_gasto(form):
    descricao_gasto = form.descricao_gasto.data
    return descricao_gasto

def inserir_db_gastos(conn, form):
    data_diaria = capturar_data(form)
    valor_gasto = capturar_gastos(form)
    descricao_gasto = capturar_descricao_gasto(form)
    print(data_diaria)
    print(valor_gasto)
    print(descricao_gasto)
    conn.execute("""
    INSERT INTO uber_daily_cost VALUES (?, ?, ?)
""", (data_diaria, valor_gasto, descricao_gasto))
    conn.commit()
    conn.close()