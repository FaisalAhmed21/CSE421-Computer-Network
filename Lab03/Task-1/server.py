import socket

data = 16
port = 5050
FORMAT = 'utf-8'
device_name = socket.gethostname()
server_ip = socket.gethostbyname(device_name)

server_socket_address = (server_ip , port)
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(server_socket_address)

server.listen()
print("Our server is listening...")

while True:
    server_socket, client_add = server.accept()
    print("Connected to ", client_add)
    connected = True

    while connected:
        upcoming_message_length = server_socket.recv(data).decode(FORMAT)

        if not upcoming_message_length.strip():
            print("Client disconnected abruptly: ", client_add)

        print("Upcoming message length is: ", upcoming_message_length.strip())

        message_length = int(upcoming_message_length.strip())

        message = server_socket.recv(message_length).decode(FORMAT)

        if message.lower() == 'disconnect':
            print("Disconnected with ", client_add)
            connected = False


        print(message)
        server_socket.send("Message received.".encode(FORMAT))

    server_socket.close()