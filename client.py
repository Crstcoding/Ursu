import socket

HEADER = 64
port = 5050
SERVER = "10.10.10.131"
FORMAT = 'utf-8'
ADDR = (SERVER, port)

client_disconnect_msg = "[!DISCONNECTED]"

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)



def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    print(client.recv(2048).decode(FORMAT))




if __name__ == '__main__':
    for i in range(10):
        message_send = input("If you have a problem with the server, send a message to the admin: ")
        send(message_send)
