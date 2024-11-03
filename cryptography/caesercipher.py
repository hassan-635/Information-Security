def caesarEncrypt(plainText, shift):
    encryptedText = ""
    
    for char in plainText:
        if char.isalpha():
            if char.isupper():
                  encryptedText+=chr((ord(char)-65+shift)%26+65)
            else:
                encryptedText+=chr((ord(char)-97+shift)%26+97)
        else:
            encryptedText+=char          
    return encryptedText


def caesarDecrypt(encText, shift):
    return caesarEncrypt(encText, -shift)
        

text = "Hassan Ali Abrar"
shift = int(input("Enter shift size : "))
enc = caesarEncrypt(text, shift)
print(f"Encrypted text : {enc}")
dec = caesarDecrypt(enc, shift)
print(f"Decrypted text : {dec}")
