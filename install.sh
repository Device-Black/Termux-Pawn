#!/bin/bash

# Mover a pasta PawnCC
mv $HOME'/termux-pawn/PawnCC' '/sdcard/'

# Definir permissoes
chmod +x $HOME'/termux-pawn/libpawnc.so'
chmod +x $HOME'/termux-pawn/compile.sh'
chmod +x $HOME'/termux-pawn/pawncc'

# Mover arquivos
mv $HOME'/termux-pawn/libpawnc.so' '/lib/'
mv $HOME'/termux-pawn/compile.sh' $HOME
mv $HOME'/termux-pawn/pawncc' '/bin/'

# Exibir comando
echo -e "\nUso: ./compile.sh <arquivo>\n"
