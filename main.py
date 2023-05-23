import MyRsa
import os
import pickle
rsa=None
if(not os.path.isfile("./rsa.bin")):
    rsa=MyRsa.getKeys()
    with open("rsa.bin","wb") as f:
        pickle.dump(rsa,f)
else:
    with open("rsa.bin","rb") as f:
        rsa=pickle.load(f)
print("Public key: "+hex(rsa.pubKey))
print("Private key: "+hex(rsa.privKey))
msg=input("Enter message to encrypt: ")
enc=MyRsa.encrypt(msg,rsa.pubKey,rsa.N)
print("Encrypted message: "+hex(enc))
dec=MyRsa.decrypt(enc,rsa.privKey,rsa.N)
print("Decrypted message: "+dec)
