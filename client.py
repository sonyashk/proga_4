import socket

def send_data(host, port, data):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        s.send(b'gdhgdhfd')
        s.sendall(data.encode())
        print("Data sent successfully.")


def main():
    host = 'localhost'
    port = 9998
    while True:
        user_input = input("Enter a number (press Enter to send and exit): ")
        if not user_input:
            break
        try:
            number = int(user_input)
        except ValueError:
            error_message = "Invalid input: '{}' is not a valid number. Please enter a valid number.".format(user_input)
            print(error_message)
            continue
        send_data(host, port, user_input)

if __name__ == "__main__":
    main()
