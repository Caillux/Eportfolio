Title: Stage_Axis
Date: 2023-06-26 17:00
Modified: 2023-06-26 17:00 17:00
Category: Python
Tags: pelican, publishing
Slug: Axis_solution
Authors: Gros damien
Summary: Mission durant le stage de fin de première année du BTS SIO, dans l'entreprise Axis Solution
type: SLAM
style: contenu

#### Contexte 
La societer Axis est certifier Qualiopi. cette certification vise à attester la qualité du processus de formation. Le fonctionnement interne était avec des tableaux de suivi 
Excel. Le but du developpement était d'amelioré le fonctionnement mais aussi le suivi de formation afin de ne pas oublier de document. De plus il avait aussi pour but de 
génerer des documents automatiques afin de faire gagner du temps en termes de fonctionnement.

Le developpement devait être implémenter pour une version du logiciel de gestion de l'entreprise Axilta. Pour cela à partir d'un clone du projet Axilta'2 je devait prévoir
et implémenter un bouton "formation" dans le menu "vente" de l'application qui ouvrirai une fenêtre qui permettra de lister les formations avec comme informations :
- un Libellé
- le Client
- le type de formation
- la date de la formation
- l'Etat (fini ou en cours)
- le répertoire de la formation
et ou il serait possible de filtrer la liste des formation par libellé date ou etat.
l'Interface devait disposer également de bouton "ajouter", "modifier", "supprimer". Le double clic sur une formation executerai le meme fonctionnement que le bouton "modifier"
et le bouton "supprimer" afficherai un pop-up de confirmation qui permmettra la suppression de la ligne selectionnée.

Axilta'2 :
![image](./theme/images/stage_axis/Axilta2_menu.PNG)

à partir de cette fentre de formation on devait pouvoir acceder à 
**La fiche de formaion**
qui devait contenir :
- le Libellé 
- le Client
- La date de formation 
- Le type de formation
- Champ "Terminer" pour l'etat de la formation

**Dans les parmaètre de données de base** 

**Formation type**
Une interface qui permettrai de lister, ajouter, modifier, supprimer les types de formations
les type de formation était:
- Gestactiv'2
- Axilta'2

**Type de chronologie**
Une interface qui permettraitde lister, ajouter, modifier, supprimer un type de chronologie
un chronologie devai être constitué de :
- Un libellé (ex : Devis, Formation)
- d'un répertoire(ex : 1-Devis, 3-Formation)
- d'un ordre d'affichage (ex : Ordre, 3)

![image](./theme/images/stage_axis/ex_type_chrono.jpg)

Pour chaque type de formation il devait être posible de renseigner 1 ou plusieur document composé de :
- un Libellé (255 caratere, champ obligatoire)
- Une description
- un type de chronologie
- Un ordre d'affichage
- Un modèle Word
- Docume,t global à la socièter ou par Interlocuteur (Géneration ou ajout du doc)
- de l'envoyer et reçu

Pour chaque formation il devait être possible de sélectionner 1 ou plusieurs interlocuteurs du client(sociéter) et l'interface devait permettre l'ajout de nouveaux 
interlocuteurs sur la fiche client de la formation
Depuis la fiche formation il devait être possible de génerer les documents et les sauvegarder dans le répertoire souhaité
pour chaque document il fallait pouvoir renseigner 
- la date
- la date de reçu
- le chemin d'envoi (le doc envoyer)
- chemin reçu (le doc reçu)
- chemin email d'nvoi (l'email d'envoi)
- chemin d'email reçu (lo'email de reçu)
- la validation

suite à l'analyse de l'application à l'aide de l'IDE WinDev et des différente table de donnée de la base à l'aide 
du logiciel Microsoft SQL server management studio 18 et Azure Data Studio
il était necessaire de crée 5 nouvelles Tables
- Formation
- Formation_type
- formation_doc
- Type_chronologie
- formation_doc_client

en relation avec des tables deja existante dans la base de donnée (ex TABLE : DocumentWord / TABLE : client)
qui serviront à la création d'une fenêtre de gestion de formations qui les listera et permettra la modification de 
ces dernieres

en amont de la créaton de ces tables un diagramme CMD ou UML devait être crée expliquant les dependances entre les
table existantes et les nouvelles 

![image](./theme/images/stage_axis/shema_dependances.PNG)

**Programation**  
Une fois la shéma CMD Validé par le chef de projet et les Tables crées je suis passé à l'implémentation de la fonctionnalité 
Toujour sur le logiciel WinDev, la programation sur ce logiciel peut etre en francais ou en anglais 
pour le logiciel Axilta'2 le code était en francais  

rajouter l'aspect de recherche (language nouveau, site utilisé etx)





#### envirronnement technologique
- clone du logiciel Axilta'2
- IDE windev
- Windows
- base de donnée MYSQL
- windows azure

#### Compétences mobilisés
- recherche approfondis de la doc ou de forum spécialisé dev pour trouvé des solutions 
- projet avec une vision logistich clair avec chef de projet
- Etude de code existant et modification ou utilisation pour faire de nouvelle fonctionnalité
- gestion de bug
- test
