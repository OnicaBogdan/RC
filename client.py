import socket
import threading

HOST = '127.0.0.1'
PORT = 65432

def receive_messages(sock):
    
    while True:
        try:
            message = sock.recv(1024).decode('utf-8')
            if message:
                print(f"\n[SERVER]: {message}")
                print("Mesaj: ", end="")
            else:
                break
        except:
            print("\nConexiune închisă.")
            break

def start_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client.connect((HOST, PORT))
    except:
        print("Eroare: Serverul nu este pornit!")
        return

    thread = threading.Thread(target=receive_messages, args=(client,))
    thread.daemon = True
    thread.start()

    print("Te-ai conectat la chat! (Scrie 'exit' pentru a ieși)")
    while True:
        msg = input("Mesaj: ")
        if msg.lower() == 'exit':
            break
        client.send(msg.encode('utf-8'))

    client.close()

if __name__ == "__main__":
    start_client()