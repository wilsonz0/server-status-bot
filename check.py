from mcstatus import JavaServer
from config import ADDRESS

server = JavaServer.lookup(ADDRESS)
status = server.status()

def get_number_online():
    return status.players.online

def get_online_players():
    if status.players.online == 0:
        return
    
    return status.players.sample
