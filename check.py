from mcstatus import JavaServer
from config import ADDRESS

server = JavaServer.lookup(ADDRESS)
status = server.status()
print(f"The server has {status.players.online} player(s) online")