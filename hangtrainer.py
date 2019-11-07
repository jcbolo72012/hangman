import random
import xlsxwriter
def remove_values_from_list(the_list, val):
   return [value for value in the_list if value != val]
word_val =[]
with open("engmix.txt","r") as d:
    for entry in d:
        words = []

        with open('test.txt', 'r') as f:
            line = f.readline().strip()
            while line:
                words.append(line)
                line = f.readline().strip()
        length = len(words)-1
        word = entry.strip()
        word = word.lower()
        guess = []
        alph=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
        alph2=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
        total=[]
        for i in alph:
            filename = i + "\\" + i + ".txt"
            with open(filename, 'r') as f:
                value = f.readline()
            value = int(value)
            value = value + 1
            for x in range(0, value):
                total.append(i)
        for i in range(0, len(word)):
            guess.append("_")
        print("welcome to Hangman!")
        bodyparts = 0
        incorrect = ""
        guesser=""

        while guesser != word:
            guessprint = ""

            for i in guess:
                guessprint = guessprint + i + " "
                lent = len(total) - 1
            guessletter = total[random.randint(0,lent)]
            print("I guess " + guessletter)
            if guessletter in word:

                for i in alph:
                    filename = guessletter + "\\" + i + ".txt"
                    with open(filename, 'r') as f:
                        value = f.readline()
                    value = int(value)
                    value = value + 1
                    for x in range(0, value):
                        if i not in incorrect:
                            total.append(i)

                location = []
                location = [pos
                    for pos, char in enumerate(word) if char == guessletter]
                guesslen = len(guess)
                for i in location:
                    guess[i] = guessletter
                guessprint=""


                for i in guess:
                    guessprint = guessprint + i + " "
                guesser = ""
                for i in guess:
                    guesser = guesser + i
                print("correct! " + guessprint)




            else:
                print(guessletter + " is not in the string")

                bodyparts=bodyparts+1
            total[:] = (value for value in total if value != guessletter)
            print("correct! " + guessprint)
            incorrect = incorrect + guessletter + ", "
# strengthen associations
        guessprint2 = guessprint.replace(" ","")
        guessprint3 = guessprint2
        for i in guessprint3:
            for j in guessprint2:
                
                filename = j + "\\" + i + ".txt"
                with open(filename, 'r') as f:
                    value = f.readline()
                value = int(value)
                value = value + 1
                val = str(value)
                with open(filename, 'w') as f:
                    f.write(val)

        for each in word:
            incorrect = incorrect.replace(each, "")
        tries = str(len(incorrect.replace(", ", "")))
        message = "word: " + word + ", tries: " + tries
        with open("test.txt", "a") as q:
            q.write(message)
            q.write('\n')
        en = [word, tries]
        word_val.append(en)

workbook = xlsxwriter.Workbook('hangmantraining.xlsx')
worksheet = workbook.add_worksheet()

row = 0
col = 0

# Iterate over the data and write it out row by row.
for w, t in (word_val):
    worksheet.write(row, col,     w)
    worksheet.write(row, col + 1, t)
    row += 1

# Write a total using a formula.


workbook.close()