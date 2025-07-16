import os

path = "C:\\Users\\path\\Desktop\\test.txt"

if os.path.exists(path):
    print("Finns")
    if os.path.isfile(path):
        print("file")
else:
    print("Finns inte")