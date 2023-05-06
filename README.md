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
apt install python3.11 -y
curl -O https://raw.githubusercontent.com/Device-Black/Termux-Pawn/DeviceBlack/compile.py
chmod +x compile.py && ./compile.py -V
```

<b>Compilar Gamemode:</b>
```bash
./compile.py new.pwn
```
Dessa forma o termux irá tentar compilar o script “new.pwn” localizado na pasta “/storage/emulated/0/PawnCC”
caso falhe irá gerar um arquivo chamado “errors.txt”.

Caso você encerre o termux e queira abrir novamente, utilize: 
```sh
proot-distro login ubuntu
```

# Observação
<i>Método testado apenas em dispositivos com <b>armeabi-v7a</b> disponível, verifique o seu!<i>
