import socket

HOTE = "127.0.0.1"
PORT = 5000

serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serveur.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
serveur.bind((HOTE,PORT))
serveur.listen()

print(f"waiting for a client on the port {PORT}")

conn, adresse = serveur.accept()

print("Client connected : ", adresse)

while True:
    donnees = conn.recv(1024)
    if not donnees:
        break
    print("Recieved : ", donnees.decode("utf-8"))
    conn.sendall(b"Echo " + donnees)

conn.close()
serveur.close()
