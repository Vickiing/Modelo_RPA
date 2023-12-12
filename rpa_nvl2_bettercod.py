from teste_de_imagem import teste_de_imagem
import pyautogui as pt
import pandas as pd
from time import sleep
from termcolor import colored

#mover para a próxima tela
def switch_to_next_screen():
    pt.hotkey('alt', 'tab')

# Função para digitar uma nota da lista
def type_nota(nota):
    pt.moveTo(526, 264, duration=0.2)
    pt.click()
    pt.typewrite(str(nota), interval=0.2)
    sleep(0.8)
    pt.hotkey('enter')

def run_teste_de_imagem():
    teste_de_imagem()

def press_f7():
    pt.hotkey('f7')

def click_position(x, y):
    pt.click(x, y)

def type_linha(linha):
    linha = str(linha).split("|")
    pt.typewrite(linha[0] + "\n", interval=0.2)

def show_success_message(notas):
    pt.alert(f"nota(s) {notas} digitadas com sucesso!", "Mensagem")

arquivo = r'C:\Users\vlsilva\Desktop\NOTAS_DIG.txt'

df = pd.read_csv(arquivo, sep="|")

# Lista para armazenar as notas
lista_nota = []

# Obtenção do número de notas a serem digitadas
contador = int(input("Quantas notas:"))

# Loop para obter as notas do usuário
for _ in range(contador):
    nota = int(input("Informe a nota:"))
    lista_nota.append(nota)

# Alterna para a próxima tela
switch_to_next_screen()

#processando cada nota
for notas in range(len(lista_nota)):
    if lista_nota[notas] in df['NOTA'].values:
        # Digita a nota na tela ativa
        type_nota(lista_nota[notas])
        sleep(0.8)
        pt.hotkey('enter')
        
        run_teste_de_imagem()
        sleep(5)
        press_f7()
        sleep(5)
        click_position(836, 243)
        
        # Digita cada linha correspondente à nota
        for linha in df[df['NOTA'] == lista_nota[notas]]['QUANTIDADE']:
            type_linha(linha)
    else:
        print(colored(f"Nota {lista_nota} não encontrada.", color='red'))
    
    sleep(1.2)
    pt.hotkey('enter')
    sleep(6)

show_success_message(lista_nota)
