"""
This file will cover the Autokey Cipher.
The Autokey Cipher uses multiple keys, with the first being manually set.
After using the first key, the numerical representation of the previous letter
in the plaintext becomes the next key.
    k1 = k,
    k2 = x1
    k3 = x2
    ...
    ki = xi - 1

The encryption and decryption functions are as follows:

       ek(x) = (x + k)mod26
       dk(y) = (y - k)mod26,   where x, y are elements of Z26


       For example, plaintext = hi and k1 = 3
                    numerical representation of 'hi' = 78

                    ek(7) = (7 + 3)mod26 = 10 = 'k'
                    then ek(8) = (8 + 7)mod26 = 15 = 'p'

                    ciphertext = 'kp'
"""

AlphaToNum = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6,
              'h': 7, 'i': 8, 'j': 9, 'k': 10, 'l': 11, 'm': 12,
              'n': 13, 'o': 14, 'p': 15, 'q': 16, 'r': 17, 's': 18,
              't': 19, 'u': 20, 'v': 21, 'w': 22, 'x': 23, 'y': 24, 'z': 25, ' ': 26}

key_list = list(AlphaToNum.keys())
val_list = list(AlphaToNum.values())

def encrypt(plaintext, k1):

    if len(plaintext) == 0:
        return ''

    elif len(plaintext) == 1:
        encrypt = (AlphaToNum[plaintext] + k1) % 26
        return key_list[val_list.index(encrypt)]

    else:
        i = 0
        encrypt = (AlphaToNum[plaintext[0]] + k1) % 26  #do the first letter
        ciphertext = key_list[val_list.index(encrypt)]
        i = i + 1
        while i < len(plaintext):

            if plaintext[i] != ' ':
                nextencrypt = (AlphaToNum[plaintext[i]] + AlphaToNum[plaintext[i-1]]) % 26
                ciphertext = ciphertext + key_list[val_list.index(nextencrypt)]
                i = i + 1
                
            else:
                ciphertext = ciphertext + ' '
                i = i + 1
                nextencrypt = (AlphaToNum[plaintext[i]] + AlphaToNum[plaintext[i-2]]) % 26
                ciphertext = ciphertext + key_list[val_list.index(nextencrypt)]
                i = i + 1

        return ciphertext


def decrypt(ciphertext, k1):

    if len(ciphertext) == 0:
        return ''

    elif len(ciphertext) == 1:
        decrypt = (AlphaToNum[ciphertext] - k1) % 26
        return key_list[val_list.index(decrypt)]

    else:
        i = 0
        decrypt = (AlphaToNum[ciphertext[0]] - k1) % 26  #do the first letter
        plaintext = key_list[val_list.index(decrypt)]
        i = i + 1
        while i < len(ciphertext):

            if ciphertext[i] != ' ':
                nextdecrypt = (AlphaToNum[ciphertext[i]] - AlphaToNum[ciphertext[i-1]]) % 26
                plaintext = plaintext + key_list[val_list.index(nextdecrypt)]
                i = i + 1
                
            else:
                plaintext = plaintext + ' '
                i = i + 1
                nextencrypt = (AlphaToNum[ciphertext[i]] - AlphaToNum[ciphertext[i-2]]) % 26
                plaintext = plaintext + key_list[val_list.index(nextdecrypt)]
                i = i + 1

        return plaintext
    
        
