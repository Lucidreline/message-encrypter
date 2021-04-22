def encrypt(msg):
    increase = 1
    message = list(msg)
    # increase each letter by 'increase'

    for i in range(len(message)):
        message[i] = chr(ord(message[i]) + increase)

    return "".join(message)
    # reverse order of letters
