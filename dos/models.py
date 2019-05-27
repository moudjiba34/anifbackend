from django.db import models

# Create your models here.

class Dos(models.Model):

    statut_operation=(
        ('Effectuee','EFFECTUEE'),
        ('En cours','EN COURS'),
    )
    categorie_declarante=(
        ( 'Trésor Public','Trésor Public'),
        ('Banque Centrale' 'Banque, établissement financier','Banque Centrale' 'Banque, établissement financier'),
        ('Intermédiaire en opérations de banque','Intermédiaire en opérations de banque'),
        ('Service financier de la Poste','Service financier de la Poste'),
        ('Etablissement de micro finance','Etablissement de micro finance'),
        ('Société d’assurance et de réassurance','Société d’assurance et de réassurance'),
        ('Courtier d’assurance et de réassurance','Courtier d’assurance et de réassurance'),
        ('Bourse des valeurs mobilières','Bourse des valeurs mobilières'),
        ('Organisme assurant les fonctions de Dépositaire central ou de banque de règlement', 'Organisme assurant les fonctions de Dépositaire central ou de banque de règlement'),
        ('Société de bourse','Société de bourse'),
        ('Intermédiaire en opérations de bourse','Intermédiaire en opérations de bourse'),
        ('Société de gestion de patrimoine','Société de gestion de patrimoine'),
        ('Agence immobilie','Agence immobilie''Agence immobilie'),
        ('Societé de transport ou de transfert de fonds','Societé de transport ou de transfert de fonds'),
        ('Agence de voyage','Agence de voyage'),
        ('Entreprise offrant des services d’investissement','Entreprise offrant des services d’investissement'),
        ('Organisme de placement collectif en valeurs mobilières (OPCVM)','Organisme de placement collectif en valeurs mobilières (OPCVM)'),
        ('Société de gestion des OPCVM','Société de gestion des OPCVM'),
        ('Changeur manuel','Changeur manuel'),
        ('Casino ou établissement de jeux Notaire','Casino ou établissement de jeux Notaire'),
        ('avocat ou autres membres des professions juridiques indépendantes','avocat ou autres membres des professions juridiques indépendantes'),
        ('Commissaire aux comptes, expert-comptable ou auditeur externe','Commissaire aux comptes, expert-comptable ou auditeur externe'),
        ('Conseiller fiscal Marchand d’articles de valeur','Conseiller fiscal Marchand d’articles de valeur'),
        ('Autre','Autre')
    )

    type_operation=(
        ('Versement espèces','Versement espèces'),
        ('Retrait espèces','Retrait espèces'),
        ('Paiement par chèque','Paiement par chèque'),
        ('Encaissement chèque','Encaissement chèque'),
        ('Virement SWIFT vers l’étranger, Pays', 'Virement SWIFT vers l’étranger, Pays'),
        ('Virement Money Gram, Western Union','Virement Money Gram, Western Union'),
        ('Virement au TCHAD', 'Virement au TCHAD'),
        ('Autres', 'Autres')
    )
    piece_declaration=(
        ('Revenus sans raison économique correspondante','Revenus sans raison économique correspondante'),
        ('Le client refuse de fournir les informations demandées','Le client refuse de fournir les informations demandées'),
        ('Présentation de faux documents', 'Présentation de faux documents'),
        ('Echange de petites coupures usagées contre des grosses coupures','Echange de petites coupures usagées contre des grosses coupures'),
        ('Compte alimenté exclusivement par des transferts','Compte alimenté exclusivement par des transferts'),
        ('Le client est lésé et il refuse de porter plainte',' Le client est lésé et il refuse de porter plainte'),
        ('Préoccupation excessive du client sur la célérité avec laquelle les opérations seront exécutées','Préoccupation excessive du client sur la célérité avec laquelle les opérations seront exécutées'),
        ('Remboursement anticipé de prêts','Remboursement anticipé de prêts'),
        ('Transfert vers un paradis fiscal','Transfert vers un paradis fiscal'),
        ('Autre','Autre')
    )

    type_infraction=(
        ('Détournement de fonds publics','Détournement de fonds publics'),
        ('Vol','Vol'),
        ('Escroquerie','Escroquerie'),
        ('Fraude fiscale','Fraude fiscale'),
        ('Financement du terrorisme','Financement du terrorisme'),
        ('Financement de la prolifération des armes','Financement de la prolifération des armes'),
        ('Autre', 'Autre')
    )
    type_compte=(
        ('Personnel','Personnel'),
        ('Commercial','Commercial'),
        ('Autre','Autre')
    )

    statut_compte=(
        ('Actif','Actif'),
        ('Inactif','Inactif'),
        ('Veilleuse','Veilleuse'),
        ('Passé par perte et profit','Passé par perte et profit'),
        ('Autre', 'Autre')
    )

    type_identification=(
        ('Carte identité nationale','Carte identité nationale'),
        ('Passeport','Passeport'),
        ('Certificat de naissance','Certificat de naissance'),
        ('Permis de conduire','Permis de conduire'),
        ('Titre de séjour','Titre de séjour'),
        ('Pays de citoyenneté','Pays de citoyenneté'),
        ('Autre', 'Autre')
    )

    numero_declaration=models.CharField(max_length=20)
    accuse_reception=models.BooleanField(default=False)
    statut_operation=models.CharField(max_length=10, choices=statut_operation)
    declaration_anterieure=models.BooleanField(default=False)
    date_declaration_initiale=models.DateField()
    heure_declaration_initiale=models.TimeField()
    date_declaration=models.DateField(auto_now_add=True)
    heure_declaration=models.TimeField(auto_now_add=True)

    denomination_sociale=models.CharField(max_length=250)
    lieu_operation=models.CharField(max_length=250)
    categorie_declarante=models.CharField(max_length=250, choices=categorie_declarante)
    date_operation=models.DateField()
    heure_operation=models.TimeField()
    date_inscription=models.DateField()
    type_operation=models.CharField(max_length=250, choices=type_operation)
    piece_declaration=models.CharField(max_length=250, choices=piece_declaration)
    type_infraction=models.CharField(max_length=250, choices=type_infraction)
    nom_etablissement=models.CharField(max_length=250)
    numero_compte=models.CharField(max_length=250)
    type_compte=models.CharField(max_length=250, choices=type_compte)
    montant=models.FloatField()
    devise=models.CharField(max_length=10)
    intitule_compte=models.CharField(max_length=250)
    date_ouverture=models.DateField()
    date_fermeture=models.DateField()
    statut_compte=models.CharField(max_length=250,choices=statut_compte)

    #identification personnelle
    nom_individu=models.CharField(max_length=250)
    prenom_individu=models.CharField(max_length=250)
    date_naissance_individu=models.DateField()
    numero_telephone_individu=models.CharField(max_length=50)
    profession_individu=models.CharField(max_length=250)
    identification_individu=models.CharField(max_length=250, choices=type_identification)

    # identification beneficiaire
    nom_beneficiaire = models.CharField(max_length=250)
    prenom_beneficiaire = models.CharField(max_length=250)
    date_naissance_beneficiaire = models.DateField()
    numero_telephone_beneficiaire = models.CharField(max_length=50)
    profession_beneficiaire = models.CharField(max_length=250)
    identification_beneficiaire = models.CharField(max_length=250, choices=type_identification)

    description_action=models.TextField(max_length=1000)
    description_mesure=models.TextField(max_length=1000)
    relation = models.TextField(max_length=1000)







