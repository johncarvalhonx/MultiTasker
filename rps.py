import os
import random

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def rps_menu():
    while True:
        clear_console()
        print("\033[1;33m" + "=" * 80)
        print(" " * 26 + "🪨JAUMNX ROCK-PAPER-SCISSORS GAME✂️")
        print("=" * 80 + "\033[0m")

        print("\033[1;36mSelecione uma opção:")
        print("1. 🪨 Pedra, 📄 Papel, ✂️ Tesoura")
        print("2. ❌ Sair\033[0m")

        opcao_rps_menu = input("\033[1;35mDigite o número da opção desejada: \033[0m")

        if opcao_rps_menu == '1':
            play_rps()
        elif opcao_rps_menu == '2':
            break
        else:
            print("\033[1;31mOpção inválida\033[0m")
            input("\033[1;35mPressione Enter para continuar...\033[0m")

def play_rps():
    clear_console()
    print("\033[1;33m" + "=" * 80)
    print(" " * 30 + "🪨JAUMNX ROCK-PAPER-SCISSORS GAME✂️")
    print("=" * 80 + "\033[0m")

    print("Escolha uma opção:")
    print("1. 🪨 Pedra")
    print("2. 📄 Papel")
    print("3. ✂️ Tesoura")

    user_choice = input("\033[1;35mDigite o número da sua escolha: \033[0m")

    if user_choice not in ["1", "2", "3"]:
        print("\033[1;31mEscolha inválida. Por favor, escolha uma opção válida.\033[0m")
        input("\033[1;35mPressione Enter para continuar...\033[0m")
        return

    user_choice_text = "Pedra" if user_choice == "1" else "Papel" if user_choice == "2" else "Tesoura"
    computer_choice_text = get_computer_choice()

    clear_console()
    print("\033[1;33m" + "=" * 80)
    print(" " * 30 + "JAUMNX ROCK-PAPER-SCISSORS GAME")
    print("=" * 80 + "\033[0m")

    print(f"Você escolheu: {user_choice_text}")
    print(f"Computador escolheu: {computer_choice_text}")

    result = determine_winner(user_choice_text, computer_choice_text)
    print(result)

    if "perdeu" in result:
        input("\033[1;31mPressione Enter para voltar ao Menu Principal...\033[0m")
    else:
        input("\033[1;35mPressione Enter para continuar...\033[0m")

def get_computer_choice():
    return random.choice(["Pedra", "Papel", "Tesoura"])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "\033[1;33mEmpate!\033[0m"
    elif (user_choice == "Pedra" and computer_choice == "Tesoura") or \
         (user_choice == "Papel" and computer_choice == "Pedra") or \
         (user_choice == "Tesoura" and computer_choice == "Papel"):
        return "\033[1;32mVocê venceu!\033[0m"
    else:
        return "\033[1;31mVocê perdeu!\033[0m"

if __name__ == "__main__":
    rps_menu()
