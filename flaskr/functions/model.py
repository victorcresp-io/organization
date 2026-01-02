
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
    data_despesa = DateField('Data', validators=[DataRequired()])
    descricao_despesa = StringField('Explique a razão desta despesa', validators=[DataRequired()])
    itens_despesa = StringField('Itens', validators=[DataRequired()])
    valor_total_despesa = DecimalField('Valor total da despesa', validators=[DataRequired()])
    motivo_despesa = SelectField(
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

