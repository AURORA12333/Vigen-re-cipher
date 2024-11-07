alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def keycode(s):
    for i in range(len(alphabet)):
        if s == alphabet[i]:
            return i
    return 0

def encode(text, key):
    code = ""
    for i in range(len(text)):
        code += alphabet[(keycode(text[i]) + keycode(key[i % len(key)])) % len(alphabet)]
    return code

def decode(text, key):
    code = ""
    for i in range(len(text)):
        code += alphabet[(keycode(text[i]) - keycode(key[i % len(key)]) + len(alphabet)) % len(alphabet)]
    return code

def main():
    choice = input("Введите 1 для шифрования или 2 для дешифрования: ")
    
    if choice not in ['1', '2']:
        print("Введено неверное значение")
        return
    
    text = input("Введите текст: ").upper()
    key = input("Введите ключ: ").upper()
    
    if choice == '1':
        print("Зашифрованное сообщение:", encode(text, key))
    elif choice == '2':
        print("Расшифрованное сообщение:", decode(text, key))
    
    
    input("Нажмите Enter, чтобы выйти...")

if __name__ == "__main__":
    main()