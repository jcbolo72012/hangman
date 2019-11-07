import os
alph=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
alph2=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
p = os.getcwd()

for i in alph:
   for j in alph2:
       j = j + ".txt"
       filename = os.path.join(p,i, j)
       with open(filename, 'w') as f:
          f.write('0')