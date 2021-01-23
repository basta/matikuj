from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, SelectField, RadioField, FileField
from wtforms.validators import DataRequired


class CreateQuestionForm(FlaskForm):
    body = TextAreaField('Zadání otázky', validators=[DataRequired()])
    image64 = FileField('Obrázek k zadání')
    typ = SelectField('Typ otázky', choices=[('field', 'Napiš odpověď'), ('multiple', 'Vyber správné'),], default=1)
    # field
    result_field = StringField('Správný výsledek')
    # multiple
<<<<<<< HEAD
    multiple_ans_type = SelectField('Typ možností', choices=[('math', 'Matematické pole'), ('field', 'Textové pole'), ('graph', 'Graf funkce'), ('image', 'Obrázek'),])
=======
    multiple_ans_type = SelectField('Typ možností', choices=[('field', 'Textové pole'), ('math', 'Matematické pole'), ('graph', 'Graf funkce'), ('image', 'Obrázek'),])
>>>>>>> 72e36bde36097b5859584b80dd42f880c5636f2c
    multiple_ans_img = FileField('Obrázek')
    multiple_ans_graph = StringField('Graf funkce')
    multiple_ans_field = StringField('Text')
    result_multiple = StringField('Správný výsledek')
    difficulty = SelectField('Obtížnost', choices=[i+1 for i in range(10)])
    tags = StringField('Tagy k úloze')
    submitter = 0
    submit = SubmitField('Submit')
