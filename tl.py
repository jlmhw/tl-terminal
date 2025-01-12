import sys
import os
from translate import Translator

def clear_screen():
    """Clear the terminal screen."""
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def translate_text(text, src, dest):
    """Translate text from source to destination language."""
    try:
        translator = Translator(from_lang=src, to_lang=dest)
        translation = translator.translate(text)
        return translation
    except Exception as e:
        raise RuntimeError(f"Translation failed: {e}")

def main():
    clear_screen()
    print('To end the conversation just press: Ctrl+C')
    print('Maximum character limit per input is 500 chars. Be careful.')
    desrc = input("Write the default language and which one you want to translate to. [i.g.: en;es]: ")
    if ';' not in desrc:
        print("Error: --desrc should contain a ';' separator.")
        sys.exit(1)
    src, dest = desrc.split(';')
    print("-" * 40)
    while True:
        try:
            text = input("[USER]: ")
            translation = translate_text(text, src, dest)
            print(f"[TL]: {translation}")
            print("-" * 40)
        except KeyboardInterrupt:
            os.system('clear')
            break
        except RuntimeError as e:
            os.system('clear')
            break

if __name__ == "__main__":
    main()