# import random

alphabet = "abcdefghijklmnopqrstuvwxyz "

alphabet_list = [alphabet[i] for i in range(len(alphabet))]
alphabet_list = list(alphabet)

# print(alphabet_list)

# message_text = "what is a baggins"

# cipher_list = list(alphabet_list)
# random.shuffle(cipher_list)
# print cipher_list

message_text = "that is an excellent idea"
cipher_text = ""

cipher_list = [
    'v', 'y', 'h', 'l', 'a', 'n', 'i', 'g', 'e', 'd', 'k',
    'c', 'w', ' ', 'f', 's', 'm', 'p', 'r', 't', 'o', 'u', 'z', 'b', 'j',
    'x', 'q'
]


def encrypt(message):
    """Create cipher from message."""
    cipher_text = ""

    for x in message:
        index = alphabet_list.index(x)
        cipher_char = cipher_list[index]
        cipher_text += cipher_char

    return cipher_text

# encrypt(message_text)


def decrypt(cipher):
    """Decrypt cipher"""
    message_text = ""

    for x in cipher:
        index = cipher_list.index(x)
        message_char = alphabet_list[index]
        message_text += message_char

    return message_text

# decrypt(cipher_text)
