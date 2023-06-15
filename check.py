from mcstatus import JavaServer
from config import ADDRESS


def get_number_online():
    server = JavaServer.lookup(ADDRESS)
    status = server.status()

    # print(f"The server has {status.players.online} player(s) online")
    return status.players.online
    