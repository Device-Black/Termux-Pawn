# Tutorial
<b>Permitir MEMÓRIA EXTERNA</b>
```sh
termux-setup-storage
```

<b>Instalar UBUNTU:</b>
```bash
pkg upgrade -y
pkg install proot-distro -y
proot-distro install ubuntu
proot-distro login ubuntu
```

<b>Instalar PAWN COMPILER:</b>
```bash
apt update -y && apt upgrade -y
apt install git -y
git clone https://github.com/device-black/termux-pawn.git
chmod +x termux-pawn/*pawn*
mv termux-pawn/libpawnc.so /lib/
mv termux-pawn/pawncc /bin/
```

<b>Compilar Gamemode:</b>
```bash
pawncc /sdcard/Download/minhagm.pwn '-C+' '-(+' '-;+' -O0 -i:./include/ -e:./errors.txt
mv arquivo.txt /home/user/documentos/ 2>/dev/null || echo "Falha ao compilar o script."
```
Dessa forma o termux irá tentar compilar o script “minhagm.pwn” localizado na pasta “Downloads”
caso falhe irá gerar um arquivo chamado “errors.txt”.
As includes devem estar na pasta “Downloads/include”.

Caso você encerre o termux e queira abrir novamente, utilize: 
```sh
proot-distro login ubuntu
```
