import time,sys,os
def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.005)
os.startfile('menu.mp3')
print_slow("Bem-vindo ao Inspermon!")
print_slow("\n"+"Deseja iniciar o jogo? 0 para quitar, 1 para iniciar e 2 para continuar jogo salvo: "+"\n")
escolha=int(input("-> "))
if (escolha==1):
	import inspermon
elif (escolha==0):
	print_slow("Até a próxima vez então!")
elif (escolha==2):
	import continua