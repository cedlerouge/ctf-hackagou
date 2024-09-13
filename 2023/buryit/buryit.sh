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

