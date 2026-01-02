import os
import requests

from flaskr.db import get_db, init_db
from flask import Flask, render_template, request
from flaskr.functions.capturar_html import inserir_db_diaria, inserir_db_gastos, capturar_tempo_gasto, capturar_data
from flaskr.functions.uber_function import inserirValoresDb
from flaskr.functions.uber_gastos_function import inserirValoresDbGastos
from flaskr.functions.model import DiariaUber, GastosUber, Despesas

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )
    # load the instance config, if it exists, when not testing
    app.config.from_pyfile('config.py', silent=True)

    # load the test config if passed in
    if test_config is None:
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
        print('Pasta instance criada com sucesso!')
    except OSError:
        print('A pasta instance já existe ou ocorreu erro ao criar.')
        pass

    # Main route
    @app.route('/', methods = ['GET', 'POST'])
    def main_page():
        if not os.path.exists(app.config['DATABASE']):
            init_db()
        return render_template('base.html')
    
    #Routes for Uber cost
    @app.route('/informacao_uber', methods = ['GET', 'POST'])
    def informacao_uber():
        teste = request.form.get('valorTotalUber')
        print(teste)
        return render_template('informe_uber.html')
    
    @app.route('/diaria_uber', methods = ['GET', 'POST'])
    def diaria_uber():
        form = DiariaUber(request.form)
        if request.method == 'POST':
            conn = get_db()
            inserir_db_diaria(conn, form)
        return render_template('diaria_uber.html', form = form)

    @app.route('/gastos_diaria', methods = ['GET', 'POST'])
    def gastos_diaria():
        form = GastosUber(request.form)
        if request.method == 'POST':
            conn = get_db()
            inserir_db_gastos(conn, form)
        return render_template('gastos_diaria.html', form = form)
    
    #Route for monitoring and filtering uber costs
    @app.route("/despesas", methods = ['GET', 'POST'])
    def uber_filtering():
        form = Despesas(request.form)
        return render_template('despesas.html', form=form)
    from . import db
    db.init_app(app)

    return app

