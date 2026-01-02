
from wtforms import Form, StringField, DateField, DecimalField, TimeField, SelectField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError

class DiariaUber(Form):
    valor = DecimalField('Valor da diária', validators=[DataRequired()])
    data = DateField('Data', validators=[DataRequired()])
    tempo = TimeField('Tempo total', validators=[DataRequired()])
 
class GastosUber(Form):
    opcao = SelectField(
        'Escolha uma opção',
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
    descricao_gasto = StringField('Com o que foi gasto?', validators=[DataRequired()])
    data = DateField('Informe o dia que foi feita a diária', validators=[DataRequired()])
    gasto = DecimalField('Qual foi o valor?', validators=[DataRequired()])

class UberFiltering(Form):
    data_inicial = DateField('Data inicial', validators=[DataRequired()])
    data_final = DateField('Data final', validators=[DataRequired()])
    opcao = SelectField(
        'Escolha uma opção',
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

