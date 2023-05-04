#!/bin/bash

# Mover a pasta PawnCC
mv 'termux-pawn/PawnCC' '/sdcard/'

# Definir permissoes
chmod +x 'termux-pawn/libpawnc.so'
chmod +x 'termux-pawn/compile.sh'
chmod +x 'termux-pawn/pawncc'

# Mover arquivos
mv 'termux-pawn/libpawnc.so' '/lib/'
mv 'termux-pawn/compile.sh' './'
mv 'termux-pawn/pawncc' '/bin/'

# Exibir comando
echo -e "\nUso: ./compile.sh <arquivo>\n"