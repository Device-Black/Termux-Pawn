#!/bin/bash

if [ $# -ne 1 ]; then
  echo "Utilize: "$0" <arquivo.pwn>"
  exit 0
fi

FILE=$1
FILENAME=$(basename $FILE .pwn)

pawncc /sdcard/PawnCC/$FILE -C+ '-;+' '-(+' -O0 -i/sdcard/PawnCC/include -e/sdcard/PawnCC/errors.txt
mv $FILENAME.amx /sdcard/PawnCC 2>/dev/null && echo $FILE "foi compilado com sucesso" || echo "Falha ao tentar compilar" $FILE
