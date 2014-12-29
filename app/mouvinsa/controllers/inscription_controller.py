from wtforms import Form, BooleanField, TextField, PasswordField, SelectField, DateField, validators

class InscriptionForm(Form):
	email = TextField(u'Email', [validators.Length(min=6, max=35)])
	surnom = TextField(u'Surnom', [validators.Length(min=4, max=25)])
	nom = TextField(u'Nom', [validators.Length(min=4, max=25)])
	prenom = TextField(u'Prenom', [validators.Length(min=4, max=25)])
	# categorie 			= SelectField(u'Categorie ', choices=[('etudiant', u'Etudiant'), ('enseignant', u'Enseignant-Chercheur'), ('personnel', u'Personnel BIATOS')])
	categorie = SelectField(u'Categorie ', choices=['Etudiant', 'Enseignant-Chercheur', 'Personnel BIATOS'])
	# annee 				= SelectField(u'Annee ', choices=[('premiere', u'1'), ('deuxieme', u'2'), ('troisieme', u'3'), ('quatrieme', u'4'), ('cinquieme', u'5')])
	annee = SelectField(u'Annee ', choices=['1', '2', '3', '4', '5'])
	cycle = SelectField(u'Cycle ', choices=['1', '2'])
	branch = SelectField(u'Branch ', choices=['Eurinsa', 'Amerinsa', 'Classique', 'Asinsa', 'Scan'])
	password = PasswordField(u'Mot de Passe', [
		validators.Required(),
		validators.EqualTo('confirm', message='Les deux mot de passe doivent correspondre')
	])
	confirm = PasswordField(u'Repeter Mot De Passe')
	dateNaissance = DateField(u'Date de Naissance', format='%d/%m/%Y')
	sexe = SelectField(u'Sexe ', choices=['Masculin', 'Feminin'])
	poids = TextField(u'Poids')
	hauteur = TextField(u'Hauteur')
