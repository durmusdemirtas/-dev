# *-* coding utf8 *-*

import socketserver
import datetime
import pickle


bagli_clientler = []
mesajlar = []

class MyHandler(socketserver.BaseRequestHandler):

    def handle(self):
        print (self.client_address)
        data =  self.request.recv(1024)
        self.request.sendall("#hg")
        username = self.request.recv(1024)
        bagli_clientler.append({'client': self.client_address, 'name' : username, 'date' : datetime.datetime.now()})
        self.request.sendall("#gir")
        while True:
            msg = self.request. recv(1024)
            mesajlar.append({'client' : (self.client_address[0], username), 'date': datetime.datetime.now(), 'message': msg})
            self.request.sendall(pickle.dumps(mesajlar))


    def baglanti_kur(host, post, classname):
        server: ThreadingTCPServer = socketserver.ThreadingTCPServer((host, post), classname)
        server.serve_forever()

    if __name__ == "__main__":
    baglanti_kur("0.0.0.0", 6666, MyHandler)



