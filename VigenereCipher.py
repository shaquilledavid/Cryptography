import os
from twilio.rest import Client


"""
This file will cover the Vignere Cipher.
The Vigenere Cipher uses a the characters of a word as keys. It uses the first
letter as the initial key, then second character as the next key and so on. 
    k1 = word[0],
    k2 = word[1]
    k3 = word[2]
    ...
    ki = word[i+1]

The encryption and decryption functions are as follows:

       ek(x0, x1, ..., xn) = (x0+k0, x1+k0, ..., xn+kn)mod26
       dk(y0, y1, ..., yn) = (y0-k0, y1-k1, ..., yn-kn)mod26,   where x, y are elements of Z26


       For example, plaintext = 'this' and keyword = ciph

                    t: ek(19) = (19 + 2)mod26 = 21 = 'v'
                    h: ek(7) = (7 + 8)mod26 = 15 = 'p'
                    i: ek(8) = (8 + 15)mod26 = 23 = 'x'
                    s: ek(18) = (18 + 7)mod26 = 25 = 'z'

                    ciphertext = 'vpxz'

                    dk(10) = (10-3)mod26
                    dk(15) = (15-7)mod26
"""

AlphaToNum = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6,
              'h': 7, 'i': 8, 'j': 9, 'k': 10, 'l': 11, 'm': 12,
              'n': 13, 'o': 14, 'p': 15, 'q': 16, 'r': 17, 's': 18,
              't': 19, 'u': 20, 'v': 21, 'w': 22, 'x': 23, 'y': 24, 'z': 25}

key_list = list(AlphaToNum.keys())
val_list = list(AlphaToNum.values())


def encrypt(plaintext, keyword):

    if len(plaintext) == 0:
        return ''

    elif len(plaintext) == 1:
        encrypt = (AlphaToNum[plaintext] + AlphaToNum[keyword[0]]) % 26
        return key_list[val_list.index(encrypt)]

    else:
        keys = []
        for letter in keyword:
            keys.append(letter)

        plaintextindex = 0
        keyindex = 0
        ciphertext = ''

        while plaintextindex < len(plaintext):
            if keyindex == len(keys):
                keyindex = 0  #if we reached the end of they keyword start over

            if plaintext[plaintextindex] == ' ':
                ciphertext = ciphertext + ' '
                plaintextindex = plaintextindex + 1
                #keyindex = keyindex + 1

            else:
                encrypt = (AlphaToNum[plaintext[plaintextindex]] + AlphaToNum[keys[keyindex]]) % 26
                ciphertext = ciphertext + key_list[val_list.index(encrypt)]
                plaintextindex = plaintextindex + 1
                keyindex = keyindex + 1
                
        return ciphertext


def decrypt(ciphertext, keyword):

    if len(ciphertext) == 0:
        return ''

    elif len(ciphertext) == 1:
        decrypt = (AlphaToNum[ciphertext] - AlphaToNum[keyword[0]]) % 26
        return key_list[val_list.index(decrypt)]

    else:
        keys = []
        for letter in keyword:
            keys.append(letter)

        ciphertextindex = 0
        keyindex = 0
        plaintext = ''

        while ciphertextindex < len(ciphertext):
            if keyindex == len(keys):
                keyindex = 0  #if we reached the end of they keyword start over

            if ciphertext[ciphertextindex] == ' ':
                plaintext = plaintext + ' '
                ciphertextindex = ciphertextindex+ 1

            else:
                decrypt = (AlphaToNum[ciphertext[ciphertextindex]] - AlphaToNum[keys[keyindex]]) % 26
                plaintext = plaintext + key_list[val_list.index(decrypt)]
                ciphertextindex = ciphertextindex + 1
                keyindex = keyindex + 1
                
        return plaintext



# run a program on startup
print("Hello! Welcome to the Vigenére Cipher.")
print('')

userplaintext = input("What message would you like me to encrypt for you? \n")

print('')
userkey = input("What would you like to use as your secret keyword? \n")

cipher = encrypt(userplaintext, str(userkey))


""" #UNCOMMENT THIS IF YOU WANT TO RUN THE MESSAGING PROCESS
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body= cipher,
                     from_='+12186566795',
                     to= os.environ['PHONE_NUMBER']
                 )

print(message.sid)
"""




            
