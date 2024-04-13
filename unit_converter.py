import os

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def length_converter_menu():
    while True:
        clear_console()
        print("\033[1;33m" + "=" * 80)
        print(" " * 24 + "📏 CONVERSOR DE COMPRIMENTO 📏")
        print("=" * 80 + "\033[0m")

        print("\033[1;36mSelecione a unidade de origem:")
        print("1. 📏 Metros")
        print("2. 📏 Centímetros")
        print("3. 📏 Pés")
        print("4. 📏 Polegadas")
        print("5. ⬅️ Voltar ao Menu Inicial\033[0m")

        escolha = input("\033[1;35mDigite o número da opção desejada: \033[0m")

        if escolha == '5':
            break
        
        valor = float(input("\033[1;36mDigite o valor: \033[0m"))

        if escolha == '1':
            metros_para_cm = valor * 100
            metros_para_pes = valor * 3.28084
            metros_para_polegadas = valor * 39.3701

            print(f"{valor} metros equivalem a:")
            print(f"{metros_para_cm} centímetros")
            print(f"{metros_para_pes} pés")
            print(f"{metros_para_polegadas} polegadas")

        elif escolha == '2':
            cm_para_metros = valor / 100
            cm_para_pes = valor / 30.48
            cm_para_polegadas = valor / 2.54

            print(f"{valor} centímetros equivalem a:")
            print(f"{cm_para_metros} metros")
            print(f"{cm_para_pes} pés")
            print(f"{cm_para_polegadas} polegadas")

        elif escolha == '3':
            pes_para_metros = valor / 3.28084
            pes_para_cm = valor * 30.48
            pes_para_polegadas = valor * 12

            print(f"{valor} pés equivalem a:")
            print(f"{pes_para_metros} metros")
            print(f"{pes_para_cm} centímetros")
            print(f"{pes_para_polegadas} polegadas")

        elif escolha == '4':
            polegadas_para_metros = valor / 39.3701
            polegadas_para_cm = valor * 2.54
            polegadas_para_pes = valor / 12

            print(f"{valor} polegadas equivalem a:")
            print(f"{polegadas_para_metros} metros")
            print(f"{polegadas_para_cm} centímetros")
            print(f"{polegadas_para_pes} pés")

        input("\033[1;35mPressione Enter para continuar...\033[0m")

def weight_converter_menu():
    while True:
        clear_console()
        print("\033[1;33m" + "=" * 80)
        print(" " * 24 + "⚖️ CONVERSOR DE PESO ⚖️")
        print("=" * 80 + "\033[0m")

        print("\033[1;36mSelecione a unidade de origem:")
        print("1. ⚖️ Quilogramas")
        print("2. ⚖️ Gramas")
        print("3. ⚖️ Libras")
        print("4. ⚖️ Onças")
        print("5. ⬅️ Voltar ao Menu Inicial\033[0m")

        escolha = input("\033[1;35mDigite o número da opção desejada: \033[0m")

        if escolha == '5':
            break
        
        valor = float(input("\033[1;36mDigite o valor: \033[0m"))

        if escolha == '1':
            kg_para_gramas = valor * 1000
            kg_para_libras = valor * 2.20462
            kg_para_oncas = valor * 35.27396

            print(f"{valor} quilogramas equivalem a:")
            print(f"{kg_para_gramas} gramas")
            print(f"{kg_para_libras} libras")
            print(f"{kg_para_oncas} onças")

        elif escolha == '2':
            gramas_para_kg = valor / 1000
            gramas_para_libras = valor / 453.592
            gramas_para_oncas = valor / 28.3495

            print(f"{valor} gramas equivalem a:")
            print(f"{gramas_para_kg} quilogramas")
            print(f"{gramas_para_libras} libras")
            print(f"{gramas_para_oncas} onças")

        elif escolha == '3':
            libras_para_kg = valor / 2.20462
            libras_para_gramas = valor * 453.592
            libras_para_oncas = valor * 16

            print(f"{valor} libras equivalem a:")
            print(f"{libras_para_kg} quilogramas")
            print(f"{libras_para_gramas} gramas")
            print(f"{libras_para_oncas} onças")

        elif escolha == '4':
            oncas_para_kg = valor / 35.27396
            oncas_para_gramas = valor * 28.3495
            oncas_para_libras = valor / 16

            print(f"{valor} onças equivalem a:")
            print(f"{oncas_para_kg} quilogramas")
            print(f"{oncas_para_gramas} gramas")
            print(f"{oncas_para_libras} libras")

        input("\033[1;35mPressione Enter para continuar...\033[0m")

def temperature_converter_menu():
    while True:
        clear_console()
        print("\033[1;33m" + "=" * 80)
        print(" " * 24 + "🌡️ CONVERSOR DE TEMPERATURA 🌡️")
        print("=" * 80 + "\033[0m")

        print("\033[1;36mSelecione a escala de origem:")
        print("1. 🌡️ Celsius")
        print("2. 🌡️ Fahrenheit")
        print("3. 🌡️ Kelvin")
        print("4. ⬅️ Voltar ao Menu Inicial\033[0m")

        escolha = input("\033[1;35mDigite o número da opção desejada: \033[0m")

        if escolha == '4':
            break
        
        valor = float(input("\033[1;36mDigite o valor: \033[0m"))

        if escolha == '1':
            celsius_para_fahrenheit = (valor * 9/5) + 32
            celsius_para_kelvin = valor + 273.15

            print(f"{valor} graus Celsius equivalem a:")
            print(f"{celsius_para_fahrenheit:.2f} graus Fahrenheit")
            print(f"{celsius_para_kelvin:.2f} Kelvin")

        elif escolha == '2':
            fahrenheit_para_celsius = (valor - 32) * 5/9
            fahrenheit_para_kelvin = ((valor - 32) * 5/9) + 273.15

            print(f"{valor} graus Fahrenheit equivalem a:")
            print(f"{fahrenheit_para_celsius:.2f} graus Celsius")
            print(f"{fahrenheit_para_kelvin:.2f} Kelvin")

        elif escolha == '3':
            kelvin_para_celsius = valor - 273.15
            kelvin_para_fahrenheit = ((valor - 273.15) * 9/5) + 32

            print(f"{valor} Kelvin equivalem a:")
            print(f"{kelvin_para_celsius:.2f} graus Celsius")
            print(f"{kelvin_para_fahrenheit:.2f} graus Fahrenheit")

        input("\033[1;35mPressione Enter para continuar...\033[0m")

def unit_converter_menu():
    while True:
        clear_console()

        print("\033[1;33m" + "=" * 80)
        print(" " * 30 + "📐 JAUMNX UNIT CONVERTER 📐")
        print("=" * 80 + "\033[0m")

        print("\033[1;36mSelecione a opção de conversão:")
        print("1. 📏 Comprimento")
        print("2. ⚖️ Peso")
        print("3. 🌡️ Temperatura")
        print("4. ❌ Sair\033[0m")

        escolha = input("\033[1;35mDigite o número da opção desejada: \033[0m")

        if escolha == '4':
            break
        elif escolha == '1':
            length_converter_menu()
        elif escolha == '2':
            weight_converter_menu()
        elif escolha == '3':
            temperature_converter_menu()
        else:
            print("\033[1;31mOpção inválida\033[0m")

        input("\033[1;35mPressione Enter para continuar...\033[0m")
        clear_console()

# Execução do programa
if __name__ == "__main__":
    unit_converter_menu()
