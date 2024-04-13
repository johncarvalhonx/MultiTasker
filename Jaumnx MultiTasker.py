import os
import calculator
import translator
import unit_converter
import rps

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def about_creator():
    clear_console()
    print("\033[1;33m" + "=" * 80)
    print(" " * 30 + "SOBRE O CRIADOR")
    print("=" * 80 + "\033[0m")
    print("Criador: Jaumnx")
    print("Data de Criação: 09 de agosto de 2023")
    print("Copyright © 2023 Jaumnx. Todos os direitos reservados.")
    input("\033[1;35mPressione Enter para voltar ao Menu Inicial...\033[0m")


while True:
    clear_console()

    print("\033[1;33m" + "=" * 80)
    print(" " * 30 + "📝 JAUMNX MULTITASKER 📝")
    print("=" * 80 + "\033[0m")

    print("\033[1;36mSelecione uma opção:")
    print("1. 🧮 Calculadora")
    print("2. 🌐 Tradutor")
    print("3. 📐 Conversor de Unidades")
    print("4. 🪨 Pedra, 📄 Papel, ✂️ Tesoura")
    print("5. ℹ️ Sobre o Criador")
    print("6. ❌ Sair\033[0m")

    opcao_menu_inicial = input("\033[1;35mDigite o número da opção desejada: \033[0m")

    if opcao_menu_inicial == '1':
        calculator.calculator_menu()
    elif opcao_menu_inicial == '2':
        translator.translator_menu()
    elif opcao_menu_inicial == '3':
        unit_converter.unit_converter_menu()
    elif opcao_menu_inicial == '4':
        rps.rps_menu()
    elif opcao_menu_inicial == '5':
        about_creator()
    elif opcao_menu_inicial == '6':
        break
    else:
        print("\033[1;31mOpção inválida\033[0m")
        input("\033[1;35mPressione Enter para continuar...\033[0m")