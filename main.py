import os
from time import sleep

def limpar_tela():
    os.system("cls")

def mostrar_opcoes():
    print("=== 🤖 ⚙️  🤖 ⚙️  🤖 ===\n")

    print("\033[35mOlá! Eu sou o ChatBot.\033[0m\n")

    print("1 - Lista de Produtos")
    print("2 - Endereço")
    print("3 - Horário de funcionamento")
    print("4 - Falar com atendente")
    print("5 - Sair")


def mostrar_produto():
    
    print("\n\033[36m=== LISTA DE PRODUTOS ===\033[0m\n")
       
    print("""\033[33m
1 - Notebook Dell Inspiron
2 - Notebook Lenovo IdeaPad
3 - Mouse Gamer Logitech
4 - Mouse Sem Fio Multilaser
5 - Teclado Mecânico Redragon
6 - Teclado Sem Fio Logitech
7 - Monitor LG 24 polegadas
8 - Monitor Samsung 27 polegadas
9 - Headset HyperX Cloud
10 - Webcam Logitech C920
11 - Impressora Epson EcoTank
12 - SSD Kingston 1TB
13 - Pendrive Sandisk 64GB
14 - Cadeira Gamer
15 - Estabilizador
\033[0m""")

def mostrar_endereco():
    print("\033[32mNosso endereço é Rua oratório, 123 - São Paulo.\033[0m")

def mostrar_horario():
    print("Funcionamos de segunda a sexta das 08h às 18h.")

def mostrar_atendente():
    print("Um atendente entrará em contato em breve.")

def sair():
     print("Obrigado por utilizar o ChatBot!")

def op_invalida():
     print("\033[31m❌ OPÇÃO INVÁLIDA ❌\033[0m")

def voltar_menu():
    print("\n\033[94mVoltando ao menu...\033[0m\n")

while True:
    
    sleep(1)
    
    mostrar_opcoes()

    opcao = input("\nEscolha uma opção: ")
    
    if opcao == "1":
        limpar_tela()
        mostrar_produto()
        voltar_menu()
    elif opcao == "2":
        limpar_tela()
        mostrar_endereco()
        voltar_menu()

    elif opcao == "3":
        limpar_tela()
        mostrar_horario()
        voltar_menu()

    elif opcao == "4":
        limpar_tela()
        mostrar_atendente()
        voltar_menu()

    elif opcao == "5":
        limpar_tela()
        sair()
        break
    else: 
       limpar_tela()
       op_invalida()
       voltar_menu()

   