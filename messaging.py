from keys import api, USRID


def msg(message):
    api.send_direct_message(user_id=USRID, text=message)
def getmsg():
    try:
        message=api.direct_messages()
        message=message[0]
        text=message.text
        id=message.id
        api.destroy_direct_message(id)
        return text
    except:
        pass