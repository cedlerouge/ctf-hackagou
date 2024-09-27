nc -w 2 mimas.picoctf.net 55107 < original.jpg
nc mimas.picoctf.net 59807# Blast From The Past

Le challenge est de modifier toutes les dates des meta-données exif d'une photo image. 

Il faut remplacer par la date suivante : 1970:01:01 00:00:00.001

Il faut faire attention car certaines dates sont facilement modifiables comme : 
* date de creation 
* date de modification 
* date original

Il faut également modifier les `Sub Sec Time` en les passant à `001`

```
exiftool -overwrite_original -createdate="1970:01:01 00:00:00.001Z" -modifydate="1970:01:01 00:00:00.001Z" -FileModifydate="1970:01:01 00:00:00.001Z" -SubSecTime=001 -datetimeoriginal="1970:01:01 00:00:00.001Z" -SubSecTimeOriginal=001 -SubSecTimeDigitized=001  ~/Downloads/original.jpg
```


Et il reste une date cachée que l'on retrouve via la commande `exiftool -ee  ~/Downloads/original.jpg  | grep Time`

On peut retrouver ce champ avec la commande `strings ~/Downloads/original.jpg | grep UTC`

Par contre pour la modifier il faut utiliser `hexedit ~/Downloads/original.jpg` puis la touche TAB pour passer en ASCII, rechercher via la touche `/` le mot `UTC`, repasser en hex via la touche TAB et remplacer 

```
- 74 61  31 37 30 30  35 31 33 31  38 31 34 32
+ 74 61  30 30 30 30  31 00 00 00  00 00 00 00
```

CTRL+X 

```
nc -w 2 mimas.picoctf.net 58868 <  ~/Downloads/original.jpg
nc mimas.picoctf.net 59606


D5 of your picture:
4b34e5904b55a0ff20029af28204a9a5  test.out

Checking tag 1/7
Looking at IFD0: ModifyDate
Looking for '1970:01:01 00:00:00'
Found: 1970:01:01 00:00:00
Great job, you got that one!

Checking tag 2/7
Looking at ExifIFD: DateTimeOriginal
Looking for '1970:01:01 00:00:00'
Found: 1970:01:01 00:00:00
Great job, you got that one!

Checking tag 3/7
Looking at ExifIFD: CreateDate
Looking for '1970:01:01 00:00:00'
Found: 1970:01:01 00:00:00
Great job, you got that one!

Checking tag 4/7
Looking at Composite: SubSecCreateDate
Looking for '1970:01:01 00:00:00.001'
Found: 1970:01:01 00:00:00.001
Great job, you got that one!

Checking tag 5/7
Looking at Composite: SubSecDateTimeOriginal
Looking for '1970:01:01 00:00:00.001'
Found: 1970:01:01 00:00:00.001
Great job, you got that one!

Checking tag 6/7
Looking at Composite: SubSecModifyDate
Looking for '1970:01:01 00:00:00.001'
Found: 1970:01:01 00:00:00.001
Great job, you got that one!

Checking tag 7/7
Timezones do not have to match, as long as it's the equivalent time.
Looking at Samsung: TimeStamp
Looking for '1970:01:01 00:00:00.001+00:00'
Found: 1970:01:01 00:00:00.001+00:00
Great job, you got that one!

You did it!
```

