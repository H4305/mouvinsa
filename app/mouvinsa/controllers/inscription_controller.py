from wtforms import Form, BooleanField, TextField, FloatField, PasswordField, SelectField, DateField, validators

class InscriptionForm(Form):
	email = TextField(u'Email', [validators.Required(), validators.EqualTo('Confirmez votre email', message='Les 2 emails doivent correspondre'), validators.Length(min=6, max=35)])
	confirmEmail = TextField(u'Confirmez votre email', [validators.Required(), validators.Length(min=6, max=35)])
	surnom = TextField(u'Pseudonyme', [validators.Required(), validators.Length(min=2, max=25)])
	nom = TextField(u'Nom', [validators.Optional(), validators.Length(min=2, max=25)])
	prenom = TextField(u'Prenom', [validators.Optional(), validators.Length(min=2, max=25)])
	categorie = SelectField(u'Categorie ', [validators.Required()], choices=[('Etudiant', 'Etudiant'), ('Enseignant-Chercheur', 'Enseignant-Chercheur'), ('Personnel BIATOS', 'Personnel BIATOS')])
	annee = SelectField(u'Annee ', choices=[('', ''), ('Premiere', 'Premiere'), ('Deuxieme', 'Deuxieme'), ('Troisieme', 'Troisieme'), ('Quatrieme', 'Quatrieme'), ('Cinquieme', 'Cinquieme')])
	cycle = SelectField(u'Cycle ', choices=[('', ''), ('Premier', 'Premier'), ('Second', 'Second')])
	filiere = SelectField(u'Filiere ', choices=[('', ''), ('Filiere Internationale','Filiere Internationale'), ('Filiere Clasique', 'Filiere Clasique'), ('PCE','PCE'), ('FAS','FAS'), ('SHN','SHN')])
	departement = SelectField(u'Departement', choices=[('',''), ('BB', 'BB'), ('BIM', 'BIM'), ('GE', 'GE'), ('GI', 'GI'), ('GCU', 'GCU'), ('GEN', 'GEN'), ('GMC', 'GMC'), ('GMD', 'GMD'), ('GMPP', 'GMPP'), ('IF', 'IF'), ('SGM', 'SGM'), ('TC', 'TC')])
	password = PasswordField(u'Mot de Passe', [
		validators.Required(),
		validators.EqualTo('Confirmez votre mot de passe', message='Les 2 mots de passe doivent correspondre')
	])
	confirm = PasswordField(u'Confirmez votre mot de passe', [validators.Required()])
	dateNaissance = DateField(u'Ne(e) le', format='%d/%m/%Y',  validators=[validators.Optional()])
	sexe = SelectField(u'Sexe ', choices=[('', ''), ('Masculin', 'Masculin'), ('Feminin', 'Feminin')])
	poids = FloatField(u'Poids (kg)', [validators.Optional()])
	hauteur = FloatField(u'Taille (cm)', [validators.Optional()])
	position = TextField(u'Position', [validators.Optional(), validators.Length(min=3, max=100)])
	affiliation = TextField(u'Affiliation', [validators.Optional(), validators.Length(min=3, max=100)])


def createStudent(form, student):
	student.firstname = form.prenom.data
	student.lastname = form.nom.data
	student.nickname = form.surnom.data
	student.password = form.password.data
	student.email = form.email.data
	student.sex = form.sexe.data
	student.category = 'etudiant'
	student.year = form.annee.data
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
	employee.lastname = form.categorie.data
	employee.nickname = form.surnom.data
	employee.password = form.password.data
	employee.birthdate = form.dateNaissance.data
	employee.email = form.email.data
	employee.sex = form.sexe.data
	if form.categorie.data == 'Enseignant-Chercheur':
		employee.category = 'enseignant'
	else:
		employee.category = 'iatos'

	employee.weight = form.poids.data
	employee.height = form.hauteur.data
	employee.etat = "PREREGISTERED"

