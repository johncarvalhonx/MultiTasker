import os

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Erro: divisão por zero"

def calculator_menu():
    while True:
        clear_console()
        
        print("\033[1;33m" + "=" * 80)
        print(" " * 30 + "🧮 JAUMNX CALCULATOR MENU 🧮")
        print("=" * 80 + "\033[0m")
        
        print("\033[1;36mSelecione a operação:")
        print("1. ➕ Adição")
        print("2. ➖ Subtração")
        print("3. ✖️ Multiplicação")
        print("4. ➗ Divisão")
        print("5. ⚡ Potenciação")
        print("6. √ Raiz Quadrada")
        print("7. ⬅️ Voltar ao Menu Inicial\033[0m")
        
        escolha = input("\033[1;35mDigite o número da opção desejada: \033[0m")

        if escolha == '7':
            break

        clear_console()

        if escolha in ['1', '2', '3', '4', '5', '6']:
            try:
                if escolha == '1':
                    print("\033[1;36m" + "=" * 80)
                    print(" " * 29 + "➕ ADIÇÃO")
                    print("=" * 80 + "\033[0m")
                    num1 = float(input("\033[1;35mDigite o primeiro número: \033[0m"))
                    num2 = float(input("\033[1;35mDigite o segundo número: \033[0m"))
                    resultado = add(num1, num2)
                    operacao = "➕"
                elif escolha == '2':
                    print("\033[1;36m" + "=" * 80)
                    print(" " * 26 + "➖ SUBTRAÇÃO")
                    print("=" * 80 + "\033[0m")
                    num1 = float(input("\033[1;35mDigite o primeiro número: \033[0m"))
                    num2 = float(input("\033[1;35mDigite o segundo número: \033[0m"))
                    resultado = subtract(num1, num2)
                    operacao = "➖"
                elif escolha == '3':
                    print("\033[1;36m" + "=" * 80)
                    print(" " * 23 + "✖️ MULTIPLICAÇÃO")
                    print("=" * 80 + "\033[0m")
                    num1 = float(input("\033[1;35mDigite o primeiro número: \033[0m"))
                    num2 = float(input("\033[1;35mDigite o segundo número: \033[0m"))
                    resultado = multiply(num1, num2)
                    operacao = "✖️"
                elif escolha == '4':
                    print("\033[1;36m" + "=" * 80)
                    print(" " * 26 + "➗ DIVISÃO")
                    print("=" * 80 + "\033[0m")
                    num1 = float(input("\033[1;35mDigite o primeiro número: \033[0m"))
                    num2 = float(input("\033[1;35mDigite o segundo número: \033[0m"))
                    resultado = divide(num1, num2)
                    operacao = "➗"
                elif escolha == '5':
                    print("\033[1;36m" + "=" * 80)
                    print(" " * 24 + "⚡ POTENCIAÇÃO")
                    print("=" * 80 + "\033[0m")
                    num1 = float(input("\033[1;35mDigite o número base: \033[0m"))
                    num2 = float(input("\033[1;35mDigite o expoente: \033[0m"))
                    resultado = num1 ** num2
                    operacao = "⚡"
                elif escolha == '6':
                    print("\033[1;36m" + "=" * 80)
                    print(" " * 28 + "√ RAIZ QUADRADA")
                    print("=" * 80 + "\033[0m")
                    num1 = float(input("\033[1;35mDigite o número: \033[0m"))
                    import math
                    resultado = math.sqrt(num1)
                    operacao = "√"
            except ValueError:
                print("\033[1;31mErro: Entrada inválida. Digite um número válido.\033[0m")
                input("\033[1;35mPressione Enter para continuar...\033[0m")
                continue
        else:
            print("\033[1;31mOpção inválida\033[0m")
            input("\033[1;35mPressione Enter para continuar...\033[0m")
            continue
        
        clear_console()
        print("\033[1;33m" + "=" * 80)
        print(" " * 37 + "RESULTADO")
        print("=" * 80 + "\033[0m")
        print(f"   {num1} {operacao} {num2 if escolha in ['1', '2', '3', '4'] else ''} = {resultado}")
        
        input("\033[1;35mPressione Enter para continuar...\033[0m")

        if __name__ == "__main__":
            calculator_menu()
