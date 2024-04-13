import os
import shutil
import pyperclip
from misc.vocabulario import translations

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def translate_word(word, source_language, target_language):
    translation = translations.get((source_language, target_language), {}).get(word, word)
    return translation

def translate_text(text, source_language, target_language):
    words = text.split()
    translated_words = [translate_word(word, source_language, target_language) for word in words]
    return ' '.join(translated_words)

def display_languages():
    print("\033[1;36mSelecione o idioma de destino:")
    print("1. 🇺🇸 Inglês")
    print("2. 🇪🇸 Espanhol")
    print("3. 🇫🇷 Francês")
    print("4. 🇰🇷 Coreano")
    print("5. 🇯🇵 Japonês")
    print("6. 🇨🇳 Chinês")
    print("7. ⚙️ Listar Palavras Traduzíveis")
    print("8. ⬅️ Voltar ao Menu Inicial\033[0m")

def display_language_menu(language_name):
    print("\033[1;33m" + "=" * 80)
    print(" " * 33 + f"🌐 TRADUTOR - {language_name} 🌐")
    print("=" * 80 + "\033[0m")

def list_translatable_words():
    clear_console()

    print("\033[1;33m" + "=" * 80)
    print(" " * 33 + "📚 PALAVRAS TRADUZÍVEIS 📚")
    print("=" * 80 + "\033[0m")

    for word in translations.get(('pt', 'en'), {}).keys():
        print(word)

    input("\033[1;35mPressione Enter para continuar...\033[0m")

def translator_menu():
    while True:
        clear_console()

        print("\033[1;33m" + "=" * 80)
        print(" " * 30 + "🌐 JAUMNX TRANSLATOR 🌐")
        print("=" * 80 + "\033[0m")

        display_languages()

        escolha = input("\033[1;35mDigite o número da opção desejada: \033[0m")

        if escolha == '8':
            break

        if escolha == '7':
            list_translatable_words()
            input("\033[1;35mPressione Enter para continuar...\033[0m")
        elif escolha in ['1', '2', '3', '4', '5', '6']:
            clear_console()
            display_language_menu("Inglês" if escolha == '1' else ("Espanhol" if escolha == '2' else ("Francês" if escolha == '3' else ("Coreano" if escolha == '4' else ("Japonês" if escolha == '5' else ("Chinês" if escolha == '6' else 'Português'))))))
            
            text = input("\033[1;35mDigite o texto a ser traduzido: \033[0m")
            clear_console()

            source_language = 'pt'
            target_language = 'en' if escolha == '1' else ('es' if escolha == '2' else ('fr' if escolha == '3' else ('ko' if escolha == '4' else ('ja' if escolha == '5' else ('zh' if escolha == '6' else 'pt')))))

            display_language_menu("Inglês" if escolha == '1' else ("Espanhol" if escolha == '2' else ("Francês" if escolha == '3' else ("Coreano" if escolha == '4' else ("Japonês" if escolha == '5' else ("Chinês" if escolha == '6' else 'Português'))))))
            print("\033[1;36mTexto original:", text, "\033[0m")
            print("=" * 80 + "\033[0m")

            translated_text = translate_text(text, source_language, target_language)
            print("\033[1;36mTradução:", translated_text, "\033[0m")

            while True:
                print("\033[1;36m\nOpções:")
                print("1. Copiar Tradução")
                print("2. Voltar ao Menu de Idiomas")
                print("3. Voltar ao Menu Inicial")
                opcao = input("\033[1;35mDigite o número da opção desejada: \033[0m")

                if opcao == '1':
                    pyperclip.copy(translated_text)
                    print("\033[1;32mTradução copiada para a área de transferência\033[0m")
                elif opcao == '2':
                    break
                elif opcao == '3':
                    return
                else:
                    print("\033[1;31mOpção inválida\033[0m")

            input("\033[1;35mPressione Enter para continuar...\033[0m")
        else:
            print("\033[1;31mOpção inválida\033[0m")
            input("\033[1;35mPressione Enter para continuar...\033[0m")

if __name__ == "__main__":
    translator_menu()
