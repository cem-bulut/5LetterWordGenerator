import random

f = open("demofile.txt", "w")

alphabet = ["a","b","c","ç","d","e","f","g","ğ","h","ı","i","j","k","l","m","n","o","ö","p","r","s","ş","t","u","ü","v","y","z"]
vowelIndex = [0,5,10,11,17,18,24,25]
consonantIndex = [1,2,3,4,6,7,8,9,12,13,14,15,16,19,20,21,22,23,26,27,28]

vowels = []
consonants = []

for i in range(100000):
    for i in vowelIndex:
        vowels.append(alphabet[i])

    for i in consonantIndex:
        consonants.append(alphabet[i])

    firstLetterSelect = random.randint(0,1)
    if firstLetterSelect == 0:
        firstLetter = random.choice(vowels)
        firstLetterIndex = vowels.index(firstLetter)
        vowels.pop(firstLetterIndex)

    else:
        firstLetter = random.choice(consonants)
        while True:
            if firstLetter == consonants[6]:
                firstLetter = random.choice(consonants)
            else:
                break
        firstLetterIndex = consonants.index(firstLetter)
        consonants.pop(firstLetterIndex)

    if firstLetterSelect == 0:
        secondLetterSelect = 1
    elif firstLetterSelect == 1:
        secondLetterSelect = 0

    if secondLetterSelect == 0:
        secondLetter = random.choice(vowels)
        secondLetterIndex = vowels.index(secondLetter)
        vowels.pop(secondLetterIndex)

    else:
        secondLetter = random.choice(consonants)
        secondLetterIndex = consonants.index(secondLetter)
        consonants.pop(secondLetterIndex)

    if secondLetterSelect == 0:
        thirdLetterSelect = 1
    elif secondLetterSelect == 1:
        thirdLetterSelect = 0

    if thirdLetterSelect == 0:
        thirdLetter = random.choice(vowels)
        thirdLetterIndex = vowels.index(thirdLetter)
        vowels.pop(thirdLetterIndex)

    else:
        thirdLetter = random.choice(consonants)
        thirdLetterIndex = consonants.index(thirdLetter)
        consonants.pop(thirdLetterIndex)

    if thirdLetterSelect == 0:
        forthLetterSelect = 1
    elif thirdLetterSelect == 1:
        forthLetterSelect = 0

    if forthLetterSelect == 0:
        forthLetter = random.choice(vowels)
        forthLetterIndex = vowels.index(forthLetter)
        vowels.pop(forthLetterIndex)

    else:
        forthLetter = random.choice(consonants)
        forthLetterIndex = consonants.index(forthLetter)
        consonants.pop(forthLetterIndex)

    if forthLetterSelect == 0:
        fifthLetterSelect = 1
    elif forthLetterSelect == 1:
        fifthLetterSelect = 0

    if fifthLetterSelect == 0:
        fifthLetter = random.choice(vowels)
        fifthLetterIndex = vowels.index(fifthLetter)
        vowels.pop(fifthLetterIndex)

    else:
        fifthLetter = random.choice(consonants)
        fifthLetterIndex = consonants.index(fifthLetter)
        consonants.pop(fifthLetterIndex)

    word = (firstLetter.capitalize() + secondLetter.capitalize() + thirdLetter.capitalize() + forthLetter.capitalize() + fifthLetter.capitalize())
    f = open("demofile.txt", "a")
    f.write(word + "\n")
    f.close()