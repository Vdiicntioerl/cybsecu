# TP Secure chat

## Prise en main

### Type de toplogy du chat : réseau en étoile
### Remarque dans les logs: on voit les messages échangés par les utilisateurs.
### Violation de la confidentialité: se serveur du chat peut voir les messages alors qu'il n'est pas dans les utilisateurs du chat
### Une solution serait de chiffrer les messages de chaque utilisateurs. Les deux utilisateurs échangent un mot de passe qui va venir chiffrer l'échange de mot de passe. Ainsi les messages seront échangés de façon à ce que le serveur ne puisse pas lire en clair.

## Chiffrement
## Urandom peut etre un bon choix pour la cryptographie car elle se base sur une source d'entropie, ce qui est suffsant pour générer des nombres aleatoires de grandes qualites. Pour des applications plus sécurisées, on utlisera une bibliotheque dediee au contexte de chiffrement.
## Cependant, si on utilise les primitives, on prend le risque de s'exposer aux failles de securite decouvertes.
## Un serveur malveillant peut encore recolter les donnees, comme les identifiants et les mots de passe, attaquer par force brute. Il peut aussi intercepter les donnees et les modifier, et meme injecter du code pour prendre le controle des systemes.
## D'apres ce qu'on vient d'ennoncer, il nous manque la propriete de l'integrite.

## ASE 
##
