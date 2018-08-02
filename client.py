import pickle
import socket
import datetime

host= "84.200.53.116"
port = 6666

server =socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.connet((host, post))
print ("baglanti kuruldu")
server.send("Mrb")
server.recv(1024)
name = raw_input("User name : ")
server.sendall(name)
data = server.recv(1024)

if data == "#gir":
    while True:
        msg = raw_input(str.format("{}$ ", name))
        server.sendall(msg)
        mesajlar = pickle.loads(server.recv(1024))
        print ("=====================================================")
        for i in mesajlar:
            print (str.format("{0}: {1}", i['client'][1], i['message']))

        print ("=====================================================")