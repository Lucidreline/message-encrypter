
increase = 1


def encrypt(msg, encryption):
    message = list(msg)
    # increase each letter by 'increase'

    if encryption:
        for i in range(len(message)):
            message[i] = chr(ord(message[i]) + increase)
    else:
        for i in range(len(message)):
            message[i] = chr(ord(message[i]) - increase)

    message.reverse()

    return "".join(message)
    # reverse order of letters
