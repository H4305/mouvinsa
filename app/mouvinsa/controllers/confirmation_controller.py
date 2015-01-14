from wtforms import Form, TextField, DateField, validators


class ConfirmationForm(Form):
    lastname = TextField(u'Nom', [validators.Length(min=4, max=25)])
    firstname = TextField(u'Prenom', [validators.Length(min=4, max=25)])
    birthdate = DateField(u'Date de Naissance', format='%d/%m/%Y')
    weight = TextField(u'Poids', [validators.Length(min=6, max=35)])
    height = TextField(u'Hauteur', [validators.Length(min=6, max=35)])
    image = TextField(u'Image', [validators.Length(min=0, max=255)])

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])
def checkExtFile(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS