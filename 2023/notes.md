## Askip

code : `79 80 69 78 78 67 123 87 104 52 55 95 49 53 95 52 53 99 49 49 63 33 125`

un nombre peut représenter un lettre comme ... le code ascii (ASKIP)
=> dcode.fr: ASCII CIPHERTEXT Decimal 
réponse : `OPENNC{Wh47_15_45c11?!}` 


## Julius

code : `BCRAAP{p4rf4e_p1cu3e_15_345l}`
Cf le nom du défi et ce à quoi à ressemble : c'est du code "César"

cela ressemble au flg précédent 
BCRAAP => OPENNC 
N => A
O => B
Alphbet decale +13

réponse : `OPENNC{c4es4r_c1ph3r_15_345y}`

## LostPassword 

OPENNC{1985MassisPirates}
OPENNC{Pirates1985Massis}
OPENNC{MassisPirates1985}
OPENNC{1985PiratesMassis}
OPENNC{Massis1985Pirates} => success
OPENNC{PiratesMassis1985}
 
## Morsure

code : 
```
--- .--. . -. -. -.-. -.--. -- ----- .-. ... ...-- ..--.- -.-. ----- -.. ...-- ..--.- .---- ..... ..--.- .-.. .---- ..-. ...-- -.--.-
```

cela ressemble à du morse => dcode.fr

réponse : `OPENNC{M0RS3_C0D3_15_L1F3}`

## PasswordFlood

* MilleSabords
* Doublons123
* ÎleAuTrésor#Secrète
* Perroquet
* Carte3D#ÎlesPerdues
* _tresor
* butin123
* 0123456
* Boussole$77Etoile
* unPirate
* longueVue
* Capitaine#Intrépide2023
* 3Iles
* CoffreFort#Rempli$
* taverne
* 7Mers
* TrésorCaché#2023
* epee

MilleSabords
Doublons123
Perroquet
butin123
0123456
unPirate
longueVue
3Iles
taverne
7Mers
epee

OPENNC{MDPb0ul3t7e} => failed
OPENNC{MP0te} => failed
OPENNC{0te} => failed
OPENNC{MP_b0ul3t7e} => failed 
OPENNC{MP_b0ul3te} => failed
OPENNC{MDP_b0ul3t7e} => success


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
cat > buryit.sh <<EOF
#!/bin/bash 

incr=0
ret=0
while [ $ret -eq 0 ];
#while [ $incr -lt 5 ]
do
  if [ -f buryit ]; then
    ext=$(file buryit | awk '{print tolower($2)}') 
    if [ $ext == "gzip" ]; then 
      mv buryit buryit.gz
      gzip -d buryit.gz
    elif [ $ext == "xz" ]; then
      mv buryit buryit.xz
      xz -d buryit.xz
    fi
  fi
  file buryit | grep "compressed" > /dev/null 2>&1
  ret=$?
  incr=$((incr+1))
  #file buryit
  echo -n .
done 
file buryit
echo -n "unzip $incr times => "
cat buryit
EOF

bash buryit.sh
......buryit: ASCII text
unzip 2001 times => OPENNC{D4n5_L4_C4P174L3}

```

## Dé&Ness


deness est un fichier pcapng que l'on peut lire avec `tcpdump -r deness.pcapng` ou avec `wireshark deness.pcapng`
L'ensemble des questions/réponses "DNS" nous donne le code ci-dessous qui ressemble `q du base64  
code : T1BFTk5De0RuU18wYmZVNWM0NzEwbnf0=

```
echo T1BFTk5De0RuU18wYmZVNWM0NzEwbn0= | base64 -d 
OPENNC{DnS_0bfU5c4710n}
```


## UnitedOrCity

codage Manchester : 
propose une inversion du signal systématique au milieu de la période d'horloge, ce qui garantit l'impossibilité d'avoir un signal continue. Pour transmettre un 1, il s'agira d'un front montant, et pour transmettre un 0, d'un front descendant
ref : 
* www.guill.net
* https://fr.wikipedia.org/wiki/Codage_Manchester

code : 10110001100110101000111111001111

1011 0001 1001 1010 1000 1111 1100 1111
29 79 69 65 91
