# TP Secure chat

## Prise en main

### Type de toplogy du chat : réseau en étoile
### Remarque dans les logs: on voit les messages échangés par les utilisateurs.
### Violation de la confidentialité: se serveur du chat peut voir les messages alors qu'il n'est pas dans les utilisateurs du chat
### Une solution serait de chiffrer les messages de chaque utilisateurs. Les deux utilisateurs échangent un mot de passe qui va venir chiffrer l'échange de mot de passe. Ainsi les messages seront échangés de façon à ce que le serveur ne puisse pas lire en clair.

## Chiffrement
## Urandom peut etre un bon choix pour la cryptographie car elle se base sur une source d'entropie, ce qui est suffsant pour générer des nombres aleatoires de grandes qualites. Pour des applications plus sécurisées, on utlisera une bibliothèque dediee au contexte de chiffrement.
## Cependant, si on utilise les primitives, on prend le risque de s'exposer aux failles de securite decouvertes.
## Un serveur malveillant peut encore recolter les données, comme les identifiants et les mots de passe, attaquer par force brute. Il peut aussi intercepter les donnees et les modifier, et meme injecter du code pour prendre le controle des systemes.
## D'après ce que l'on vient d'ennoncer, il nous manque la propriété de l'integrité.

## ASE 
## Avec la methode Fernet, le code est beaucoup plus facile à implementer, on a eu besoin que de 2 lignes de codes pour générer une clé.
## Lorsqu'un serveur vient attaquer avec des faux messages, on appelle l'attaque de  l'homme du milieu (HDM)
## Pour contrer une attaque HDM, on peut utiliser un certificat d'authentification SSL/TLS, qui va donner une preuve que le message vient bien du contact avec qui on veut communiquer, et pas d'un pirate.

## TTL
## Aucune différence n'a ete remarquée avec la précédente classe.
## En soustrayant 45 sec au TTL, le message envoyé est directement mis de côté, le log d'erreur se déclenche directement.
## Si on ne prend qu'un TTL de 30 sec, c'est inefficace. Les pirates on largement le temps de changer le message. Si on prend un temps plus petit, on diminue le risque d'altération des données. 
## Si on prend ce risque, des messages qui ne sont pas altérés déclencheront un log d'erreur parce que le délai de transmission est trop long par rapport au TTL.

## Regard critique
## Dans ce chat, nous avons essayé d'appliquer les propriétés vues en cours, on a chiffré les données pour la confidentialité, on a limité l'altération des données avec la méthode Fernet et par limitation du temps pour décrypter la donnée. Cependant, il nous manque la propriété de tracabilité pour savoir ce qu'il se passe pendant la transmission de données. Il nous manque aussi l'authentification, car dans ce chat, on peut prendre le nom de n'importe quel utilisateur sans qu'on ne vérifie l'identité.
