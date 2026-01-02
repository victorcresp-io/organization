
from wtforms import Form, StringField, DateField, DecimalField, TimeField, SelectField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError

class DiariaUber(Form):
    valor = DecimalField('Valor da diária', validators=[DataRequired()])
    data = DateField('Data', validators=[DataRequired()])
    tempo = TimeField('Tempo total', validators=[DataRequired()])
 
class GastosUber(Form):
    descricao_gasto = StringField('Com o que foi gasto?', validators=[DataRequired()])
    data = DateField('Informe o dia que foi feita a diária', validators=[DataRequired()])
    gasto = DecimalField('Qual foi o valor?', validators=[DataRequired()])

class Despesas(Form):
    data_inicial = DateField('Data', validators=[DataRequired()])
    descricao_gasto = StringField('Explique a razão desta despesa', validators=[DataRequired()])
    opcao = SelectField(
        'Motivo despesa',
        choices = [
            ('Alimentação'),
            ('Mercado'),
            ('Farmácia'),
            ('Gasolina'),
            ('Empréstimo'),
            ('Acessórios'),
        ],
        validators=[DataRequired()]
    )

