#!/bin/bash

# Definir permissoes
chmod +x termux-pawn/*

# Mover a pasta PawnCC
mv termux-pawn/PawnCC /sdcard

# Mover arquivos
mv termux-pawn/libpawnc.so /lib
mv termux-pawn/pawncc /bin
mv termux-pawn/compile.sh $HOME

# Finalizar
rm -rf termux-pawn
echo -e "\nUso: ./compile.sh <arquivo>\n"
