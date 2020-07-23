from cryptography.fernet import Fernet

import re

#Ignore the commented code as it is just extra functionality that I thought to be part of the objective

'''
Encode method  : 
'''
#encryptionKey = Fernet.generate_key()
encryptionKey = b'O1-2lR-RTyfXj6T07WN8sz8zeotthtWHCkBaNLDlQ7o='
cipher_suite = Fernet(encryptionKey)

ref_ID_patter = "^[\w\d]{12}$"

def check_RefID(refID):
    return True if bool(re.match(ref_ID_patter, refID)) else False
'''
def create_account(db):
    toWriteString = ''
    ref_id = str(input('Enter your Ref-ID: '))
    if check_RefID(ref_id): 
        pass
    else:
        print("Invalid.")
        create_account(db)
    name = str(input('Enter your First Name: '))
    toWriteString += ref_id + ',' + name
    db.write(toWriteString)
    print("Account Created Successfully")
'''  
codec = 'UTF'
def encrypt_refID(refID:bytes):
    return cipher_suite.encrypt(refID)
def decrypt_refID(refID:bytes):
    return cipher_suite.decrypt(refID)

def main():
    print('Welcome to -!')
    option = int(input('Do you want to encrypt[1] or decrypt[2]?'))
    if option==1:
        #ENCRYPTING
        refID = str(input('Please enter your RefID to proceed: '))
        if refID: pass
        encryptedRefID = encrypt_refID(bytes(refID, 'UTF'))
        print(encryptedRefID)
    else:
        #DECRYPTING
        refID_to_decrypt = input('Enter your encrypted refID: ')
        tmp = bytes(refID_to_decrypt, 'UTF')
        print(decrypt_refID(tmp))
        
        
    #LogorSign = int(input('Sign In[1] or Sign Up[2]'))
    #if LogorSign is 1:
    #    LogIn()
    #else:
    #    db = open('tData.csv', 'w')
    #    db.seek(2)
    #    create_account(db)
    #    db.close()
    #refID = str(input('Please enter your RefID to proceed: '))
    #if refID: pass
    #encryptedRefID = encrypt_refID(refID)
    #print(encryptedRefID)
main()