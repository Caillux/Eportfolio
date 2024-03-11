Title: gestion de ticket
Date: 2023-03-07 11:00
Modified: 2023-03-07 11:00
Category: Python
Tags: pelican, publishing
Slug: Creation_session_SNCF
Authors: Gros damien
Summary: Test d'une application de gestion de formation et gestions des erreur trouvé par ticket en binôme 
type: SLAM
style: contenu
                    
### Gestion d'une application de création de session de formation de la SNCF

#### Contexte

Réalisation d’un projet de gestion des erreurs en groupe de 2 personnes.

La SNCF emplois des millier de salarié, ces différents salariés doivent pour mener à bien leurs tâche suivre des formations geré par la SNCF elle-même. L'entreprise utilise donc pour cela une application de gestion de formation de ces salariés. Nous avions à résoudre les problèmes liés à la création de session de cette dernière.

![mon image](./themes/mon-theme-pelican/static/images/creation_session/gestion_formation_menu.png) ![mon image](./themes/mon-theme-pelican/static/images/creation_session/gestion_formation_activite.png) 
![mon image](./themes/mon-theme-pelican/static/images/creation_session/gestion_formation_action.png) ![mon image](./themes/mon-theme-pelican/static/images/creation_session/gestion_formation.png) 

Le but de cette mission était d’analyser l'application de gestion de Session de formation afin de trouver les différentes erreurs du programme ou valeur aberrante possible dans la partie création de session de l’application pour ajouter une gestion de ces erreurs. Pour cela il était demandé de créer un ticket par problème de valeur trouver lors des différents tests d’entrée de valeur dans les différents champs de l’application, et de régler et ajouter la gestion de l’erreur sur une branche prévue à la résolution du ticket.

Il a donc fallu dans un premier temps effectuer différents contrôle lors de la phase de travail préparatoire. Cette phase c’est fait en rentrant différentes valeurs aberrante (que l’application aurait dû refuser) dans les différents champs pour repérer les champs qui acceptaient des valeurs aberrantes et ainsi former le ticket conforme au champ et au problème rencontrer

Les tickets crée à partir de la forge logicielle framagit devaient contenir une description détaillé du problème rencontré. afin que la 2ᵉ personne du binôme puisse comprendre et travailler sur le problème à son tour.
A savoir :

- Une description du test effectuer
- une description de l'erreur rencontré 
- un détail sur le/les valeurs qui créaient le/les erreurs 

#### Environnement technologique

- Forge logiciel Framagit (création de ticket, ainsi que des branches associer à ces derniers)
- Langage du programmation python
- Logiciel Geany
- Ordinateur sous GNU/Linux Debian.

#### Compétences mobilisé

Cette mission a demandé la mobilisation des compétences suivantes :

- **B1.1.1 Recenser et identifier les ressources numériques**
- (gestion de resolution des erreur par le biais de communication et de validation de ticket)
- **B1.1.2 Exploiter des référentiels, normes et standards adoptés par le prestataire informatique**
- (Prise en main de l'application terminal et de son language d'écriture (Python) pour traiter la demande et respect du PEP-8)
- **B1.2.1 Collecter, suivre et orienter des demandes**
- (Test des différentes partie de l'applications afin de crée un ticket, orienter la marche à suivre, l'attribuer à son binôme et de suivre sa résolution. )
- **B1.2.3 Traiter des demandes concernant les applications**
- (Traitement des erreurs par la création et l'attribution de ticket en accord avec la demande de gestion des erreur de création de formation)
