#!/bin/bash

# Criar a pasta PawnCC e include
mkdir '/sdcard/PawnCC' 2>'/dev/null'
mkdir '/sdcard/PawnCC/include' 2>'/dev/null'

# Instalar includes atualizadas
git clone https://github.com/device-black/fix-includes.git
mv 'fix-includes/*' '/sdcard/PawnCC/include'

# Definir permissoes
chmod +x compile.sh && chmod +x *pawn*

# Mover arquivos
mv compile.sh $HOME && mv pawncc '/bin/' && mv libpawnc.so '/lib/'

# Exibir comando
echo -e "\nUso: ./compile.sh <arquivo>\n"
