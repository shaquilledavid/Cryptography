"""
This file will serve as purpose for encrypting and decrypting messages for the
Affine Cipher.
The Affine Cipher uses a key K: (a, b). With the encryption and decryption
function are as follows:
                        ek(x): (ax + b)mod26
                        dk(x): a^-1(y - b)mod26

                        where x and y are elements of Z26.

                        For example, if we have K = (7,3) and our plaintext is 'H'

                        H corresponds to 7 in our Alpha to Num conversion chart

                        Encryption of H: ek(7) = ((7*7) + 3))mod26
"""

AlphaToNum = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6,
              'h': 7, 'i': 8, 'j': 9, 'k': 10, 'l': 11, 'm': 12,
              'n': 13, 'o': 14, 'p': 15, 'q': 16, 'r': 17, 's': 18,
              't': 19, 'u': 20, 'v': 21, 'w': 22, 'x': 23, 'y': 24, 'z': 25, ' ': 26}

key_list = list(AlphaToNum.keys()) 
val_list = list(AlphaToNum.values())

def encrypt(word, a, b):

    if len(word) == 0:
        return ''
    
    elif len(word) == 1:
        alphanum = AlphaToNum[word]
        return ((a*alphanum) + b) % 26

    else:
        i = 0
        ciphertext = ''
        while i < len(word):
            alphanum = AlphaToNum[word[i]]
            
            if alphanum == 26:                   # special case for a space
                ciphertext = ciphertext + ' '
                i = i + 1
                
            else:
                letterEncrypt = ((a*alphanum) + b) % 26 
                ciphertext = ciphertext + (key_list[val_list.index(letterEncrypt)]) 
                i = i + 1
                
        return ciphertext
            
            
            
            
                        
