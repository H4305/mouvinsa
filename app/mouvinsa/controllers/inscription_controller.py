from wtforms import Form, BooleanField, TextField, PasswordField, SelectField, DateField, validators

class InscriptionForm(Form):
	email = TextField(u'Email', [validators.Length(min=6, max=35)])
	surnom = TextField(u'Surnom', [validators.Length(min=4, max=25)])
	nom = TextField(u'Nom', [validators.Length(min=4, max=25)])
	prenom = TextField(u'Prenom', [validators.Length(min=4, max=25)])
	categorie = SelectField(u'Categorie ', choices=[('Etudiant', 'Etudiant'), ('Enseignant-Chercheur', 'Enseignant-Chercheur'), ('Personnel BIATOS', 'Personnel BIATOS')])
	annee = SelectField(u'Annee ', choices=[('', ''), ('Premiere', 'Premiere'), ('Deuxieme', 'Deuxieme'), ('Troisieme', 'Troisieme'), ('Quatrieme', 'Quatrieme'), ('Cinquieme', 'Cinquieme')])
	cycle = SelectField(u'Cycle ', choices=[('', ''), ('Premier', 'Premier'), ('Second', 'Second')])
	branch = SelectField(u'Branch ', choices=[('', ''), ('Eurinsa','Eurinsa'), ('Amerinsa', 'Amerinsa'), ('Classique','Classique'), ('Asinsa','Asinsa'), ('Scan','Scan')])
	password = PasswordField(u'Mot de Passe', [
		validators.Required(),
		validators.EqualTo('confirm', message='Les mots de passe doivent correspondre')
	])
	confirm = PasswordField(u'Repeter le mot de passe')
	dateNaissance = DateField(u'Date de Naissance', format='%d/%m/%Y')
	sexe = SelectField(u'Sexe ', choices=[('', ''), ('Masculin', 'Masculin'), ('Feminin', 'Feminin')])
	poids = TextField(u'Poids')
	hauteur = TextField(u'Hauteur')
	position = TextField(u'Position')
	affiliation = TextField(u'Affiliation')


def createStudent(form, student):
	student.firstname = form.prenom.data
	student.lastname = form.nom.data
	student.nickname = form.surnom.data
	student.password = form.password.data
	student.email = form.email.data
	student.sex = form.sexe.data
	student.category = 'etudiant'
	student.year = form.annee.data
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

