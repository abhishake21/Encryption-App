# Importing Tkinter
import tkinter as tk
import tkinter.filedialog as fd
from tkinter import messagebox
from tkinter.ttk import *

# Importing required libraries
import os
import threading
import webbrowser

# Importing cryptography library modules
from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import base64

# File Frame
def fileframe():
# Frames
    global fiframe
    global filist_frame
    global fibutton_frame
# Labels
    global fipassword_lable
    global fisalt_lable
    global fi_selectfile_label
# Input boxes
    global fipasswordbox
    global fisaltbox
    global filistbox
# Buttons
    global browsefi
    global file_enc_button
    global file_dec_button

# Input Box + Browse Button
    fiframe = tk.LabelFrame(root, text='   Files   ',font='Raleway 19 bold',padx=10,pady=10)
    fiframe.grid(row=0,column=0,padx=40,pady=20)

    fipassword_lable = tk.Label(fiframe, text = "Password",font='Raleway 15 bold')
    fipassword_lable.grid(row=0, column=0)

    fipasswordbox = tk.Entry(fiframe, show='*', width=25, font='Raleway 15 bold', insertbackground='white')
    fipasswordbox.grid(row=0, column=1, padx=5, pady=5)

    fisalt_lable = tk.Label(fiframe, text = "Salt",font='Raleway 15 bold')
    fisalt_lable.grid(row=1, column=0)

    fisaltbox = tk.Entry(fiframe, show='*', width=25, font='Raleway 15 bold', insertbackground='white')
    fisaltbox.grid(row=1, column=1, padx=5, pady=5)

    fi_selectfile_label = tk.Label(fiframe,text='Select Files', font='Raleway 15 bold')
    fi_selectfile_label.grid(row=2,column=0)

    browsefi = tk.Button(fiframe, text='Browse', font='Raleway 15 bold', width=20, command=fibrowse, borderwidth=3)
    browsefi.grid(row=2,column=1,padx=5, pady=5)


# List + Scroll Bar
    filist_frame = tk.Frame(fiframe)
    filist_frame.grid(row=3, columnspan=2)

    fiscroll = tk.Scrollbar(filist_frame, orient='vertical')
    fiscroll.grid(row=3,column=2, sticky='NSW')

    filistbox = tk.Listbox(filist_frame, width=50,height=10,font='Raleway 13')
    filistbox.grid(row=3,columnspan=2, pady=10)

    filistbox.config(yscrollcommand=fiscroll.set)
    fiscroll.config(command=filistbox.yview)


# Button
    fibutton_frame = tk.Frame(fiframe)
    fibutton_frame.grid(row=4, columnspan=2)

    file_enc_button = tk.Button(fibutton_frame, text='Encrypt',font='Raleway 15 bold', width=15,command=encfile, borderwidth=3)
    file_enc_button.grid(row=4,column=0,padx=30,pady=15)

    file_dec_button = tk.Button(fibutton_frame, text='Decrypt',font='Raleway 15 bold', width=15,command=decfile, borderwidth=3)
    file_dec_button.grid(row=4,column=1,padx=30,pady=15)


# HOVER COLOR CHANGE
    file_enc_button.bind("<Enter>", lambda e: file_enc_button.config(fg='white', bg='black'))
    file_enc_button.bind("<Leave>", lambda e: file_enc_button.config(fg='white', bg='#575757'))

    file_dec_button.bind("<Enter>", lambda e: file_dec_button.config(fg='white', bg='black'))
    file_dec_button.bind("<Leave>", lambda e: file_dec_button.config(fg='white', bg='#575757'))

    browsefi.bind("<Enter>", lambda e: browsefi.config(fg='white', bg='black'))
    browsefi.bind("<Leave>", lambda e: browsefi.config(fg='white', bg='#575757'))


# Folder Frame
def folderframe():
# Frames
    global foframe
    global folist_frame
    global fobutton_frame
# Labels
    global fopassword_lable
    global fosalt_lable
    global fo_selectfolder_label
# Input boxes
    global fopasswordbox
    global fosaltbox
    global folistbox
# Buttons
    global browsefo
    global fold_enc_button
    global fold_dec_button

# Input Box + Browse Button
    foframe = tk.LabelFrame(root, text='   Folder   ',font='Raleway 19 bold',padx=10,pady=10)
    foframe.grid(row=0,column=1,padx=40,pady=20)

    fopassword_lable = tk.Label(foframe, text = "Password",font='Raleway 15 bold')
    fopassword_lable.grid(row=0, column=0)

    fopasswordbox = tk.Entry(foframe, show='*', width=25, font='Raleway 15 bold', insertbackground='white')
    fopasswordbox.grid(row=0, column=1, padx=5, pady=5)

    fosalt_lable = tk.Label(foframe, text = "Salt",font='Raleway 15 bold')
    fosalt_lable.grid(row=1, column=0)

    fosaltbox = tk.Entry(foframe, show='*', width=25, font='Raleway 15 bold', insertbackground='white')
    fosaltbox.grid(row=1, column=1, padx=5, pady=5)

    fo_selectfolder_label = tk.Label(foframe,text='Select Folder', font='Raleway 15 bold')
    fo_selectfolder_label.grid(row=2,column=0)

    browsefo = tk.Button(foframe, text='Browse', font='Raleway 15 bold', width=20, command=fobrowse, borderwidth=3)
    browsefo.grid(row=2,column=1, padx=5, pady=5)


# List + Scroll Bar
    folist_frame = tk.Frame(foframe)
    folist_frame.grid(row=3, columnspan=2)

    foscroll = tk.Scrollbar(folist_frame, orient='vertical')
    foscroll.grid(row=3,column=2, sticky='NSW')

    folistbox = tk.Listbox(folist_frame, width=50,height=10,font='Raleway 13')
    folistbox.grid(row=3,columnspan=2, pady=10)

    folistbox.config(yscrollcommand=foscroll.set)
    foscroll.config(command=folistbox.yview)


# Button
    fobutton_frame = tk.Frame(foframe)
    fobutton_frame.grid(row=4, columnspan=2)

    fold_enc_button = tk.Button(fobutton_frame, text='Encrypt',font='Raleway 15 bold', width=15,command=encfolder, borderwidth=3)
    fold_enc_button.grid(row=4,column=0,padx=30,pady=15)

    fold_dec_button = tk.Button(fobutton_frame, text='Decrypt',font='Raleway 15 bold', width=15, command=decfolder, borderwidth=3)
    fold_dec_button.grid(row=4,column=1,padx=30,pady=15)


# HOVER COLOR CHANGE

    fold_enc_button.bind("<Enter>", lambda e: fold_enc_button.config(fg='white', bg='black'))
    fold_enc_button.bind("<Leave>", lambda e: fold_enc_button.config(fg='white', bg='#575757'))

    fold_dec_button.bind("<Enter>", lambda e: fold_dec_button.config(fg='white', bg='black'))
    fold_dec_button.bind("<Leave>", lambda e: fold_dec_button.config(fg='white', bg='#575757'))

    browsefo.bind("<Enter>", lambda e: browsefo.config(fg='white', bg='black'))
    browsefo.bind("<Leave>", lambda e: browsefo.config(fg='white', bg='#575757'))


# Progress Bar
def progbar():
    global pb_lable
    global percent
    global pbar
    global percentlabel
    global darkmodebtn
    global pbar_frame

    pb_lable = tk.Label(root, text=' |      Progress      | ', bg="#B0FF84", font = "Raleway 13 bold")
    pb_lable.grid(row=5, columnspan=2, sticky='w', padx=35)

    darkmodebtn = tk.Button(root, text='Turn Off Darkmode', bg='#B0FF84', font='Raleway 13 bold', borderwidth=1, relief="solid",width=20, command=switch)
    darkmodebtn.grid(row=5, columnspan=2, sticky='e', padx=35)

    pbar_frame = tk.Frame(root)
    pbar_frame.grid(row=6, columnspan=2)

    pbar = Progressbar(pbar_frame,orient='horizontal',length=1150,mode='determinate')
    pbar.grid(row=7,column=0, pady=(0,20))

    percent = tk.StringVar()

    percentlabel = tk.Label(root, textvariable=percent, font='Raleway 15')
    percentlabel.grid(row=5,columnspan=2,pady=10, padx=200, sticky='w')


# Menu Bar
def openweb():
    webbrowser.open('https://github.com/abhishake21/Encryption-App',1)
def aboutproj():
    tk.messagebox.showinfo('About',
'''This app Encrypts and Decrypts your files with a password and salt of your choice.\n
It uses cryptography library and PBKDF2(Password Based Key Derivation Function) to achieve it.\n
If you wanna learn more about how the app works the code can be found on my github.\n
This program is written in Python and uses Tkinter for its GUI.
Not the best looking but gets the job done :)''')
def openblog():
    webbrowser.open('https://hashnode.com/preview/61eedc11c99aed184e7278e5',1)


# DarkMode Function
global is_on
is_on = True
def switch():
    global is_on
    if is_on:
        darkmodeon()
        darkmodebtn.config(text='Turn Off Darkmode')
        is_on = False
    else:
        darkmodebtn.config(text='Turn On Darkmode')
        darkmodeoff()
        is_on = True

def darkmodeon():
    # File Frame
    fipasswordbox['bg']='#575757'
    fipasswordbox['fg']='white'
    fipasswordbox['insertbackground']='white'
    fisaltbox['bg']='#575757'
    fisaltbox['fg']='white'
    fisaltbox['insertbackground']='white'
    browsefi['bg']='#575757'
    browsefi['fg']='white'
    filistbox['bg']='#575757'
    filistbox['fg']='white'

    file_enc_button['bg']='#575757'
    file_enc_button['fg']='white'
    file_dec_button['bg']='#575757'
    file_dec_button['fg']='white'

    fipassword_lable['bg']='black'
    fipassword_lable['fg']='white'
    fisalt_lable['bg']='black'
    fisalt_lable['fg']='white'
    fi_selectfile_label['bg']='black'
    fi_selectfile_label['fg']='white'

    pb_lable['fg']='black'
    percentlabel['bg']='black'
    percentlabel['fg']='white'
    pbar_frame['bg']='black'

    root['bg']='black'
    fiframe['bg']='black'
    fiframe['fg']='white'
    filist_frame['bg']='black'
    fibutton_frame['bg']='black'


    # Folder Frame
    fopasswordbox['bg']='#575757'
    fopasswordbox['fg']='white'
    fopasswordbox['insertbackground']='white'
    fosaltbox['bg']='#575757'
    fosaltbox['fg']='white'
    fosaltbox['insertbackground']='white'
    browsefo['bg']='#575757'
    browsefo['fg']='white'
    folistbox['bg']='#575757'
    folistbox['fg']='white'

    fold_enc_button['bg']='#575757'
    fold_enc_button['fg']='white'
    fold_dec_button['bg']='#575757'
    fold_dec_button['fg']='white'

    fopassword_lable['bg']='black'
    fopassword_lable['fg']='white'
    fosalt_lable['bg'] = 'black'
    fosalt_lable['fg']='white'
    fo_selectfolder_label['bg']='black'
    fo_selectfolder_label['fg']='white'

    foframe['bg']='black'
    foframe['fg']='white'
    folist_frame['bg']='black'
    fobutton_frame['bg']='black'

    # HOVER COLOR CHANGE File buttons
    file_enc_button.bind("<Enter>", lambda e: file_enc_button.config(fg='white', bg='black'))
    file_enc_button.bind("<Leave>", lambda e: file_enc_button.config(fg='white', bg='#575757'))

    file_dec_button.bind("<Enter>", lambda e: file_dec_button.config(fg='white', bg='black'))
    file_dec_button.bind("<Leave>", lambda e: file_dec_button.config(fg='white', bg='#575757'))

    browsefi.bind("<Enter>", lambda e: browsefi.config(fg='white', bg='black'))
    browsefi.bind("<Leave>", lambda e: browsefi.config(fg='white', bg='#575757'))

    # HOVER COLOR CHANGE Fold buttons
    fold_enc_button.bind("<Enter>", lambda e: fold_enc_button.config(fg='white', bg='black'))
    fold_enc_button.bind("<Leave>", lambda e: fold_enc_button.config(fg='white', bg='#575757'))

    fold_dec_button.bind("<Enter>", lambda e: fold_dec_button.config(fg='white', bg='black'))
    fold_dec_button.bind("<Leave>", lambda e: fold_dec_button.config(fg='white', bg='#575757'))

    browsefo.bind("<Enter>", lambda e: browsefo.config(fg='white', bg='black'))
    browsefo.bind("<Leave>", lambda e: browsefo.config(fg='white', bg='#575757'))

def darkmodeoff():
    # File Frame
    fipasswordbox['bg']='white'
    fipasswordbox['fg']='black'
    fipasswordbox['insertbackground']='black'
    fisaltbox['bg']='white'
    fisaltbox['fg']='black'
    fisaltbox['insertbackground']='black'
    browsefi['bg']='#F0F0F0'
    browsefi['fg']='black'
    filistbox['bg']='white'
    filistbox['fg']='black'

    file_enc_button['bg']='#F0F0F0'
    file_enc_button['fg']='black'
    file_dec_button['bg']='#F0F0F0'
    file_dec_button['fg']='black'

    fipassword_lable['bg']='#F0F0F0'
    fipassword_lable['fg']='black'
    fisalt_lable['bg']='#F0F0F0'
    fisalt_lable['fg']='black'
    fi_selectfile_label['bg']='#F0F0F0'
    fi_selectfile_label['fg']='black'

    pb_lable['fg']='black'
    percentlabel['bg']='#F0F0F0'
    percentlabel['fg']='black'
    pbar_frame['bg']='#F0F0F0'

    root['bg']='#F0F0F0'
    fiframe['bg']='#F0F0F0'
    fiframe['fg']='black'
    filist_frame['bg']='#F0F0F0'
    fibutton_frame['bg']='#F0F0F0'

    # Folder Frame
    fopasswordbox['bg']='white'
    fopasswordbox['fg']='black'
    fopasswordbox['insertbackground']='black'
    fosaltbox['bg']='white'
    fosaltbox['fg']='black'
    fosaltbox['insertbackground']='black'
    browsefo['bg']='#F0F0F0'
    browsefo['fg']='black'
    folistbox['bg']='white'
    folistbox['fg']='black'

    fold_enc_button['bg']='#F0F0F0'
    fold_enc_button['fg']='black'
    fold_dec_button['bg']='#F0F0F0'
    fold_dec_button['fg']='black'

    fopassword_lable['bg']='#F0F0F0'
    fopassword_lable['fg']='black'
    fosalt_lable['bg']='#F0F0F0'
    fosalt_lable['fg']='black'
    fo_selectfolder_label['bg']='#F0F0F0'
    fo_selectfolder_label['fg']='black'

    foframe['bg']='#F0F0F0'
    foframe['fg']='black'
    folist_frame['bg']='#F0F0F0'
    fobutton_frame['bg']='#F0F0F0'

    # HOVER COLOR CHANGE File buttons
    file_enc_button.bind("<Enter>", lambda e: file_enc_button.config(fg='black', bg='#D0D0D0'))
    file_enc_button.bind("<Leave>", lambda e: file_enc_button.config(fg='black', bg='#F0F0F0'))

    file_dec_button.bind("<Enter>", lambda e: file_dec_button.config(fg='black', bg='#D0D0D0'))
    file_dec_button.bind("<Leave>", lambda e: file_dec_button.config(fg='black', bg='#F0F0F0'))

    browsefi.bind("<Enter>", lambda e: browsefi.config(fg='black', bg='#D0D0D0'))
    browsefi.bind("<Leave>", lambda e: browsefi.config(fg='black', bg='#F0F0F0'))

    # HOVER COLOR CHANGE Fold buttons
    fold_enc_button.bind("<Enter>", lambda e: fold_enc_button.config(fg='black', bg='#D0D0D0'))
    fold_enc_button.bind("<Leave>", lambda e: fold_enc_button.config(fg='black', bg='#F0F0F0'))

    fold_dec_button.bind("<Enter>", lambda e: fold_dec_button.config(fg='black', bg='#D0D0D0'))
    fold_dec_button.bind("<Leave>", lambda e: fold_dec_button.config(fg='black', bg='#F0F0F0'))

    browsefo.bind("<Enter>", lambda e: browsefo.config(fg='black', bg='#D0D0D0'))
    browsefo.bind("<Leave>", lambda e: browsefo.config(fg='black', bg='#F0F0F0'))


# Browse Button Function
def fibrowse():
    files = fd.askopenfilenames(parent=root, title='Choose files')
    for file in files:
        filistbox.insert('end', file)
def fobrowse():
    folders = fd.askdirectory(parent=root, title='Choose folders')
    for path, subdirs, filesa in os.walk(folders):
        for file in filesa:
            folistbox.insert('end' ,path+'/'+file)


# Errors Pop-up Messagebox
def fierrorbox():
    tk.messagebox.showerror('File Error','Select a file or files')
    fipasswordbox.delete(0,'end')
    fisaltbox.delete(0,'end')
    filistbox.delete(0,'end')

    fopasswordbox.delete(0,'end')
    fosaltbox.delete(0,'end')
    folistbox.delete(0,'end')
def foerrorbox():
    tk.messagebox.showerror('Folder Error','Select a folder')
    fipasswordbox.delete(0,'end')
    fisaltbox.delete(0,'end')
    filistbox.delete(0,'end')

    fopasswordbox.delete(0,'end')
    fosaltbox.delete(0,'end')
    folistbox.delete(0,'end')
def passerrorbox():
    tk.messagebox.showerror('Password Error','Enter a Password')
    fipasswordbox.delete(0,'end')
    fisaltbox.delete(0,'end')
    filistbox.delete(0,'end')

    fopasswordbox.delete(0,'end')
    fosaltbox.delete(0,'end')
    folistbox.delete(0,'end')

def fiwrongpass():
    tk.messagebox.showerror('Error Try Again','Something went wrong.\n\n1.  Wrong Password and/or Salt Entered.\n\tOR\n2.  Check if correct file is selected.')
    pbar['value']=0
    percent.set('0%')

    fold_enc_button['state']='active'
    fold_dec_button['state']='active'
    browsefo['state']='active'

    file_enc_button['state']='active'
    file_dec_button['state']='active'
    browsefi['state']='active'

    fipasswordbox['state']='normal'
    fisaltbox['state']='normal'

    fopasswordbox['state']='normal'
    fosaltbox['state']='normal'

    fipasswordbox.delete(0,'end')
    fisaltbox.delete(0,'end')
    filistbox.delete(0,'end')

    fopasswordbox.delete(0,'end')
    fosaltbox.delete(0,'end')
    folistbox.delete(0,'end')
def fowrongpass():
    tk.messagebox.showerror('Error Try Again','Something went wrong.\n\n1.  Wrong Password and/or Salt Entered.\n\tOR\n2.  Check if correct folder is selected.')
    pbar['value']=0
    percent.set('0%')

    fold_enc_button['state']='active'
    fold_dec_button['state']='active'
    browsefo['state']='active'

    file_enc_button['state']='active'
    file_dec_button['state']='active'
    browsefi['state']='active'

    fipasswordbox['state']='normal'
    fisaltbox['state']='normal'

    fopasswordbox['state']='normal'
    fosaltbox['state']='normal'

    fipasswordbox.delete(0,'end')
    fisaltbox.delete(0,'end')
    filistbox.delete(0,'end')

    fopasswordbox.delete(0,'end')
    fosaltbox.delete(0,'end')
    folistbox.delete(0,'end')


# Done Pop-up Messagebox
def fiencdone():
    tk.messagebox.showinfo('Done','All Files Encrypted')
    fipasswordbox['state']='normal'
    fisaltbox['state']='normal'

    fopasswordbox['state']='normal'
    fosaltbox['state']='normal'

    fipasswordbox.delete(0,'end')
    fisaltbox.delete(0,'end')
    filistbox.delete(0,'end')

    fopasswordbox.delete(0,'end')
    fosaltbox.delete(0,'end')
    folistbox.delete(0,'end')

    pbar['value']=0
    percent.set('0%')

    fold_enc_button['state']='active'
    fold_dec_button['state']='active'
    browsefo['state']='active'

    file_enc_button['state']='active'
    file_dec_button['state']='active'
    browsefi['state']='active'
def foencdone():
    tk.messagebox.showinfo('Done','Folder Encrypted')
    fipasswordbox['state']='normal'
    fisaltbox['state']='normal'

    fopasswordbox['state']='normal'
    fosaltbox['state']='normal'

    fipasswordbox.delete(0,'end')
    fisaltbox.delete(0,'end')
    filistbox.delete(0,'end')

    fopasswordbox.delete(0,'end')
    fosaltbox.delete(0,'end')
    folistbox.delete(0,'end')

    pbar['value']=0
    percent.set('0%')

    fold_enc_button['state']='active'
    fold_dec_button['state']='active'
    browsefo['state']='active'

    file_enc_button['state']='active'
    file_dec_button['state']='active'
    browsefi['state']='active'
def fidecdone():
    tk.messagebox.showinfo('Done','All Files Decrypted')
    fipasswordbox['state']='normal'
    fisaltbox['state']='normal'

    fopasswordbox['state']='normal'
    fosaltbox['state']='normal'

    fipasswordbox.delete(0,'end')
    fisaltbox.delete(0,'end')
    filistbox.delete(0,'end')

    fopasswordbox.delete(0,'end')
    fosaltbox.delete(0,'end')
    folistbox.delete(0,'end')

    pbar['value']=0
    percent.set('0%')

    fold_enc_button['state']='active'
    fold_dec_button['state']='active'
    browsefo['state']='active'

    file_enc_button['state']='active'
    file_dec_button['state']='active'
    browsefi['state']='active'
def fodecdone():
    tk.messagebox.showinfo('Done','Folder Decrypted')
    fipasswordbox['state']='normal'
    fisaltbox['state']='normal'

    fopasswordbox['state']='normal'
    fosaltbox['state']='normal'

    fipasswordbox.delete(0,'end')
    fisaltbox.delete(0,'end')
    filistbox.delete(0,'end')

    fopasswordbox.delete(0,'end')
    fosaltbox.delete(0,'end')
    folistbox.delete(0,'end')

    pbar['value']=0
    percent.set('0%')

    fold_enc_button['state']='active'
    fold_dec_button['state']='active'
    browsefo['state']='active'

    file_enc_button['state']='active'
    file_dec_button['state']='active'
    browsefi['state']='active'


# File Encryption Button Function
def encfile():
    password = bytes(fipasswordbox.get(), 'utf-8')
    salt = bytes(fisaltbox.get(),'utf-8')
    fileln = filistbox.get(0,'end')

    def enc():
        task = len(fileln)
        x = 0
        if len(fileln) == 0:
            fierrorbox()
        elif len(password) == 0:
            passerrorbox()
        else:
            fold_enc_button['state']='disabled'
            fold_dec_button['state']='disabled'
            browsefo['state']='disabled'

            file_enc_button['state']='disabled'
            file_dec_button['state']='disabled'
            browsefi['state']='disabled'

            fipasswordbox['state']='disabled'
            fisaltbox['state']='disabled'

            fopasswordbox['state']='disabled'
            fosaltbox['state']='disabled'
            while (x<task):
                kdf = PBKDF2HMAC(
                    algorithm=hashes.SHA256(),
                    length=32,
                    salt=salt,
                    iterations=100000,
                    backend=default_backend())

                key = base64.urlsafe_b64encode(kdf.derive(password))
                f = Fernet(key)

                for file in fileln:
                    with open(file,'rb') as original_file:
                        original = original_file.read()

                    encrypted = f.encrypt(original)

                    with open (file,'wb') as encrypted_file:
                        encrypted_file.write(encrypted)
                    pbar['value']+=100/task
                    x+=1
                    percent.set(str(int((x/task)*100))+'%')
                    root.update_idletasks()

                fiencdone()

    def threadingst():
        trd=threading.Thread(target=enc)
        trd.start()

    threadingst()

# File Decryption Button Function
def decfile():
    password = bytes(fipasswordbox.get(), 'utf-8')
    salt = bytes(fisaltbox.get(),'utf-8')
    fileln = filistbox.get(0,'end')

    def dec():
        task = len(fileln)
        x = 0
        if len(fileln) == 0:
            fierrorbox()
        elif len(password) == 0:
            passerrorbox()
        else:
            fold_enc_button['state']='disabled'
            fold_dec_button['state']='disabled'
            browsefo['state']='disabled'

            file_enc_button['state']='disabled'
            file_dec_button['state']='disabled'
            browsefi['state']='disabled'

            fipasswordbox['state']='disabled'
            fisaltbox['state']='disabled'

            fopasswordbox['state']='disabled'
            fosaltbox['state']='disabled'

            while (x<task):
                try:
                    kdf = PBKDF2HMAC(
                        algorithm=hashes.SHA256(),
                        length=32,
                        salt=salt,
                        iterations=100000,
                        backend=default_backend())

                    key = base64.urlsafe_b64encode(kdf.derive(password))
                    f = Fernet(key)

                    for file in fileln:
                        with open(file,'rb') as original_file:
                            original = original_file.read()

                        decrypted = f.decrypt(original)

                        with open (file,'wb') as decrypted_file:
                            decrypted_file.write(decrypted)
                        pbar['value']+=100/task
                        x+=1
                        percent.set(str(int((x/task)*100))+'%')
                        root.update_idletasks()

                    fidecdone()
                except:
                    fiwrongpass()
                break

    def threadingst():
        trd=threading.Thread(target=dec)
        trd.start()

    threadingst()

# Folder Encryption Button Function
def encfolder():
    password = bytes(fopasswordbox.get(), 'utf-8')
    salt = bytes(fosaltbox.get(),'utf-8')
    folderln = folistbox.get(0,'end')

    def enc():
        task = len(folderln)
        x = 0

        if len(folderln) == 0:
            foerrorbox()
        elif len(password) == 0:
            passerrorbox()
        else:
            fold_enc_button['state']='disabled'
            fold_dec_button['state']='disabled'
            browsefo['state']='disabled'

            file_enc_button['state']='disabled'
            file_dec_button['state']='disabled'
            browsefi['state']='disabled'

            fipasswordbox['state']='disabled'
            fisaltbox['state']='disabled'

            fopasswordbox['state']='disabled'
            fosaltbox['state']='disabled'
            while (x<task):
                kdf = PBKDF2HMAC(
                    algorithm=hashes.SHA256(),
                    length=32,
                    salt=salt,
                    iterations=100000,
                    backend=default_backend())

                key = base64.urlsafe_b64encode(kdf.derive(password))
                f = Fernet(key)

                for file in folderln:
                    with open(file,'rb') as original_file:
                        original = original_file.read()

                    encrypted = f.encrypt(original)

                    with open(file,'wb') as encrypted_file:
                        encrypted_file.write(encrypted)

                    pbar['value']+=100/task
                    x+=1
                    percent.set(str(int((x/task)*100))+'%')
                    root.update_idletasks()

                foencdone()

    def threadingst():
        trd=threading.Thread(target=enc)
        trd.start()

    threadingst()

# Folder Encryption Button Function
def decfolder():
    password = bytes(fopasswordbox.get(), 'utf-8')
    salt = bytes(fosaltbox.get(),'utf-8')
    folderln = folistbox.get(0,'end')

    def dec():
        task = len(folderln)
        x = 0

        if len(folderln) == 0:
            foerrorbox()
        elif len(password) == 0:
            passerrorbox()
        else:
            fold_enc_button['state']='disabled'
            fold_dec_button['state']='disabled'
            browsefo['state']='disabled'

            file_enc_button['state']='disabled'
            file_dec_button['state']='disabled'
            browsefi['state']='disabled'

            fipasswordbox['state']='disabled'
            fisaltbox['state']='disabled'

            fopasswordbox['state']='disabled'
            fosaltbox['state']='disabled'
            while (x<task):
                try:
                    kdf = PBKDF2HMAC(
                        algorithm=hashes.SHA256(),
                        length=32,
                        salt=salt,
                        iterations=100000,
                        backend=default_backend())

                    key = base64.urlsafe_b64encode(kdf.derive(password))
                    f = Fernet(key)

                    for file in folderln:
                        with open(file,'rb') as original_file:
                            original = original_file.read()

                        decrypted = f.decrypt(original)

                        with open(file,'wb') as decrypted_file:
                            decrypted_file.write(decrypted)

                        pbar['value']+=100/task
                        x+=1
                        percent.set(str(int((x/task)*100))+'%')
                        root.update_idletasks()

                    fodecdone()
                except:
                    fowrongpass()
                break

    def threadingst():
        trd=threading.Thread(target=dec)
        trd.start()

    threadingst()


# Main App
root = tk.Tk()

root.resizable(False,False)
root.title('Encryption App')
fileframe()
folderframe()
progbar()
percent.set('0%')
darkmodeon()

my_menu = tk.Menu(root)
about_menu = tk.Menu(my_menu, tearoff=0)

my_menu.add_cascade(label='Help', menu=about_menu)
about_menu.add_command(label='About the app', command=aboutproj)
about_menu.add_command(label='Project code on Github', command=openweb)
about_menu.add_command(label='Project Blog', command=openblog)
root.config(menu=my_menu)

root.mainloop()
