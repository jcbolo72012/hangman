import os
from os import system, name

def createFiles():
    dir = os.path.dirname(__file__)
    if os.path.isfile(dir+"\\a\\a.txt"):
        print("file system exists- moving on")
    else:
        print("no filesystem detected, here goes!")
        alph = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        alph2 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y', 'z']
        for i in alph:
            path = "\\" + i
            try:

                os.makedirs(dir+path)
            except OSError:
                print("Creation of the directory %s failed" % path)
            else:
                print("Successfully created the directory %s " % path)
            for j in alph2:
                f = open(dir+path+"\\"+j+".txt", "w+")
                f.write('0')
                f.close()
    # for windows
    if name == 'nt':
        _ = system('cls')

        # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')




