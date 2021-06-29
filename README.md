# Encryption-App
A simple python program that lets you Encrypt and Decrypt files and folders using a password and salt of your choice.                            
So far tested with txt / png / jpeg / json / html / csv / zip / mp3 / mp4 / pdf

I have created a GUI App and a CLI version as well. At first i just created a simple CLI version but then i got tired of typing the full path of the files one by one and so i created a GUI app for it. I personally prefer GUI cause its very easy to just run the exe and encrypt files and folder.

## The only problem with the GUI app is that it might trigger your Windows Defender or Antivirus so you might have to create an exclusion for the app.

Both the programs are written in python and the GUI app is made using Tkinter. If you wanna know how the encryption works behind the app then check out the [blog](https://medium.com/@abhishake21) i wrote about how the code works. 

Basically uses:
* cryptography library - https://pypi.org/project/cryptography/
* PBKDF2 explained in this video - https://youtu.be/cMykd0jScSY?t=234

I have also added Jupyter notebooks for clearer understanding of the code.

Below are videos of how the app works.
