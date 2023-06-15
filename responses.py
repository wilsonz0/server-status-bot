import check

def get_response(message: str) -> str:
    p_message = message.lower()

    if p_message == 'hello':
        return 'Yahoi'
    
    if p_message == '!getstatus':
        return str(check.get_number_online()) + " players(s) online"

    return "I do not understand. Try again." 