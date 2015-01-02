from wtforms import Form, TextField, DateField, validators, FloatField, IntegerField, SelectField


class ConfirmationForm(Form):
    lastname = TextField(u'Nom', validators=[validators.Optional(), validators.Length(min=2, max=25, message='La longeur doit etre comprise entre 2 et 25 caracteres.')])
    firstname = TextField(u'Prenom',[validators.Optional(), validators.Length(min=2, max=25, message='La longeur doit etre comprise entre 2 et 25 caracteres.')])
    birthdate = DateField(u'Date de Naissance', format='%d/%m/%Y',validators=[validators.Optional()])
    weight = FloatField(u'Poids (kg)',[validators.Optional(), validators.NumberRange(min=20, max=300, message='Le poids doit etre compris entre 20 kg et 300 kg')])
    height = IntegerField(u'Taille (cm)', [validators.Optional(), validators.NumberRange(min=90, max=250, message='La taille doit etre comprise entre 90 cm et 250 cm.')])
    sex = SelectField(u'Sexe ', choices=[('', ''), ('Masculin', 'Masculin'), ('Feminin', 'Feminin')])
    image = TextField(u'Image', [validators.Length(min=0, max=255)])

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])
def checkExtImage(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

def updateProfil(form, person):
        person.lastname = form.lastname.data
        person.firstname = form.firstname.data
        person.weight = form.weight.data
        person.height = form.height.data
        person.birthdate = form.birthdate.data
        person.sex = form.sex.data
        person.etat = 'REGISTERED'