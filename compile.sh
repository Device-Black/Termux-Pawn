#!/bin/bash

# Verifica se um arquivo foi passado como argumento
if [ $# -ne 1 ]; then
  echo -e "\nUso: $0 <arquivo>\n"
  exit 1
fi

# Extrai o nome do arquivo
arquivo=$1
nome_arquivo=$(basename $arquivo .pwn)

# Extrai o nome do arquivo
arquivo=$1
nome_arquivo=$(basename $arquivo .pwn)

# Compila o arquivo usando o comando pawncc
pawncc '/sdcard/PawnCC/'$arquivo '-C+' '-(+' '-;+' '-O0' '-i/sdcard/PawnCC/include' '-e/sdcard/PawnCC/errors.txt'

# Move o arquivo compilado para o diretório /home/user/compilados
mv $HOME'/'$nome_arquivo'.amx' '/sdcard/PawnCC' 2>'/dev/null' && echo -e "\nSucesso ao tentar compilar o script '"$arquivo"'\n" || echo -e "\nFalha ao tentar compilar o script '"$arquivo"'\n" 
