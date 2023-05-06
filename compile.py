#!/usr/bin/env python3.11

import os, shutil, sys, urllib.request, zipfile

def Baixar_Arquivos():
	url = 'https://github.com/Device-Black/Termux-Pawn/archive/refs/heads/DeviceBlack.zip'
	nome_arquivo = 'termux-pawn.zip'
	
	try:
		print('Baixando "termux-pawn.zip", aguarde...')
		urllib.request.urlretrieve(url, nome_arquivo)
		print('Download concluido!')
	except urllib.error.HTTPError as e:
		print('Erro HTTP:', e.code, url)
	except urllib.error.URLError as e:
		print('Erro de URL:', e.reason, url)
	except Exception as e:
		print('Erro:', e)
	
	if os.path.exists("termux-pawn.zip"):
		return True
	else:
		return False

def Extrair_Arquivos():
	try:
		print('Extraindo "termux-pawn.zip", aguarde...')
		zipfile.ZipFile("termux-pawn.zip", 'r').extractall("./")
		os.remove("termux-pawn.zip")
		print('Extracao concluida!')
	except zipfile.BadZipFile:
		print("Erro ao extrair arquivo ZIP: arquivo invalido.")
	except zipfile.LargeZipFile:
		print("Erro ao extrair arquivo ZIP: arquivo muito grande.")
	except:
		print("Erro ao extrair arquivo ZIP: erro desconhecido.")

	if os.path.exists("Termux-Pawn-DeviceBlack"):
		return True
	else:
		return False

def Mover_Arquivos():
	for raiz, subpastas, arquivos in os.walk("./Termux-Pawn-DeviceBlack"):
		for arquivo in arquivos:
			caminho_arquivo = os.path.join(raiz, arquivo)
			os.chmod(caminho_arquivo, 0o777)
	
	try:
		shutil.move("Termux-Pawn-DeviceBlack", "/backup/")
	except OSError as e:
		print('(A) Erro do sistema operacional:', e)
	except shutil.Error as e:
		print('(B) Erro:', e)
	
	return os.path.exists("/backup/Termux-Pawn-DeviceBlack")

def Instalar_Arquivos():
	if not os.path.exists("/usr/bin/pawncc"):
		try:
			shutil.copy("/backup/Termux-Pawn-DeviceBlack/pawncc", "/usr/bin")
		except OSError as e:
			print('(C) Erro do sistema operacional:', e)
			return False
		except shutil.Error as e:
			print('(D) Erro:', e)
			return False
		
	if not os.path.exists("/usr/bin/libpawnc.so"):
		try:
			shutil.copy("/backup/Termux-Pawn-DeviceBlack/libpawnc.so", "/usr/lib")
		except OSError as e:
			print('(E) Erro do sistema operacional:', e)
			return False
		except shutil.Error as e:
			print('(F) Erro:', e)
			return False
	
	if not os.path.exists("/sdcard/PawnCC"):
		try:
			shutil.copytree("/backup/Termux-Pawn-DeviceBlack/PawnCC", "/sdcard/PawnCC")
		except OSError as e:
			print('(G) Erro do sistema operacional:', e)
			return False
		except shutil.Error as e:
			print('(H) Erro:', e)
			return False
	
	return True

def Verificar_Sistema():
	if not os.path.exists("/backup/Termux-Pawn-DeviceBlack"):
		if not os.path.exists("/backup"):
			os.mkdir("/backup")
	
		if not Baixar_Arquivos():
			sys.exit(1)
		if not Extrair_Arquivos():
			sys.exit(1)
		if not Mover_Arquivos():
			sys.exit(1)
		
		os.system("clear")

	if not (os.path.exists("/usr/bin/pawncc") and os.path.exists("/usr/lib/libpawnc.so") and os.path.exists("/sdcard/PawnCC")):
		if Instalar_Arquivos():
			print("Sucesso ao instalar o compilador")
		else:
			sys.exit(1)

def main():
	Verificar_Sistema()

	if len(sys.argv) < 2:
		print("Autor: github.com/Device-Black")
		print("Utilize: ./compile.py <filename.pwn>")
	else:
		arquivo_pwn = sys.argv[1]
		arquivo_amx = f"{arquivo_pwn[:-3]}amx"
		
		print(f"Compilando o arquivo {arquivo_pwn}...")
		os.system(f"pawncc /sdcard/PawnCC/{arquivo_pwn} -C+ '-;+' '-(+' -e:/sdcard/PawnCC/errors.txt -i:/sdcard/PawnCC/include")
		
		if not os.path.exists(arquivo_amx):
			print(f"Falha ao tentar compilar '{arquivo_pwn}', verifique 'errors.txt'")
		else:
			try:
				os.remove(f"/sdcard/PawnCC/{arquivo_amx}")
				print(f"... gerando um novo arquivo: {arquivo_amx} ...")
			except:
				print(f"... gerando um novo arquivo: {arquivo_amx} ...")
			
			shutil.move(arquivo_amx, "/sdcard/PawnCC")
			print(f"Script '{arquivo_pwn}' compilado com sucesso!")

if __name__ == "__main__":
	main()
