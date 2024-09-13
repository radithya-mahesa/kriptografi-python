import hashlib

#Caesar cipher algorithm
def encrypt(text,s):
    result = ""

    # traverse text
    for i in range(len(text)):
        char = text[i]

        # Encrypt uppercase characters
        if (char.isupper()):
            result += chr((ord(char) + s -65) % 26 + 65)

        # Encrypt lowercase characters
        else:
           result += chr((ord(char) + s -97) % 26 + 97)

    return result

#check the above function
text = 'Ligma'
s = 10
print ('Plain Text : ' + text)
print ('Shift : ' + str(s))
print ('Cipher Text : ' + encrypt(text,s))

#SHA256 algorithm
plaintext = 'Sigma'
hasil = hashlib.sha256(plaintext.encode())

print('Hasil enkripsi SHA256 dari', text, end =" ")
print(hasil.hexdigest())