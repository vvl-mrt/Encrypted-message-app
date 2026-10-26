import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("127.0.0.1", 5000))

while True:
    texte = input("> ")
    if texte == "quit":
        break
    client.sendall(texte.encode("utf-8"))
    reponse = client.recv(1024)
    print(reponse.decode("utf-8"))

client.close()
