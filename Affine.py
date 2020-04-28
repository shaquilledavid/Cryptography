"""
This file will serve as purpose for encrypting and decrypting messages for the
Affine Cipher.
The Affine Cipher uses a key K: (a, b). The encryption and decryption
function are as follows:
                        ek(x): (ax + b)mod26
                        dk(x): a^-1(y - b)mod26

                        where x and y are elements of Z26.

                        For example, if we have K = (7,3) and our plaintext is 'h'
                        H corresponds to 7 in our Alpha to Num conversion chart

                        Encryption of 'h': ek(7) = ((7*7) + 3))mod26
                                          = 'a'
"""

AlphaToNum = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6,
              'h': 7, 'i': 8, 'j': 9, 'k': 10, 'l': 11, 'm': 12,
              'n': 13, 'o': 14, 'p': 15, 'q': 16, 'r': 17, 's': 18,
              't': 19, 'u': 20, 'v': 21, 'w': 22, 'x': 23, 'y': 24, 'z': 25, ' ': 26}

multiplicativeInverse = {1: 1, 3: 9, 5: 21, 7: 15, 9: 3, 11: 19,
                          15: 7, 17: 23, 19: 11, 21: 5, 23: 17, 25: 25}

key_list = list(AlphaToNum.keys())
val_list = list(AlphaToNum.values())



def encrypt(plaintext, a, b):

    if len(plaintext) == 0:
        return ''
    
    elif len(plaintext) == 1:
        alphanum = AlphaToNum[plaintext]
        encrypt = ((a*alphanum) + b) % 26
        return key_list[val_list.index(encrypt)]

    else:
        i = 0
        ciphertext = ''
        while i < len(plaintext):
            alphanum = AlphaToNum[plaintext[i]]
            
            if alphanum == 26:                   # special case for a space
                ciphertext = ciphertext + ' '
                i = i + 1
                
            else:
                letterEncrypt = ((a*alphanum) + b) % 26 
                ciphertext = ciphertext + (key_list[val_list.index(letterEncrypt)]) 
                i = i + 1
                
        return ciphertext



def decrypt(ciphertext, a, b):
    
        if len(ciphertext) == 0:
            return ''
        
        elif len(ciphertext) == 1:
            decrypt = (multiplicativeInverse[a] * (AlphaToNum[ciphertext] - b)) % 26
            return key_list[val_list.index(decrypt)]

        else:
            i = 0
            plaintext = ''
            while i < len(ciphertext):

                if ciphertext[i] == ' ':
                    plaintext = plaintext + ' '
                    i = i + 1
                    
                else:
                    decrypt = (multiplicativeInverse[a] * (AlphaToNum[ciphertext[i]] - b)) % 26
                    plaintext = plaintext + key_list[val_list.index(decrypt)]
                    i = i + 1

            return plaintext
            
                        
