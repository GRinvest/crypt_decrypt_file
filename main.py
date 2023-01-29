from cryptography.fernet import Fernet


def write_key():
    # Создаем ключ и сохраняем его в файл
    key = Fernet.generate_key()
    with open('crypto.key', 'xb') as key_file:
        key_file.write(key)


def load_key():
    # Загружаем ключ 'crypto.key' из текущего каталога
    return open('crypto.key', 'rb').read()


def encrypt(filename, key_):
    # Зашифруем файл и записываем его
    f = Fernet(key_)
    with open(filename, 'rb') as file:
        # прочитать все данные файла
        file_data = file.read()
    encrypted_data = f.encrypt(file_data)
    # записать зашифрованный файл
    with open(filename, 'wb') as file:
        file.write(encrypted_data)


def decrypt(filename, key_):
    # Расшифруем файл и записываем его
    f = Fernet(key_)
    with open(filename, 'rb') as file:
        # читать зашифрованные данные
        encrypted_data = file.read()
    # расшифровать данные
    decrypted_data = f.decrypt(encrypted_data)
    # записать оригинальный файл
    with open(filename, 'wb') as file:
        file.write(decrypted_data)


def main():
    var = int(input('Что сделать? Создать ключ 1, Зашифровать файл 2, Расшифровать файл 3: '))
    if var == 1:
        write_key()
    elif var == 2:
        file_name = input('Путь и название файла: ')
        key_ = load_key()
        encrypt(file_name, key_)
    elif var == 3:
        file_name = input('Путь и название файла: ')
        key_ = load_key()
        decrypt(file_name, key_)


if __name__ == '__main__':
    main()
