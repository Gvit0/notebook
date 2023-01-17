from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer
import os, socket

ip = socket.gethostbyname(socket.gethostname())
PATH = 'D:\\Misc'
os.chdir(PATH)

addr = (ip,21)
authorizer = DummyAuthorizer()
authorizer.add_user('Gvit0','yyyrrr1747', '.', perm='elradfmw')

handler = FTPHandler
handler.authorizer = authorizer
server = FTPServer(addr,handler)
server.serve_forever()
