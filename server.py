import socket
import threading


HOST = '127.0.0.1'  
PORT = 65432       

clients = [] 

def broadcast(message, _client_socket):
    
    for client in clients:
        try:
            client.send(message)
        except:
          
            if client in clients:
                clients.remove(client)

def handle_client(client_socket, addr):
    
    print(f"[CONEXIUNE] {addr} s-a conectat.")
    
    while True:
        try:
            message = client_socket.recv(1024)
            if not message:
                break
            
            print(f"[{addr}]: {message.decode('utf-8')}")
            
            broadcast(message, client_socket)
        except:
            break

    client_socket.close()
    if client_socket in clients:
        clients.remove(client_socket)
    print(f"[DECONECTARE] {addr} a plecat.")

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen()
    print(f"SERVERUL A PORNIT pe {HOST}:{PORT}")

    while True:
        client_socket, addr = server.accept()
        clients.append(client_socket)

        thread = threading.Thread(target=handle_client, args=(client_socket, addr))
        thread.start()

if __name__ == "__main__":
    start_server()