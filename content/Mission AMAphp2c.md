Title: Mission AMAphp_2c
Date: 2023-12-18 15:00
Modified: 2023-12-18 15:00
Category: Python
Tags: pelican, publishing
Slug: AMAphp_2c
Authors: Gros damien
Summary: Ajout de fonctionnalité par groupe de developpement pour l'application web AMAphp version 2c par la gestion de ticket. 
type: SLAM
style: contenu

### Ajout de fonctionnalité de l'application web AMAphp par groupe de developpement

#### Contexte

Nous étions répartis par groupe (1 de 3 personnes et un autre de 4) pour réaliser deux mission qui avaient pour projet d'aboutir à un ajout de fonctionnalité pour l'application web AMAphp.
Les deux groupes partaient de la même base à savoir la version 2c de l'application (AMAphp_2c) et devaient réaliser 2 mission bien distinct.
> Le 1er groupe (composé de 3 personnes) avait pour mission de Gerer les règlements des contrats et aboutir à une version AMAphp_2c1 de l'application.

> Le 2er groupe (composé de 4 personnes) avait pour mission, la gestion de la saion des paysans et aboutir à une version AMAphp_2c2 de l'application.
je faisais partis du 2e groupe mes mission tournais donc autour de la version AMAphp_2c2.

**Le contexte de la mission était le suivant:**

Les amapiens souhaitent pouvoir ajouter, modifier, supprimer facilement les dates de distribution, qui devront être associées aux contrats. On vous demande de gérer les formulaires nécessaires ainsi qu'une vue récapitulative des distributions à venir et passés.
Même si les dates de distribution hebdomadaires ont souvent lieu le même jour de la semaine : par exemple, tous les lundi, ou mardi, etc, elles devront rester librement éditables pour gérer les cas exceptionnels comme les jours fériés.
Les paysans partenaires souhaitent pouvoir visualiser leurs contrats en cours selon les différentes dates de distribution hebdomadaires. En effet, les contrats n'ayant pas tous la même date de début, l'application ne leur apporte que très peu de visibilité dans leur travail de composition des paniers hebdomadaires.

#### réalisation de la mission

Afin de réaliser la mission nous travaillions sur le dépot framagit, avec un gestion de version à l'aide de git et s'appuyer sur un diagramme des cas d'utilisation pour cahier des charges.
les différents commit devait respecter une logique spécifique puisque nous codions sur une branche spécifique au numéro de notre ticket (ex: ticket-01). Enfin notre code devait respecter les recommandation PSR.

ce projet a necessité le passage de plusieurs étapes :

- Tout d'abord nous avions du faire un travail preparatoire.
en effet un fois nos ticket assigné par le chef de projet nous avions à analyser le code de l'application pour analyser et rédiger la façon dont nous pensions implémenter la solution à l'application ainsi que tout les changement et altération que cela provoquerait.
cela passer également par rédiger l'implémentation des différents test que nous aurions à implémenter.

- Ensuite une fois le ticket rédigé le chef de projet validé ou non l'implémentation prévu de la solution et nous passions à l'implémentgation de la solution.
auquel cas il ne validé pas la solution, il rédigait un commentaire sur le ticket expliquant les changements à effectuer.

- Venait ensuite l'étape ou l'on implémenté la solution, puis le chef de projet validé ou non l'implémentation.

- Si l'implémentation était validée alors le ticket était fermé et un autre nous été attribué.

**Mes missions**

Mes missions consistait à :

- Lister les contrats par date de distribution
    Il a donc fallut modifier la base de donnée pour qu’elle prenne en compte les prochaines dates de distributions. Puis se servir de cette dernière pour récupérer le nombre de contrat en cours pour chaque paysan à la date de distribution visée.
    Crée un lien 'Consultation des contrats par date de distribution' qui mène a une page qui retourne un tableau qui possède autant de colonne que de paysan avec des paniers enregistrés et qui liste le nombre de contrat pour chaque paysan à la date donnée.
    cela passait par :
        - la création d'une classe DAO
        - la création d'une methode dans le controller des contrats de l'application
        - la création d'un template twig qui affiche un tableau avec autant de colonne que de paysans enregistré dans la base, affiche par ligne et dans la colonne du paysan le nombre de contrat pour ce dernier à la date donnée et créer un lien sur le nombre de contrat qui mène à une autre page qui liste les contrats pour le paysan
        - la création des différents tests
        - il a egalement fallut prendre en compte les autorisation d'accès ("admin" ou "user")
- Mise en production

#### Environnement technologique

- pc sous linux (Debian)
- php
- symfony
- framagit (dépot) et git

#### Compétences mobilisé

Cette mission a demandé la mobilisation des compétences suivantes :

- **B1.2.3 Traiter des demandes concernant les applications**
- **B1.4.1 Analyser les objectifs et les modalités d’organisation d’un projet**
- **B1.4.2 Planifier les activités**

