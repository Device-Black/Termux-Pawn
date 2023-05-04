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
.compile.sh minhagm.pwn
```
Dessa forma o termux irá tentar compilar o script “minhagm.pwn” localizado na pasta “/storage/emulated/0/PawnCC”
caso falhe irá gerar um arquivo chamado “errors.txt”.

Caso você encerre o termux e queira abrir novamente, utilize: 
```sh
proot-distro login ubuntu
```
