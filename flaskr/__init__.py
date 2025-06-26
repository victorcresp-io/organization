import os
import requests

from flaskr.db import get_db
from flask import Flask, render_template, request
from flaskr.functions.uber_function import inserirValoresDb

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

    # a simple page that says hello
    @app.route('/', methods = ['GET', 'POST'])
    def main_page():
        teste = request.form.get('valorTotalUber')
        print(teste)
        return render_template('base.html')
    
    @app.route('/informacao_uber', methods = ['GET', 'POST'])
    def informacao_uber():
        teste = request.form.get('valorTotalUber')
        print(teste)
        return render_template('informe_uber.html')
    
    @app.route('/diaria_uber', methods = ['GET', 'POST'])
    def diaria_uber():
        conn = get_db()
        inserirValoresDb(conn)
        return render_template('diaria_uber.html')

    @app.route('/gastos_diaria', methods = ['GET', 'POST'])
    def gastos_diaria():
        return render_template('gastos_diaria.html')
    
    from . import db
    db.init_app(app)

    return app

