from django import forms
from dos.models import Dos




class DosForm(forms.Form):
    statut_operation_list = (
        ('Effectuee', 'EFFECTUEE'),
        ('En cours', 'EN COURS'),
    )
    reponse = (
        ('oui', 'oui'),
        ('non', 'non'),
    )
    numero_declaration = forms.CharField(max_length=20)
    accuse_reception = forms.ChoiceField(choices=reponse, widget=forms.RadioSelect())
    statut_operation = forms.ChoiceField(widget=forms.RadioSelect(), choices=statut_operation_list)
    declaration_anterieure = forms.ChoiceField(widget=forms.RadioSelect(), choices=reponse)
    date_declaration_initiale = forms.DateField(widget=forms.SelectDateWidget(attrs={'class':'form-control m-input'}))
    heure_declaration_initiale = forms.TimeField(widget=forms.TimeInput(attrs={'class':'form-control m-input'}))
    date_declaration = forms.DateField(widget=forms.SelectDateWidget(attrs={'class':'form-control m-input'}))
    heure_declaration = forms.TimeField(widget=forms.TimeInput(attrs={'class':'form-control m-input'}))

    categorie_declarante = (
        ('Trésor Public', 'Trésor Public'),
        ('Banque Centrale,Banque, établissement financier', 'Banque Centrale,Banque, établissement financier'),
        ('Intermédiaire en opérations de banque', 'Intermédiaire en opérations de banque'),
        ('Service financier de la Poste', 'Service financier de la Poste'),
        ('Etablissement de micro finance', 'Etablissement de micro finance'),
        ('Société d’assurance et de réassurance', 'Société d’assurance et de réassurance'),
        ('Courtier d’assurance et de réassurance', 'Courtier d’assurance et de réassurance'),
        ('Bourse des valeurs mobilières', 'Bourse des valeurs mobilières'),
        ('Organisme assurant les fonctions de Dépositaire central ou de banque de règlement',
         'Organisme assurant les fonctions de Dépositaire central ou de banque de règlement'),
        ('Société de bourse', 'Société de bourse'),
        ('Intermédiaire en opérations de bourse', 'Intermédiaire en opérations de bourse'),
        ('Société de gestion de patrimoine', 'Société de gestion de patrimoine'),
        ('Agence immobilie', 'Agence immobilie''Agence immobilie'),
        ('Societé de transport ou de transfert de fonds', 'Societé de transport ou de transfert de fonds'),
        ('Agence de voyage', 'Agence de voyage'),
        ('Entreprise offrant des services d’investissement', 'Entreprise offrant des services d’investissement'),
        ('Organisme de placement collectif en valeurs mobilières (OPCVM)',
         'Organisme de placement collectif en valeurs mobilières (OPCVM)'),
        ('Société de gestion des OPCVM', 'Société de gestion des OPCVM'),
        ('Changeur manuel', 'Changeur manuel'),
        ('Casino ou établissement de jeux Notaire', 'Casino ou établissement de jeux Notaire'),
        ('avocat ou autres membres des professions juridiques indépendantes',
         'avocat ou autres membres des professions juridiques indépendantes'),
        ('Commissaire aux comptes, expert-comptable ou auditeur externe',
         'Commissaire aux comptes, expert-comptable ou auditeur externe'),
        ('Conseiller fiscal Marchand d’articles de valeur', 'Conseiller fiscal Marchand d’articles de valeur'),
        ('Autre', 'Autre')
    )
    denomination_sociale = forms.CharField(max_length=250, widget=forms.TextInput(attrs={'class':'form-control m-input'}))
    lieu_operation = forms.CharField(max_length=250, widget=forms.TextInput(attrs={'class':'form-control m-input'}))
    categorie_declarante = forms.ChoiceField(choices=categorie_declarante, widget=forms.Select(attrs={'class':'form-control'}))

    type_operation = (
        ('Versement espèces', 'Versement espèces'),
        ('Retrait espèces', 'Retrait espèces'),
        ('Paiement par chèque', 'Paiement par chèque'),
        ('Encaissement chèque', 'Encaissement chèque'),
        ('Virement SWIFT vers l’étranger, Pays', 'Virement SWIFT vers l’étranger, Pays'),
        ('Virement Money Gram, Western Union', 'Virement Money Gram, Western Union'),
        ('Virement au TCHAD', 'Virement au TCHAD'),
        ('Autres', 'Autres')
    )
    piece_declaration = (
        ('Revenus sans raison économique correspondante', 'Revenus sans raison économique correspondante'),
        ('Le client refuse de fournir les informations demandées',
         'Le client refuse de fournir les informations demandées'),
        ('Présentation de faux documents', 'Présentation de faux documents'),
        ('Echange de petites coupures usagées contre des grosses coupures',
         'Echange de petites coupures usagées contre des grosses coupures'),
        ('Compte alimenté exclusivement par des transferts', 'Compte alimenté exclusivement par des transferts'),
        ('Le client est lésé et il refuse de porter plainte', ' Le client est lésé et il refuse de porter plainte'),
        ('Préoccupation excessive du client sur la célérité avec laquelle les opérations seront exécutées',
         'Préoccupation excessive du client sur la célérité avec laquelle les opérations seront exécutées'),
        ('Remboursement anticipé de prêts', 'Remboursement anticipé de prêts'),
        ('Transfert vers un paradis fiscal', 'Transfert vers un paradis fiscal'),
        ('Autre', 'Autre')
    )

    type_infraction = (
        ('Détournement de fonds publics', 'Détournement de fonds publics'),
        ('Vol', 'Vol'),
        ('Escroquerie', 'Escroquerie'),
        ('Fraude fiscale', 'Fraude fiscale'),
        ('Financement du terrorisme', 'Financement du terrorisme'),
        ('Financement de la prolifération des armes', 'Financement de la prolifération des armes'),
        ('Autre', 'Autre')
    )

    date_operation = forms.DateField( widget=forms.SelectDateWidget(empty_label=("Jour", "Mois", "Année"),attrs={'class':'form-control m-input'}))
    heure_operation = forms.TimeField(widget=forms.TimeInput(attrs={'class':'form-control m-input'}))
    date_inscription = forms.DateField( widget=forms.SelectDateWidget(empty_label=("Jour", "Mois", "Année"),attrs={'class':'form-control m-input'}))
    type_operation = forms.ChoiceField(widget=forms.RadioSelect(),choices=type_operation)
    piece_declaration = forms.ChoiceField(widget=forms.RadioSelect(),choices=piece_declaration)
    type_infraction = forms.ChoiceField(widget=forms.RadioSelect(),choices=type_infraction)

    type_compte = (
        ('Personnel', 'Personnel'),
        ('Commercial', 'Commercial'),
        ('Autre', 'Autre')
    )

    statut_compte = (
        ('Actif', 'Actif'),
        ('Inactif', 'Inactif'),
        ('Veilleuse', 'Veilleuse'),
        ('Passé par perte et profit', 'Passé par perte et profit'),
        ('Autre', 'Autre')
    )

    nom_etablissement = forms.CharField(max_length=250, widget=forms.TextInput(attrs={'class':'form-control m-input'}))
    numero_compte = forms.CharField(max_length=250,widget=forms.TextInput(attrs={'class':'form-control m-input'}))
    type_compte = forms.ChoiceField(choices=type_compte, widget=forms.RadioSelect)
    montant = forms.FloatField(widget=forms.NumberInput(attrs={'class':'form-control m-input'}))
    devise = forms.CharField(max_length=10,widget=forms.TextInput(attrs={'class':'form-control m-input'}))
    intitule_compte = forms.CharField(max_length=250,widget=forms.TextInput(attrs={'class':'form-control m-input'}))
    date_ouverture = forms.DateField(widget=forms.SelectDateWidget(attrs={'class':'form-control m-input'}))
    date_fermeture = forms.DateField(widget=forms.SelectDateWidget(attrs={'class':'form-control m-input'}))
    statut_compte = forms.ChoiceField(choices=statut_compte, widget=forms.RadioSelect())

    type_identification = (
        ('Carte identité nationale', 'Carte identité nationale'),
        ('Passeport', 'Passeport'),
        ('Certificat de naissance', 'Certificat de naissance'),
        ('Permis de conduire', 'Permis de conduire'),
        ('Titre de séjour', 'Titre de séjour'),
        ('Pays de citoyenneté', 'Pays de citoyenneté'),
        ('Autre', 'Autre')
    )
    nom_individu = forms.CharField(max_length=250, widget=forms.TextInput(attrs={'class':'form-control m-input'}))
    prenom_individu = forms.CharField(max_length=250,widget=forms.TextInput(attrs={'class':'form-control m-input'}))
    date_naissance_individu = forms.DateField(widget=forms.SelectDateWidget(attrs={'class':'form-control m-input'}))
    numero_telephone_individu = forms.CharField(max_length=50,widget=forms.TextInput(attrs={'class':'form-control m-input'}))
    profession_individu = forms.CharField(max_length=250,widget=forms.TextInput(attrs={'class':'form-control m-input'}))
    identification_individu = forms.ChoiceField(choices=type_identification,widget=forms.RadioSelect)

    nom_beneficiaire = forms.CharField(max_length=250,widget=forms.TextInput(attrs={'class':'form-control m-input'}))
    prenom_beneficiaire = forms.CharField(max_length=250,widget=forms.TextInput(attrs={'class':'form-control m-input'}))
    date_naissance_beneficiaire = forms.DateField(widget=forms.SelectDateWidget(attrs={'class':'form-control m-input'}))
    numero_telephone_beneficiaire = forms.CharField(max_length=50,widget=forms.TextInput(attrs={'class':'form-control m-input'}))
    profession_beneficiaire = forms.CharField(max_length=250,widget=forms.TextInput(attrs={'class':'form-control m-input'}))
    identification_beneficiaire = forms.ChoiceField(choices=type_identification,widget=forms.RadioSelect)

    description_action = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control m-input m-input--air'}))
    description_mesure = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control m-input m-input--air'}))
    relation = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control m-input m-input--air'}))

    class Meta:
        # Provide an association between the ModelForm and a model
        model = Dos


class FormStepOne(forms.Form):
    statut_operation_list = (
        ('Effectuee', 'EFFECTUEE'),
        ('En cours', 'EN COURS'),
    )
    reponse=(
        ('oui','oui'),
        ('non','non'),
    )
    numero_declaration = forms.CharField(max_length=20)
    accuse_reception = forms.ChoiceField(widget=forms.RadioSelect, choices=reponse)
    statut_operation = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,choices=statut_operation_list)
    declaration_anterieure = forms.ChoiceField(widget=forms.RadioSelect, choices=reponse)
    date_declaration_initiale = forms.DateField(widget=forms.SelectDateWidget())
    heure_declaration_initiale = forms.TimeField(widget=forms.TimeInput())
    date_declaration = forms.DateField(widget=forms.SelectDateWidget())
    heure_dclaration = forms.TimeField(widget=forms.TimeInput())

class FormStepTwo(forms.Form):
    categorie_declarante = (
        ('Trésor Public', 'Trésor Public'),
        ('Banque Centrale,Banque, établissement financier', 'Banque Centrale,Banque, établissement financier'),
        ('Intermédiaire en opérations de banque', 'Intermédiaire en opérations de banque'),
        ('Service financier de la Poste', 'Service financier de la Poste'),
        ('Etablissement de micro finance', 'Etablissement de micro finance'),
        ('Société d’assurance et de réassurance', 'Société d’assurance et de réassurance'),
        ('Courtier d’assurance et de réassurance', 'Courtier d’assurance et de réassurance'),
        ('Bourse des valeurs mobilières', 'Bourse des valeurs mobilières'),
        ('Organisme assurant les fonctions de Dépositaire central ou de banque de règlement',
         'Organisme assurant les fonctions de Dépositaire central ou de banque de règlement'),
        ('Société de bourse', 'Société de bourse'),
        ('Intermédiaire en opérations de bourse', 'Intermédiaire en opérations de bourse'),
        ('Société de gestion de patrimoine', 'Société de gestion de patrimoine'),
        ('Agence immobilie', 'Agence immobilie''Agence immobilie'),
        ('Societé de transport ou de transfert de fonds', 'Societé de transport ou de transfert de fonds'),
        ('Agence de voyage', 'Agence de voyage'),
        ('Entreprise offrant des services d’investissement', 'Entreprise offrant des services d’investissement'),
        ('Organisme de placement collectif en valeurs mobilières (OPCVM)',
         'Organisme de placement collectif en valeurs mobilières (OPCVM)'),
        ('Société de gestion des OPCVM', 'Société de gestion des OPCVM'),
        ('Changeur manuel', 'Changeur manuel'),
        ('Casino ou établissement de jeux Notaire', 'Casino ou établissement de jeux Notaire'),
        ('avocat ou autres membres des professions juridiques indépendantes',
         'avocat ou autres membres des professions juridiques indépendantes'),
        ('Commissaire aux comptes, expert-comptable ou auditeur externe',
         'Commissaire aux comptes, expert-comptable ou auditeur externe'),
        ('Conseiller fiscal Marchand d’articles de valeur', 'Conseiller fiscal Marchand d’articles de valeur'),
        ('Autre', 'Autre')
    )
    denomination_sociale = forms.CharField(max_length=250)
    lieu_operation = forms.CharField(max_length=250)
    categorie_declarante = forms.ChoiceField( choices=categorie_declarante)

class FormStepThree(forms.Form):
        type_operation = (
            ('Versement espèces', 'Versement espèces'),
            ('Retrait espèces', 'Retrait espèces'),
            ('Paiement par chèque', 'Paiement par chèque'),
            ('Encaissement chèque', 'Encaissement chèque'),
            ('Virement SWIFT vers l’étranger, Pays', 'Virement SWIFT vers l’étranger, Pays'),
            ('Virement Money Gram, Western Union', 'Virement Money Gram, Western Union'),
            ('Virement au TCHAD', 'Virement au TCHAD'),
            ('Autres', 'Autres')
        )
        piece_declaration = (
            ('Revenus sans raison économique correspondante', 'Revenus sans raison économique correspondante'),
            ('Le client refuse de fournir les informations demandées',
             'Le client refuse de fournir les informations demandées'),
            ('Présentation de faux documents', 'Présentation de faux documents'),
            ('Echange de petites coupures usagées contre des grosses coupures',
             'Echange de petites coupures usagées contre des grosses coupures'),
            ('Compte alimenté exclusivement par des transferts', 'Compte alimenté exclusivement par des transferts'),
            ('Le client est lésé et il refuse de porter plainte', ' Le client est lésé et il refuse de porter plainte'),
            ('Préoccupation excessive du client sur la célérité avec laquelle les opérations seront exécutées',
             'Préoccupation excessive du client sur la célérité avec laquelle les opérations seront exécutées'),
            ('Remboursement anticipé de prêts', 'Remboursement anticipé de prêts'),
            ('Transfert vers un paradis fiscal', 'Transfert vers un paradis fiscal'),
            ('Autre', 'Autre')
        )

        type_infraction = (
            ('Détournement de fonds publics', 'Détournement de fonds publics'),
            ('Vol', 'Vol'),
            ('Escroquerie', 'Escroquerie'),
            ('Fraude fiscale', 'Fraude fiscale'),
            ('Financement du terrorisme', 'Financement du terrorisme'),
            ('Financement de la prolifération des armes', 'Financement de la prolifération des armes'),
            ('Autre', 'Autre')
        )
        
        date_operation = forms.DateField(widget=forms.SelectDateWidget())
        heure_operation = forms.TimeField()
        date_inscription = forms.DateField(widget=forms.SelectDateWidget())
        type_operation = forms.ChoiceField( choices=type_operation)
        piece_declaration = forms.ChoiceField (choices=piece_declaration)
        type_infraction = forms.ChoiceField ( choices=type_infraction)
    


class FormStepFour(forms.Form):
        type_compte = (
            ('Personnel', 'Personnel'),
            ('Commercial', 'Commercial'),
            ('Autre', 'Autre')
        )

        statut_compte = (
            ('Actif', 'Actif'),
            ('Inactif', 'Inactif'),
            ('Veilleuse', 'Veilleuse'),
            ('Passé par perte et profit', 'Passé par perte et profit'),
            ('Autre', 'Autre')
        )

        nom_etablissement = forms.CharField(max_length=250)
        numero_compte = forms.CharField(max_length=250)
        type_compte = forms.ChoiceField( choices=type_compte)
        montant = forms.FloatField()
        devise = forms.CharField(max_length=10)
        intitule_compte = forms.CharField(max_length=250)
        date_ouverture = forms.DateField(widget=forms.SelectDateWidget())
        date_fermeture = forms.DateField(widget=forms.SelectDateWidget())
        statut_compte = forms.ChoiceField( choices=statut_compte)

class FormStepFive(forms.Form):
        type_identification = (
            ('Carte identité nationale', 'Carte identité nationale'),
            ('Passeport', 'Passeport'),
            ('Certificat de naissance', 'Certificat de naissance'),
            ('Permis de conduire', 'Permis de conduire'),
            ('Titre de séjour', 'Titre de séjour'),
            ('Pays de citoyenneté', 'Pays de citoyenneté'),
            ('Autre', 'Autre')
        )
        nom_individu = forms.CharField(max_length=250)
        prenom_individu = forms.CharField(max_length=250)
        date_naissance_individu = forms.DateField(widget=forms.SelectDateWidget())
        numero_telephone_individu = forms.CharField(max_length=50)
        profession_individu = forms.CharField(max_length=250)
        identification_individu = forms.ChoiceField( choices=type_identification)

        nom_beneficiaire = forms.CharField(max_length=250)
        prenom_beneficiaire = forms.CharField(max_length=250)
        date_naissance_beneficiaire = forms.DateField(widget=forms.SelectDateWidget())
        numero_telephone_beneficiaire = forms.CharField(max_length=50)
        profession_beneficiaire = forms.CharField(max_length=250)
        identification_beneficiaire = forms.ChoiceField ( choices=type_identification)

class FormStepSix(forms.Form):
            description_action = forms.CharField(widget=forms.Textarea)
            description_mesure = forms.CharField(widget=forms.Textarea)


