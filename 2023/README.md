# CTF Hackagou 2023 

site : https://ctf2023.hackagou.nc/

1. créer un compte en ajoutant son adresse email 
2. cliquer sur le lien du mail reçu 
3. s'authentifier

site : https://ctf2023.hackagou.nc/challenges


## Askip

code : `79 80 69 78 78 67 123 87 104 52 55 95 49 53 95 52 53 99 49 49 63 33 125`

un nombre peut représenter un lettre comme ... le code ascii (ASKIP)
=> dcode.fr: ASCII CIPHERTEXT Decimal
réponse : `OPENNC{Wh47_15_45c11?!}`


## Julius

code : `BCRAAP{p4rf4e_p1cu3e_15_345l}`

Cf le nom du défi et ce à quoi à ressemble : c'est du code "César"

cela ressemble au flag précédent
* BCRAAP => OPENNC
* N => A
* O => B
=> Alphbet decale +13

réponse : `OPENNC{c4es4r_c1ph3r_15_345y}`

## LostPassword 

### intitulé

> Un pirate, dont on taira le nom, aurait trouvé l'un des trésors cachés de Capt'N Nepo. Il en aurait profiter pour poser un cadenas afin que notre légendaire pirate ne puisse remettre la main sur le fruit de son dur labeur.
>
>Pouvez-vous aider Capt'N Nepo à ouvrir ce cadenas grâce aux indices fournis par un membre de l'équipage du vil pillard ?
> 
> Indices :
>
> * Le mot de passe est composé de 17 caractères.
> * Le pirate est né le 12 mars 1985.
> * Son film préféré est "Pirates des Caraïbes".
> * Il a un chien nommé Massis.
> * Il utilise toujours une combinaison de son année de naissance, du nom de son chien et d'un mot lié à son film préféré.

Les possibilités sont les suivantes, il suffit de tester

* OPENNC{1985MassisPirates}
* OPENNC{Pirates1985Massis}
* OPENNC{MassisPirates1985}
* OPENNC{1985PiratesMassis}
* OPENNC{Massis1985Pirates} => success
* OPENNC{PiratesMassis1985}
 
## Morsure

code : 
```
--- .--. . -. -. -.-. -.--. -- ----- .-. ... ...-- ..--.- -.-. ----- -.. ...-- ..--.- .---- ..... ..--.- .-.. .---- ..-. ...-- -.--.-
```

cela ressemble à du morse => dcode.fr

réponse : `OPENNC{M0RS3_C0D3_15_L1F3}`

## PasswordFlood

> * MilleSabords
> * Doublons123
> * ÎleAuTrésor#Secrète
> * Perroquet
> * Carte3D#ÎlesPerdues
> * _tresor
> * butin123
> * 0123456
> * Boussole$77Etoile
> * unPirate
> * longueVue
> * Capitaine#Intrépide2023
> * 3Iles
> * CoffreFort#Rempli$
> * taverne
> * 7Mers
> * TrésorCaché#2023
> * epee

* MilleSabords
* Doublons123
* Perroquet
* _tresor
* butin123
* 0123456
* unPirate
* longueVue
* 3Iles
* taverne
* 7Mers
* epee

Les essais : 

* OPENNC{MDPb0ul3t7e} => failed
* OPENNC{MP0te} => failed
* OPENNC{0te} => failed
* OPENNC{MP_b0ul3t7e} => failed 
* OPENNC{MP_b0ul3te} => failed
* OPENNC{MDP_b0ul3t7e} => success


## Sicstifort 

code : `T1BFTk5De0I0NTM2NF8xNV9uMDdfQ3JZUDcwfQ==`

cela ressemble à du base64 (sixtyfour)

```
echo T1BFTk5De0I0NTM2NF8xNV9uMDdfQ3JZUDcwfQ== | base64 -d 
OPENNC{B45364_15_n07_CrYP70}
```

## sponsor

Quels sont les sponsors  ? 
=> liste selection unique 


## st4ff

Par quelle organisation a été créé le HacKagou ?
=> liste selection unique


## Espion

```
curl -A "007" http://challs.hackagou.nc:5004
```


## Burryit 

fichier à telecharger : buryit

```
file buryit
buryit: gzip compressed data, last modified: Wed Nov 30 10:21:40 2022, max compression, original size modulo 2^32 81178
mv buryit{,gz}
gzip -d buryit.gz
file buryit
buryit: gzip compressed data, last modified: Wed Nov 30 10:21:40 2022, max compression, original size modulo 2^32 81296
mv buryit{,gz}
gzip -d buryit.gz
file buryit
buryit: XZ compressed data, checksum CRC64
```

il faut faire un script ; 

```
cd burryit
bash buryit.sh
......buryit: ASCII text
unzip 2001 times => OPENNC{D4n5_L4_C4P174L3}

```

## Dé&Ness


deness est un fichier pcapng que l'on peut lire avec `tcpdump -r deness.pcapng` ou avec `wireshark deness.pcapng`
L'ensemble des questions/réponses "DNS" nous donne le code ci-dessous qui ressemble `q du base64  

```
tcpdump -qns 0 -A -r  2023/deness/deetness.pcapng 2>&1 | grep -v "IP 172\|reading" | sed -e "s#^.*\([A-Za-z=0-9]\)\.com.*#\1#" | xargs  | sed "s/ //g"
T1BFTk5De0RuU18wYmZVNWM0NzEwbnf0=
```

code : `T1BFTk5De0RuU18wYmZVNWM0NzEwbnf0=`

```
echo T1BFTk5De0RuU18wYmZVNWM0NzEwbn0= | base64 -d 
OPENNC{DnS_0bfU5c4710n}
```


## UnitedOrCity

*codage Manchester* : 
propose une inversion du signal systématique au milieu de la période d'horloge, ce qui garantit l'impossibilité d'avoir un signal continue. Pour transmettre un 1, il s'agira d'un front montant, et pour transmettre un 0, d'un front descendant. 
Le code peut être inversé suivnat l'usage 
ref : 
* www.guill.net
* https://fr.wikipedia.org/wiki/Codage_Manchester

De l'image signal.png, il ressort le code suivant 

* code         : `10110001100110101000111111001111`
* code inverse : `01001110011001010111000000110000`

Utilisation d'un outil en ligne pour convertir du binaire en text.
Appliqué au code inversé, nous donne  `Nep0`

Le md5 de ce dernier résultat, nous donne la valeur du flag 

```
t=$(echo -n Nep0| md5sum| awk  '{print $1}'); echo "OPENNC{$t}"
```


## Goalcausse

retrouver une rue depuis une photo

1. identifier la tour Q1 gold coast via google image
2. via google street trouver l'angle
3. retrouver une impasse via la trajectoire

réponse : `OPENNC{SunriseBoulevard}`


## Hiddn


* linkedin capt'n nemo
* contact info => url site web => blog 

### Le blog

le seul article du blog : https://openntpac.wordpress.com/2023/04/09/tresor-cache-a-la-station-n/
Nous donne des informations sur le lieu et sur une date relative

En allant sur la page `about ME` on découvre l'adresse email

### EPIOS

L'outil EPIOS nous permet de retrouver tout ce qui est publique dans google pour une adresse email 

On y retrouve un avis dans google maps
=> google map + avis (entre cyclone judy et kevin => 03/03/2023)

Le blog indique que le tresor a été decouvert la veille et donc est entéré le 04/03/2023 à la station n

réponse : `OPENNC{04032023_stationn}`



## RizVerse

code : 160 172 104 107 106 70 104 20 70 126 81 20 85 106 106 81 20 126 81 106 70 106 104 85 106 169 106 117 162 122 113 113 120 119 118

le script qui a généré le code indique qu'on appelle 3 fonctions  : 

```
print(fun3(fun2(fun1(flag))))
```

En s'appuyant sur le script, il faut donc faire l'inverse

```
a="160 172 104 107 106 70 104 20 70 126 81 20 85 106 106 81 20 126 81 106 70 106 104 85 106 169 106 117 162 122 113 113 120 119 118

la = a.split(" ")
print(la)
lb = []
for i in la:
    lb.append(int(i))
b = fun3(lb)
print(type(b))

```

L'exécution du script nous donne ceci : 

réponse : `OPENNC{R3v3r53_3nG1n33r1nG_15_345y}`



## 3x1f

aperisolv 

=> Zteg commentaire : OPENNC{M374d474_4r3_345Y_70_R34d}

## Ellesbe

aperisolv

superimposed : OPENNC{57eGan0_0bfU5c4710n}

## Singeblase 

recherche google

```
t=$(echo -n 0.05ETH| md5sum| awk  '{print $1}'); echo "OPENNC{$t}"
```



