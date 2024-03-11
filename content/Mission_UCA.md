Title: Mission_UCA
Date: 2024-03-10 15:00
Modified: 2024-03-10 15:00
Category: Python
Tags: pelican, publishing
Slug: stage_uca
Authors: Gros damien
Summary: Mission durant le stage de deuxième année dans l'Univérsité de L'UCA (Univérsité Clermont Auvergne)
type: SLAM
style: contenu

### Stage de 2er année à Univérsité Clermont Auvergne (UCA)

#### L'organisme d'acceuil

Dans le cadre de notre formation de BTS SIO nous avions un stage de 6 semaines en entreprise durant la période du 8 janvier 2024 au vendredi 16 février 2024 (inclus)
j'ai effectuer mon stage dans l'Univérsité Clermont Auvergne (UCA), dans le département de la DSI.
l'équipe de la DSI était composé d'une dizaine de personnes 
Le departement s'occupe de différence application en lien avec l'ENT et les outils de l'univérsité (ENT, cour en ligne, noodle, ressource des cours, app de gestion d'accès dans certain batiment, etc...)

#### Contexte 

J'ai été affecter au menu d'acceuil de l'ENT
le design du site internet de l'univérsité ayant fait l'objet d'une refonte graphique il a été juger interréssant de modifier l'ENT pour coller à la nouvelle charte graphique de l'UCA
l'ENT a donc fait l'objet d'une refonte integrale que ce soit du design et du fonctionnement (nom de domaine etc...)
lors de mon stage ce nouveaux menu était en phase de test et ouvert une certaine population (utilisateur avec comme role "personnel")

![image](./themes/mon-theme-pelican/static/images/stage_uca/maquette_web.png)
![image](./themes/mon-theme-pelican/static/images/stage_uca/current_dashboard.png)

**l'application**
l'ENT est une application web sous PHP5 symfony7
Elle implémente du JS et execute des reqête Ajax à la base de donnée ainsi que Bootstrap et du SCSS pour tout ce qui est CSS est responsivité.
pour les classe Model elle implémente des classes ORM avec l'utilisation de doctrine.

**organisation de l'équipe**
chaque personne s'occupe d'un type d'application en principal (ex: administratif, etc...)
Tout le monde aà au moins 1 jour de télétravail ils utilisent donc teams

ma mission consistait principalement à l'implémentation de widget raccourcis dans le nouveaux menu de l'application avec plusieurs tickets gerer sur notion.org

![image](./themes/mon-theme-pelican/static/images/stage_uca/notions.png)
![image](./themes/mon-theme-pelican/static/images/stage_uca/notions2.png)

j'ai eu plusieurs tickets correspondant au tâches suivante :
- implémentation widget_shortcut :
    Ajout d'un widget de raccourcis avec la possibilité de selectionner 6 shortcuts à l'aide d'un bouton (+) qui ouvre modal ou l'on selectionne parmis tout les menus possible de l'ENT et ou il est possible de les reorganiser
    ![image](./themes/mon-theme-pelican/static/images/stage_uca/shortcut/menu_customization.png)
    ![image](./themes/mon-theme-pelican/static/images/stage_uca/shortcut/customization-shortcuts_modal.png)
    cette mission à demandé l'apprentissage et l'utilisation de Bootstrap pour le rendu du template twig, de JS pour la reorganisation des menus dans le widget à partir du modal et de doctrine pour la récuperation et la construction des objets menus

- Modification Widget_email:
    Modification du widget email déjà présent qui affichait les mails non lu pour permettre à l'utilisateur de pouvoir choisir entre "afficher tous les emails non lus" ou "afficher les email non lus du jour" ainsi que l'affichage ou non du titre du derniers message non lu
    
    ![image](./themes/mon-theme-pelican/static/images/stage_uca/email/menu_widget_email.png)
    
    la messagerie et la recuperation des message de l'ENT s'appuie sur l'API Zimbra (messagerie et calendrier) montrer ci-dessous. Il a donc été necessaire d'apprendre le fonctionnement de l'API en recherchant à tratillon car la documentation est pratiquement innexistante
    
    ![image](./themes/mon-theme-pelican/static/images/stage_uca/email/apizimbra.png)

    Pour cela une API de test zimbra a été mise en place.

    ![image](./themes/mon-theme-pelican/static/images/stage_uca/email/apizimbra_test.png)

- Traduction de l'application en englais
    Traduction de l'application en englais par le biais de la fonctionnalité translation native à symfony.
    Cette mission était à l'origine le 2eme ticket assigné cependant il a été mit en pause car n'etant pas la priorité sur les autres missions et étant bloquer a un stade particulier par manque de connaissance de ma part et une contrainte technique lié a l'application (nom de domaine et routes), mon maître de stage étant assez occuper la mission prenais plus de temps que ce qu'il était necessaire.

    ![image](./themes/mon-theme-pelican/static/images/stage_uca/translation/menu-en.png)
    ![image](./themes/mon-theme-pelican/static/images/stage_uca/translation/email.twig-translation.png) 


**Programation**  

#### envirronnement technologique

- pc sous Linux (Ubuntu)*
- Teams et Rocket (communication au sein de l'entreprise)
- Notion (la gestion des tickets assigné et le journal de bord)
- API Zimbra (gestion de la messagerie et calendrier)
- PHP version 5
- Symphony version 7
- JS et Ajax
- Classe ORM Doctrine

#### Compétences mobilisés

- **B1.2.3 Traiter des demandes concernant les applications**
- **B1.4.1 Analyser les objectifs et les modalités d’organisation d’un projet**
- **B1.4.2 Planifier les activités**
