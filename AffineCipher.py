"""
This file will serve as purpose for encrypting and decrypting messages for the
Affine Cipher.
The Affine Cipher uses a key K: (a, b). The encryption and decryption
functions are as follows:
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




# run a program on startup
print("Hello! Welcome to the Affine Cipher.")

print('')

userplaintext = input("What message would you like me to encrypt for you? \n")

userkey = input("What number would you like to use as the first value of your key? \n")
userkey2 = input("What number would you like to use as the second value of your key? \n")

cipher = encrypt(userplaintext, int(userkey), int(userkey2))
print('')
print('...')
print('Encryption Successful.')
print('')
print("Your encrypted message is \n" + cipher)
print('')
print('')

answer = input("Would you like to decrypt a message? ('yes'/'no') \n")

if answer == 'yes':
    print('')
    decryptquestion = input("Enter the message \n")
    userkey3 = input("Enter the first key value \n")
    userkey4 = input("Enter second key value \n")
    print('')
    print('...')
    if int(userkey3) not in multiplicativeInverse.values():
        print("Sorry, this decryption is not possible. The first key value is not coprime with 26")

    else:
        print('Decryption Successful.')
        print('')
        print("The decrypted message is \n" + decrypt(decryptquestion, int(userkey3), int(userkey4)))

    


                        
