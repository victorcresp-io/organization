import os
import requests

from flask import Flask, render_template, request


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
    @app.route('/organizacao_uber', methods = ['GET', 'POST'])
    def hello():
        teste = request.form.get('valorTotalUber')
        print(teste)
        return render_template('base.html')
    return app