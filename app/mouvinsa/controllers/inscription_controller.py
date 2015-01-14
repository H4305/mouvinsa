from wtforms import Form, BooleanField, TextField, FloatField, PasswordField, SelectField, DateField, validators
import uuid
from hashlib import sha256


def hash_password(password):
    salt = uuid.uuid4().hex
    return sha256(salt.encode() + password.encode()).hexdigest() + \
        ':' + salt


messageObligatoire='Ce champs est obligatoire. Veuillez le remplir.'
messageEmail='Les 2 emails doivent correspondre. Veuillez reessayer.'
messageLongueur2_25='La longeur doit etre comprise entre 2 et 25 caracteres.'
messagePassword='Les 2 mots de passe doivent correspondre.  Veuillez reessayer.'
messageLongueur4_25='La longeur doit etre comprise entre 4 et 25 caracteres.'
messagePoids='Le poids doit etre compris entre 20 kg et 300 kg'
messageTaille='La taille doit etre comprise entre 90 cm et 250 cm.'
messageLongueur3_100='La longeur doit etre comprise entre 3 et 100 caracteres.'
choices=[('', ''), ('Premier', 'Premier'), ('Second', 'Second')]

class InscriptionForm(Form):
	email = TextField(u'Email', [validators.Required(message=messageObligatoire), validators.EqualTo('confirmEmail', message=messageEmail)])
	confirmEmail = TextField(u'Confirmez votre email', [validators.Required(message=messageObligatoire)])
	surnom = TextField(u'Pseudonyme', [validators.Required(message=messageObligatoire), validators.Length(min=2, max=25, message=messageLongueur2_25)])
	nom = TextField(u'Nom', [validators.Optional(), validators.Length(min=2, max=25, message=messageLongueur2_25)])
	prenom = TextField(u'Prenom', [validators.Optional(), validators.Length(min=2, max=25, message=messageLongueur2_25)])
	categorie = SelectField(u'Categorie', [validators.Required(message=messageObligatoire)], choices=[('Etudiant', 'Etudiant'), ('Enseignant-Chercheur', 'Enseignant-Chercheur'), ('Personnel BIATOS', 'Personnel BIATOS')])
	annee = SelectField(u'Annee', choices=[('', ''), ('Premiere', 'Premiere'), ('Deuxieme', 'Deuxieme'), ('Troisieme', 'Troisieme'), ('Quatrieme', 'Quatrieme'), ('Cinquieme', 'Cinquieme')])
	cycle = SelectField(u'Cycle', choices=[('', ''), ('Premier', 'Premier'), ('Second', 'Second')])
	filiere = SelectField(u'Filiere', choices=[('', ''), ('Filiere Internationale','Filiere Internationale'), ('Filiere Clasique', 'Filiere Clasique'), ('PCE','PCE'), ('FAS','FAS'), ('SHN','SHN')])
	departement = SelectField(u'Departement', choices=[('',''), ('BB', 'BB'), ('BIM', 'BIM'), ('GE', 'GE'), ('GI', 'GI'), ('GCU', 'GCU'), ('GEN', 'GEN'), ('GMC', 'GMC'), ('GMD', 'GMD'), ('GMPP', 'GMPP'), ('IF', 'IF'), ('SGM', 'SGM'), ('TC', 'TC')])
	password = PasswordField(u'Mot de Passe', [
		validators.Required(message=messageObligatoire),
		validators.EqualTo('confirm', message=messagePassword),
		validators.Length(min=4, max=25, message=messageLongueur4_25)
	])
	confirm = PasswordField(u'Confirmez le mot de passe', [validators.Required(message=messageObligatoire)])
	dateNaissance = DateField(u'Ne(e) le', format='%d/%m/%Y',  validators=[validators.Optional()])
	sexe = SelectField(u'Sexe ', choices=[('', ''), ('Masculin', 'Masculin'), ('Feminin', 'Feminin')])
	poids = FloatField(u'Poids (kg)', [validators.Optional(), validators.NumberRange(min=20, max=300, message=messagePoids)])
	hauteur = FloatField(u'Taille (cm)', [validators.Optional(), validators.NumberRange(min=90, max=250, message=messageTaille)])
	position = TextField(u'Position', [validators.Optional(), validators.Length(min=2, max=100,  message=messageLongueur3_100)])
	affiliation = TextField(u'Affiliation', [validators.Optional(), validators.Length(min=2, max=100,  message=messageLongueur3_100)])


def createStudent(form, student):
	student.firstname = form.prenom.data
	student.lastname = form.nom.data
	student.nickname = form.surnom.data
	student.password = hash_password(form.password.data)
	student.email = form.email.data
	if form.sexe.data == '':
		student.sex = 'Inconnu'
	else:
		student.sex = form.sexe.data
	student.category = 'etudiant'
	student.year = 'premiere'#form.annee.data
	student.cycle = form.cycle.data
	if form.cycle.data == 'Premier':
		student.branch = form.filiere.data
	else:
		student.branch = form.departement.data
	student.birthdate = form.dateNaissance.data
	student.weight = form.poids.data
	student.height = form.hauteur.data
	student.etat = "PREREGISTERED"


def createEmployee(form, employee):
	employee.firstname = form.prenom.data
	employee.lastname = form.nom.data
	employee.nickname = form.surnom.data
	employee.password = hash_password(form.password.data)
	employee.email = form.email.data
	if form.sexe.data == '':
		employee.sex = 'Inconnu'
	else:
		employee.sex = form.sexe.data
	employee.birthdate = form.dateNaissance.data
	if form.categorie.data == 'Enseignant-Chercheur':
		employee.category = 'enseignant'
	else:
		employee.category = 'iatos'
	employee.weight = form.poids.data
	employee.height = form.hauteur.data
	employee.etat = "PREREGISTERED"
	employee.affiliation = form.affiliation.data
	employee.position = form.position.data

