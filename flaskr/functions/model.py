
from wtforms import Form, StringField, DateField, DecimalField, TimeField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError

class DiariaUber(Form):
    valor = DecimalField('Valor da diária', validators=[DataRequired()])
    data = DateField('Data', validators=[DataRequired()])
    tempo = TimeField('Tempo total', validators=[DataRequired()])
