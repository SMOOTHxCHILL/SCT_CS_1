#Caesar Cipher Encryption

def encryptor(p,k):#p=plaintext; k=key
    l = list(p)
    for  i in range(len(p)) :
        if l[i].isalpha() : # so that it doesn’t increment [space] or numbers
            l[i] = chr(((ord(l[i]) + k -  97) % 26) + 97) # ord() converts letter to number, increments it by key and chr() reconverts it back to letter. 26 as there are 26 letters in English. 97 as it is the ASCII value of 'a'
    print("The encrypted plaintext is ", end = "")
    for i in l :
        print(i, end = "")
    print("\n")
    
def decryptor(C,k):
    l = list(C)
    for i in range(len(C)) :
        if l[i].isalpha() :
            l[i] = chr(((ord(l[i]) - k - 97) % 26) + 97)
    print("The decrypted plaintext is ", end = "")
    for i in l :
        print(i, end = "")
    print("\n")

print("What\'s good")
while True:
    a = input("Enter\n1 for encryption\n2 for decryption\n3 to exit\nWhat's your choice?\n")
    if a == "1":
        str1 = input("Enter the plaintext; text to be encrypted: ")
        p = str1.lower()
        k = int(input("Enter the key; shift value: ")) % 26
        encryptor(p,k)
    elif a == "2":
        str2 = input("Enter the ciphertext; text to be decrypted: ")
        C = str2.lower()
        k = int(input("Enter the key; shift value: ")) % 26
        decryptor(C,k)
    elif a == "3":
        print("Byee<3")
        break
    else:
        print("Invalid input")
        continue
