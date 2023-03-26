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
## D'apres ce que l'on vient d'ennoncer, il nous manque la propriete de l'integrite.

## ASE 
## Avec la methode Fernet, le code est beaucoup plus facile a implementer, on a eu besoin que de 2 lignes de codes pour generer une cle
## Lorsqu'un serveur vient attaquer avec des faux messages, on appelle l'attaque de  l'homme du milieu (HDM)
## Pour contrer une attaque HDM, on peut utiliser un certificat d'authentification SSL/TLS, qui vont donner une preuve que le message vient bien du contact avec qui on veut communiquer, et pas d'un pirate.

## TTL
## Aucune différence n'a ete remarquee avec la precedente classe.
## En soustrayant 45 sec au TTL, le message envoye est directement mis de cote, le log d'erreur se declenche directement.
## Si on ne prend qu'un TTL de 30 sec, c'est inefficace. Les pirates on largement le temps de changer le message. Si on prend un temps plus petit, on diminue le risque d'alteration des donnees. 
## Si on prend ce risque, des messages qui ne sont pas alteres declencheront un log d'erreur parce que le delai de transmission est trop long par rapport au TTL.

## Regard critique
## Dans ce chat, nous avons essaye d'appliquer les proprietes vues en cours, on a chiffre les donnees pour la confidentialite, on a limite l'alteration des donnees avec la methode Fernet et par limitation du temps pour decrypter la donnee. Cependant, il nous manque la propriete de tracabilite pour savoir ce qu'l se passe pendant la transmission de donnees. Il nous manque aussi l'authentification, car dans ce chat, on peut prendre le nom de n'importe quel utilisateur sans qu'on ne verifie l'identite.
