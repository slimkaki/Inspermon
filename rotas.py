#Função para simular "Typing"
import time,sys,random,os,json
def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.01)
def print_sleep(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.1)

#função para vida nas batalhas
clear = lambda: os.system('cls')

#Opções de lugares para ir
os.startfile('rota.mp3')
print_slow("Escolha um lugar para ir:\n")
print_slow("\n- Casa(0)\n"+"\n- Fablab: Recupera seus inspermons(1)\n"+"\n- Grama Alta: Pode encontrar inspermons selvagens(2)\n"+"\n- Lago: Pode encontrar inspermons aquáticos(3)\n"+"\n- Floresta: Pode encontrar inspermons mais fortes(4)\n")

lugar_escolha=int(input("\n"+"-> "))

# LUGARES
if lugar_escolha==1:
    print_slow("\nVocê foi ao FabLab\n")
    print_slow("\nAguarde enquanto seus inspermons são recuperados\n"+". . . . .")
    os.startfile('heal.mp3')
    time.sleep(3)
    os.startfile('rota.mp3')
    print_slow("\nSeus inspermons foram recuperados\n")
    print_slow("\nDeseja ver a insperdex (1)? Caso não, digite qualquer outro número")
    y=int(input("\n-> "))
    if (y==1):
        insperdex=json.loads(open("insperdex.json", encoding='UTF-8').read())
        for x in insperdex:
            print_slow("\n- Nome: "+str(x['nome'])+"\n- Tipo: "+str(x['tipo'])+"\n")
        print_slow("\nPronto para continuar (1)?\n")
        t=int(input("\n-> "))
        if (t==1):
            sys.exit(0)
    else:
        sys.exit(0)

elif lugar_escolha==0:
    print_slow("\nVocê voltou para casa\n")
    os.startfile('rota.mp3')
    time.sleep(3)
    import continua
    clear()

elif lugar_escolha==2:
    print_slow("\nVocê foi andar pela grama alta\n")
    time.sleep(3)
    clear()
    import batalha_inspermon

elif lugar_escolha==3:
    print_slow("\nVocê foi andar pela beira do lago\n")
    time.sleep(3)
    clear()
    import batalha_inspermon
    
elif lugar_escolha==4:
    print_slow("\nVocê foi andar pela floresta\n")
    time.sleep(3)
    clear()
    import batalha_inspermon