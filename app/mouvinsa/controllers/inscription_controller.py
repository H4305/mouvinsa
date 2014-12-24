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
	password = PasswordField(u'Mot de Passe', [
		validators.Required(),
		validators.EqualTo('confirm', message='Les deux mot de passe doivent correspondre')
	])
	confirm = PasswordField(u'Repeter Mot De Passe')
	dateNaissance = DateField(u'Date de Naissance', format='%d/%m/%Y')
	# sexe				= SelectField(u'Sexe ', choices=[('masculin', u'Masculin'), ('feminin', u'Feminin')])
	sexe = SelectField(u'Sexe ', choices=['Masculin', 'Feminin'])
	poids = TextField(u'Poids', [validators.Length(min=6, max=35)])
	hauteur = TextField(u'Hauteur', [validators.Length(min=6, max=35)])
