#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Gros Damien'
SITENAME = 'ePortfolio Gros Damien'
SITEURL = ''

PATH = 'content'
OUTPUT_PATH = 'public'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'fr'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME = 'themes/mon-theme-pelican'
CSS_FILE = 'style.css'

SITUATION = 'Étudiant en BTS SIO option SLAM'

MENU = (
	('#presentation', 'Accueil'),
        ('#mes_competences', 'Mes compétences'),
        ('#realisations', 'Mes contribution / réalisations professionnelles'),
	('#a_propos', 'À Propos'),
	('#bas', 'Contact'),
        )

COMPETENCES = 'Mes compétences'

TITRE_COMPETENCE1 = 'B1.6 : Organiser son développement professionnel'

COMPETENCE1 = (
        'B1.6.1 Mettre en place son environnement d’apprentissage personnel (acquis)',
        'B1.6.3 Gérer son identité professionnelle (en cour d\'acquisition)',
        'B1.6.4 Développer son projet professionnel (acquis)'
        )


TITRE_COMPETENCE2 = 'B1.4 : Travailler en mode projet'

COMPETENCE2 = (
        'B1.4.1 Analyser les objectifs et les modalités d’organisation d’un projet (en cour)',
        'B1.4.2 Planifier les activités (acquis)',
        'B1.4.3 Évaluer les indicateurs de suivi d’un projet et analyser les écarts (en cour)',
        )
        
TITRE_COMPETENCE3 = 'B1.1 : Gérer le patrimoine informatique'

COMPETENCE3 = (
        'B1.1.1 Recenser et identifier les ressources numériques (acquis)',
        'B1.1.2 Exploiter des référentiels, normes et standards adoptés par le prestataire informatique (acquis)'
        )
        
TITRE_COMPETENCE4 = 'B1.2 : Répondre aux incidents et aux demandes d’assistance et d’évolution'

COMPETENCE4 = (
        'B1.2.1 Collecter, suivre et orienter des demandes (acquis)',
        'B1.2.3 Traiter des demandes concernant les applications (acquis)'
        )

        
TITRE_REALISATION = 'Réalisations professionnels'

TEXT_A_PROPOS = (
        'Bonjour, je m\'appelle GROS Damien je suis née en 2003 j\'ai donc 19 ans et je suis actuellement étudiant en BTS SIO au lycée général et technologique Albert Londres à Cusset.',
        'Ce BTS, comporte deux spécialités, une spécialité tournée vers le développement et l\'autre tourné vers le réseau. J\'ai pour ma part choisi la première, Solutions Logicielles et Applications Métiers (SLAM);',
        'La spécialité SLAM nous forme au développement Web (frameworks Symfony et Django / Front-End avec le framework Bootstrap. Mais également au développement d\'application multi-plateformes (JavaFX), d\'applications mobiles Android et sur l\'analyse et l\'administration des bases de données.',
        'Avant cela j\'ai obtenu un BAC STI2D option SIN qui nous a formé à du C++ (Arduino) et à quelques notions de PHP',
	'Dans la vie je m\'intéresse à beaucoup de chose différente, je suis de nature plutôt curieuse mais avant tout j\'aime le volley et les jeux vidéos',
         )
CONTACT = (
        'Mail : Dgros398@protonmail.com',
        'Tél : 06.52.33.18.03',
        'Courrier : 6 Rue de beauséjour,03200 Vichy',
        )

ENTREPRISE = (
        'Lycée général et technologique Albert Londres,',
        'Bd du 8 mai 1945, 03300 Cusset',
        )

LIENS = (
    ('Mission_CV_&_Motivation'),
    ('Mission_découverte_des_metiers'),
    ('gestion_erreur_AP')
    )

# a modifier

