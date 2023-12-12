from teste_de_imagem import teste_de_imagem
import pyautogui as pt
import pandas as pd
from time import sleep
from termcolor import colored


arquivo = (r'C:\Users\vlsilva\Desktop\NOTAS_DIG.txt')
df = pd.read_csv(arquivo, sep="|")

lista_nota = []

contador = int(input("Quantas notas:"))
for _ in range(contador):
    nota = int(input("Informe a nota:"))
    lista_nota.append(nota)

#muda tela
pt.hotkey('alt','tab')
for notas in range(len(lista_nota)):
    if lista_nota[notas] in df['NOTA'].values:
        pt.moveTo(526,264,duration=0.2)
        pt.click()
        pt.typewrite(str(lista_nota[notas]),interval=0.2)
        sleep(0.8)
        pt.hotkey('enter')
        teste_de_imagem()
        sleep(5)
        pt.hotkey('f7')
        sleep(5)
        pt.click(836,243)
        for linha in df[df['NOTA'] == lista_nota[notas]]['QUANTIDADE']:
            linha = str(linha).split("|")
            pt.typewrite(linha[0] + "\n",interval=0.2)
    else:
        print(colored(f"Nota {lista_nota} não encontrada.", color='red'))
    sleep(1.2)
    pt.hotkey('enter')
    sleep(6)
print(colored(f"nota(s) {lista_nota} digitadas com sucesso!", color='green'))
def mensagem():
    pt.alert(f"nota(s) {lista_nota}  digitadas com sucesso!","Mensagem")
mensagem()