# TP Secure chat

## Prise en main

### Type de toplogy du chat : réseau en étoile
### Remarque dans les logs: on voit les messages échangés par les utilisateurs.
### Violation de la confidentialité: se serveur du chat peut voir les messages alors qu'il n'est pas dans les utilisateurs du chat
### Une solution serait de chiffrer les messages de chaque utilisateurs. Les deux utilisateurs échangent un mot de passe qui va venir chiffrer l'échange de mot de passe. Ainsi les messages seront échangés de façon à ce que le serveur ne puisse pas lire en clair.