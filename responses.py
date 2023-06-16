import check

def get_response(message: str) -> str:
    p_message = message.lower()

    if p_message == 'hello':
        return 'Yahoi'
    
    if p_message == 'smithing':
        return 'smeyething'
    
    if p_message == '!getstatus':
        return str(check.get_number_online()) + " player(s) online"
    
    if p_message == '!getallnames':
        allplayers = check.get_online_players()

        if allplayers == None:
            return "Everyone is offline"

        temp = ""
        for player in allplayers:
            temp += str(player.name) + ", "
        return temp

