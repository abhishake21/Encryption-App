# Importing cryptography library
from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

# Importing required libraries
import os
import base64
import getpass
from tqdm import tqdm


# Menu
def menu():
    choice = input('\n1. Encrypt a file\n2. Decrypt a file\n3. Encrypt a folder\n4. Decrypt a folder\n\nType "quit" to exit.\n\n')

    if choice == '1':
        print('\tTo Encrypt a file enter Password, Salt and file-location. Type "menu" to select different option or "quit" to exit.')
        encfile()
    elif choice == '2':
        print('\tTo Decrypt a file enter Password, Salt and file-location. Type "menu" to select different option or "quit" to exit.')
        decfile()
    elif choice == '3':
        print('\tTo Encrypt a folder enter Password, Salt and folder-location. Type "menu" to select different option or "quit" to exit.')
        encfolder()
    elif choice == '4':
        print('\tTo Decrypt a folder enter Password, Salt and folder-location. Type "menu" to select different option or "quit" to exit.')
        decfolder()
    elif choice == 'quit':
        print('\nProgram Ended.')
    else:
        print('\nEnter below choices only')
        menu()


# os.walk() Error Handler
def enc_walk_error_handler(exception_instance):
    print('\n\n\tSomething went wrong.')
    print('''
    > Check if file location and name are correct.
    Eg - D:/User/Secretfiles/

    Type "menu" to select different option or "quit" to exit.\n
    ''')
    encfolder()
def dec_walk_error_handler(exception_instance):
    print('\n\n\tSomething went wrong.')
    print('''
    > Wrong Password and/or Salt entered.
    > Check if folder location and name are correct.
    Eg - D:/User/Secretfiles/

    Type "menu" to select different option or "quit" to exit.\n
    ''')
    decfolder()


# File Encryption funtion
def encfile():

    upassword = getpass.getpass('\nEnter password - ')

    if upassword == 'quit':
        print('Program Ended.')
    elif upassword == 'menu':
        menu()
    else:
        usalt = getpass.getpass('Enter Salt(leave blank if not required) - ')

        if usalt == 'quit':
            print('\nProgram Ended.')
        elif usalt == 'menu':
            menu()
        else:
            def enc():
                fileln = input('Enter file locations(separated by comma) - ').split(',')
                password=bytes(upassword,'utf-8')
                salt=bytes(usalt,'utf-8')

                try:
                    kdf = PBKDF2HMAC(
                        algorithm=hashes.SHA256(),
                        length=32,
                        salt=salt,
                        iterations=100000,
                        backend=default_backend())

                    key = base64.urlsafe_b64encode(kdf.derive(password))
                    f = Fernet(key)

                    cnt = len(fileln)

                    with tqdm(total=cnt) as pbar:
                        for file in fileln:
                            with open(file,'rb') as original_file:
                                original = original_file.read()

                            encrypted = f.encrypt(original)

                            with open (file,'wb') as encrypted_file:
                                encrypted_file.write(encrypted)
                            pbar.update(1)

                    print('\nAll files are Encrypted.')

                except:
                    print('\n\tSomething went wrong.')
                    print('''
                    Check if file location and name are correct.
                    Eg - D:/User/Secretfiles/secrets.txt

                    Type "menu" to select different option or "quit" to exit.\n
                    ''')
                    encfile()
            enc()
    menu()

# File Decryption funtion
def decfile():

    upassword = getpass.getpass('\nEnter password - ')

    if upassword == 'quit':
        print('\nProgram Ended.')
    elif upassword == 'menu':
        menu()
    else:
        usalt = getpass.getpass('Enter Salt(leave blank if not required) - ')

        if usalt == 'quit':
            print('\nProgram Ended.')
        elif usalt == 'menu':
            menu()
        else:
            def dec():
                fileln = input('Enter file locations(separated by comma) - ').split(',')
                password=bytes(upassword,'utf-8')
                salt=bytes(usalt,'utf-8')

                try:
                    kdf = PBKDF2HMAC(
                        algorithm=hashes.SHA256(),
                        length=32,
                        salt=salt,
                        iterations=100000,
                        backend=default_backend())

                    key = base64.urlsafe_b64encode(kdf.derive(password))
                    f = Fernet(key)

                    cnt = len(fileln)

                    with tqdm(total=cnt) as pbar:
                        for file in fileln:
                            with open(file,'rb') as original_file:
                                original = original_file.read()

                            decrypted = f.decrypt(original)

                            with open (file,'wb') as decrypted_file:
                                decrypted_file.write(decrypted)
                            pbar.update(1)
                    print('\nAll files are Decrypted.')


                except:
                    print('\n\tSomething went wrong.')
                    print('''
                    > Wrong Password and/or Salt entered.
                    > Check if file location and name are correct.
                    Eg - D:/User/Secretfiles/secrets.txt

                    Type "menu" to select different option or "quit" to exit.\n
                    ''')
                    decfile()
            dec()
    menu()

# Folder Encryption funtion
def encfolder():

    upassword = getpass.getpass('\nEnter password - ')

    if upassword == 'quit':
        print('\nProgram Ended.')
    elif upassword == 'menu':
        menu()
    else:
        usalt = getpass.getpass('Enter Salt(leave blank if not required) - ')

        if usalt == 'quit':
            print('\nProgram Ended.')
        elif usalt == 'menu':
            menu()
        else:
            def enc():
                folderln = input('Enter folder location - ')
                if folderln == 'quit':
                    print('\nProgram Ended.')
                elif folderln == 'restart':
                    encfolder()
                else:
                    password=bytes(upassword,'utf-8')
                    salt=bytes(usalt,'utf-8')

                    try:
                        kdf = PBKDF2HMAC(
                            algorithm=hashes.SHA256(),
                            length=32,
                            salt=salt,
                            iterations=100000,
                            backend=default_backend())

                        key = base64.urlsafe_b64encode(kdf.derive(password))
                        f = Fernet(key)

                        cnt = sum([len(files) for r, d, files in os.walk(folderln)])

                        with tqdm(total=cnt, position=0, leave=True) as pbar:
                            for path, subdirs, files in os.walk(folderln, onerror=enc_walk_error_handler):
                                if enc_walk_error_handler==True:
                                    pass
                                else:
                                    for file in files:
                                        with open(os.path.join(path,file),'rb') as original_file:
                                            original = original_file.read()

                                        encrypted = f.encrypt(original)

                                        with open(os.path.join(path,file),'wb') as encrypted_file:
                                            encrypted_file.write(encrypted)
                                        pbar.update(1)

                        print('\nAll files and folders in '+folderln+' are Encrypted.')

                    except:
                        print('\n\tSomething went wrong.')
                        print('''
                        > Check if file location and name are correct.
                        Eg - D:/User/Secretfiles/

                        Type "menu" to select different option or "quit" to exit.\n
                        ''')
                        encfolder()
            enc()
    menu()

# Folder Decryption funtion
def decfolder():

    upassword = getpass.getpass('\nEnter password - ')

    if upassword == 'quit':
        print('\nProgram Ended.')
    else:
        usalt = getpass.getpass('Enter Salt(leave blank if not required) - ')

        if usalt == 'quit':
            print('\nProgram Ended.')
        else:
            def dec():
                folderln = input('Enter folder location - ')

                if folderln == 'quit':
                    print('\nProgram Ended.')
                elif folderln == 'restart':
                    decfolder()
                else:
                    password=bytes(upassword,'utf-8')
                    salt=bytes(usalt,'utf-8')

                    try:
                        kdf = PBKDF2HMAC(
                            algorithm=hashes.SHA256(),
                            length=32,
                            salt=salt,
                            iterations=100000,
                            backend=default_backend())

                        key = base64.urlsafe_b64encode(kdf.derive(password))
                        f = Fernet(key)

                        cnt = sum([len(files) for r, d, files in os.walk(folderln)])

                        with tqdm(total=cnt, position=0, leave=True) as pbar:
                            for path, subdirs, files in os.walk(folderln, onerror=dec_walk_error_handler):
                                if dec_walk_error_handler==True:
                                    pass
                                else:
                                    for file in files:
                                        with open(os.path.join(path,file),'rb') as original_file:
                                            original = original_file.read()

                                        decrypted = f.decrypt(original)

                                        with open(os.path.join(path,file),'wb') as decrypted_file:
                                            decrypted_file.write(decrypted)
                                        pbar.update(1)

                        print('\nAll files and folders in '+folderln+' are Decrypted.')

                    except:
                        print('\n\tSomething went wrong.')
                        print('''
                        > Wrong Password and/or Salt entered.
                        > Check if folder location and name are correct.
                        Eg - D:/User/Secretfiles/

                        Type "menu" to select different option or "quit" to exit.\n
                        ''')
                        decfolder()
            dec()
    menu()


# Main App
menu()
