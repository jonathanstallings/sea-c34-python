#modify code so it can be decrypted given key


#import random

alphabet = "abcdefghijklmnopqrstuvwxyz "

alphabet_list = [alphabet[i] for i in range(len(alphabet))]
alphabet_list = list(alphabet)

    #print(alphabet_list)

    #message_text = "why hello there!"

    #cipher_list = list(alphabet_list)
    #random.shuffle(cipher_list)

message_text = "great success"

cipher_list = ['v', 'y', 'h', 'l', 'a', 'n', 'i', 'g', 'e', 'd', 'k', 'c', 'w', ' ', 'f', 's', 'm', 'p', 'r', 't', 'o', 'u', 'z', 'b', 'j', 'x', 'q']
#print cipher_list


def cipher():
    cipher_text = ""

    for x in message_text:
        index = alphabet_list.index(x)
        cipher_char = cipher_list[index]
        cipher_text += cipher_char
    
    print cipher_text
cipher()

cipher_text = "ipavtqrohharr"

def decipher():
    message_text = ""

    for x in cipher_text:
        index = cipher_list.index(x)
        message_char = alphabet_list[index]
        message_text += message_char
    
print message_text
decipher()


