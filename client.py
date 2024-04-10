import socket

def send_data(host, port, data):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        s.sendall(data.encode())
        print("Data sent successfully.")
        response = s.recv(1024)
        print("Response from server:", response.decode())

def main():
    host = '127.0.0.1'
    port = 9995

    # Установка соединения с сервером
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        print("Connection established with the server.")

    while True:
        user_input = input("Enter a number (press Enter to send and exit): ")
        if not user_input:
            break
        try:
            number = int(user_input)
        except ValueError:
            error_message = f"Invalid input: '{user_input}' is not a valid number. Please enter a valid number."
            print(error_message)
            continue
        send_data(host, port, user_input)

if __name__ == "__main__":
    main()

