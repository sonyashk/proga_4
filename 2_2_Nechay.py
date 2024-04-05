import json
import socket


# Функция для отправки команды на установку новой корневой папки
def send_command_to_program1(new_root):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 9998))
    client_socket.sendall(f"SET_ROOT:{new_root}".encode())  # Отправляем новую папку программе 1

    # Получаем данные по сети
    received_data = b""
    while True:
        chunk = client_socket.recv(1024)
        if not chunk:
            break
        received_data += chunk

    client_socket.close()
    return received_data


# Функция для вывода содержимого
def print_file_content(file_info):
    file_info = json.loads(file_info.decode())
    for item in file_info:
        print(f"Путь: {item['path']}, Размер: {item['size']} байт, Modified Time: {item['modified_time']}")



def main():
    new_root = input("Ведите путь новой директории: ")
    received_data = send_command_to_program1(new_root)  # Команда на зменение корневой папки
    print_file_content(received_data)  # Выводим содержимое файла


if __name__ == "__main__":
    main()