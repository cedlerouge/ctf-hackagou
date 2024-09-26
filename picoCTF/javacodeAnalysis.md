## Java Code Analysis

* Un site affiche des livre en PDF, 
* 3 roles pour 3 livres
* le flag est dans le pdf du role admin 
* On a accès au code source du site 
* On peut y voir que l'accès est condition du bon role (Admin) et du bon id utilisateur (2)
* On accede au livre avec token JWT. 
* le token est chiffré via une clé qui se trouve dans un fichier secret_key.txt, s'il existe, sinon la clé est `1234`
* Il faut donc modifier les informations du token jwt récupéré via l'usage du compte `user` via [jwt.io](http://jwt.io)
  - role 
  - id 
  - clé de chiffrement
* et faire la requête vers le bon livre avec la commande curl : 

```
TOKEN=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJyb2xlIjoiQWRtaW4iLCJpc3MiOiJib29rc2hlbGYiLCJleHAiOjE3Mjc5MDYxMDUsImlhdCI6MTcyNzMwMTMwNSwidXNlcklkIjoyLCJlbWFpbCI6ImFkbWluIn0.5dptOqeZm1TFhAPAAJj1X9aVC5_ifbcyIPgeVCAlm-c
curl -L -H "Authorization: Bearer $TOKEN" http://saturn.picoctf.net:59108/base/books/pdf/5
```

Le contenu de la requête contient un flag `picoctf{}`
