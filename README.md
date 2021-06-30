# Encryption-App
A simple python program that lets you Encrypt and Decrypt files and folders using a password and salt of your choice.                            
So far tested with txt / png / jpeg / json / html / csv / zip / mp3 / mp4 / pdf

I have created a GUI App and a CLI version as well. At first, i just created a simple CLI version but then i got tired of typing the full path of the files one by one and so i created a GUI app for it. I have included both versions, so use which ever you like. I prefer GUI cause its very easy to just run the exe and encrypt files and folder.

![Encryption App](https://user-images.githubusercontent.com/67749693/123956857-c82cd500-d9c8-11eb-8f7b-4d86b5b6a30b.png)

## The only problem with the GUI app is that it might trigger your Windows Defender or Antivirus so you might have to create an exclusion for the app.
If you dont want do that then copy the code and install `auto-py-to-exe` - https://pypi.org/project/auto-py-to-exe/ and convert the .py file into exe.

Follow this video - https://www.youtube.com/watch?v=Y0HN9tdLuJo to convert py to exe

Now when you press Encrypt/Decrypt button you might also encounter a dialogue box like [this](https://user-images.githubusercontent.com/67749693/123821128-c4417a00-d918-11eb-9744-0504a008a13c.png) from your AV in my case Norton. Just press `View Details` and then `Exclude Process` in [Action tab](https://user-images.githubusercontent.com/67749693/123821118-c3104d00-d918-11eb-864f-dea50c14e0f1.png) and rerun the app. This process might differ from AV to AV.
#

Both programs are written in python and the GUI app is made using Tkinter. If you want to know how the encryption works behind the app then check out the blog i wrote about how the code works.

Blog - https://medium.com/@abhishake21

Basically uses:
* Cryptography library - https://pypi.org/project/cryptography/
* PBKDF2 explained in this video - https://youtu.be/cMykd0jScSY?t=234

I have also added Jupyter notebooks for clear understanding of the code.
#

Below are videos of how the app works.
* GUI App - https://www.youtube.com/watch?v=ZhcIAd3owko
* Python CLI - https://www.youtube.com/watch?v=YaxM0zI9x1A
