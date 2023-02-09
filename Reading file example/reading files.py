# My example code for work placement - ERIC TYERMAN
# This program will write random letters to a file, amount specified by the user.
# It will then take a 3 letter input from the user and tell if the user's combination has appeared in the array

import random

# Creating array of letters that can be written to the file
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
letterAmount = int(input("How many letters do you want to read from?: "))
l1positions = []
l2positions = []
wordPositions = []

# Checking if the amount specified by user is valid
while letterAmount < 0:
    letterAmount = int(input("Please pick an amount above 0: "))

word = input("Using 3 letters, what letters would you like to search for? Place one space between each letter: ")
l = word.split(" ")

# Checking if the amount specified by user is valid
while len(l) < 3 or len(l) > 3:
    word = input("Please use 3 letters. Place one space between each letter: ")
    l = word.split(" ")
    
print("Your 3 letters are:", l)

file = open("Letters.txt", "w")

# Writes letters to file, seperating them with a empty space
for i in range(letterAmount):
    file.write(alphabet[random.randint(0,25)]+" ")

file.close()

file = open("Letters.txt")

# Splits the letters in the file into an array using the empty space as an indicator as to where to split into individual elements
lines = file.readline()
data = lines.split(" ")

letter1Count = 0
letter2Count = 0
count = 0
for i in range(len(data)):
    # if a letter in the array matches with the first letter of the combination, the algorithm moves onto the next part
    if data[i] == l[0]:
        letter1Count += 1
        l1positions.append(i)
        if data[i+1] == l[1] and len(l) > 1:
            letter2Count += 1
            l2positions.append(i)
            if data[i+2] == l[2] and len(l) > 2:
                count += 1
                wordPositions.append(i)

# Outputs how many times the word appears, the first letter appears, and the first and second letter next to each other appears
print(word, "appeared", count, "times in the array at positons", wordPositions,"\n")
print(l[0], "appeared", letter1Count, "times in the array at positons", l1positions,"\n")
print(l[0], "and", l[1], "appeared", letter2Count, "times in the array at positions", l2positions,"\n")
print("The array is shown below", "\n")
print(data)

file.close()
