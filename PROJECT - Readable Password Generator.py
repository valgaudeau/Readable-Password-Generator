# The aim of this project is to build a program that will generate passwords that resemble real letter combinations in order to make them easier to remember.
# To do that, the program first begins by recording the frequency at which one letter follows letter (or special characters - includes ".", ",", "!" etc.) from a text.
# We record this within a central 3-dimensional structure, which is then used to produce the random passwords.
# The logic behind building this project is that it's close to real world applications. For instance, this idea can be used to make auto-correctors on phones.
# Phones have very little processing power and storing space, and have to work with efficient algorithms that don't take much memory.

import random

text_open = open("alice_in_wonderland.txt", "r")
text_read = text_open.read()

array0 = []

# First we're going to establish which characters we allow in our final result:
character_universe = []
for i in range(97, 123):
    character_universe.append(chr(i))

for letter in text_read:
    if letter.lower() in character_universe:
        array0.append(letter.lower())

array = []

# We have to create the central structure which will be used for this program.
# We need a 3-dimensional structure. The first dimension stores all of the unique characters encountered in the text.
# The second dimension stores each character which followed those unique characters, and how many times they appeared.
# The third dimension stores how many times in the text each unique character appeared.
# To give an example, here is the output with the word "helloeee":
# h(1) e(1)
# e(4) l(1) e(2)
# l(2) l(1) o(1)
# o(1) e(1)
# This shows each unique character, how many times they showed up, and then the letters that followed those unique characters and how many times those showed up.
# Dimension 1 can be thought of as x, dimension 2 y, and dimension 3 z (depth for visualisation - see drawn representation in journal)

for idx, letter in enumerate(array0):
# This goes through the list and stores the index of each character which is stored in the first dimension of our array.
    found = False
    for i in range(len(array)):
        if array[i][0][0] == letter:
            found = True
            break
            # We need to break here, because we want to keep the value of the i the same as when we found the value == letter. Otherwise it will keep looping, and the value of i changes.
            # This is important because we have to keep the value of i the same for when we add "+1" to the second dimension in the else statement.
    print("letter = ", letter, "found = ", found)
    # This print information is for debugging purposes to see what's going on

    if not found:
        dummy = [[letter, 1]]
        array.append(dummy)
    else:
    # If we find that the letter is already in the first dimension, we add "+1" in the third dimension at the position i.
        print("position = ", i)
        array[i][0][1] = array[i][0][1] + 1
    # This else statement is really like a "found" statement. The reason it's after the "if not" found is because logically, when we loop through the array,
    # the first situation that happens is that we don't find the character we're looking for in the first dimension. After we don't find it, it goes to the "if not found" part of the code and appends the dummy array.
    # The code above in the for loop fills the first and third dimensions of the array.
    # Now we have to fill the second dimension - THIS IS STILL PART OF THE FOR LOOP ABOVE.
    if idx < len(array0)-1:
    # We have to write this because the last letter doesn't have anything that follows, therefore Python would report index out of bound.
        next_letter = array0[idx+1]
        # We look at the characters that follows the character we're looking at - Therefore "idx+1"
        for x in range(len(array)):
            if array[x][0][0] == letter:
                found = True
                break
        # So we look for the position of letter in our first dimension and we break.
        # We then use that information to print the position of x and have the value of x in the for loop below.
        print("x = ", end='')
        print(x)

        found = False
        # The logic of the loop below is the following: We use the stored value of x which loops through letters, and we ask:
        # "Hey, for that position x in D1, does the y or D2 hold next letter (which is idx+1) anywhere? If yes, we break. If not, we have to append next letter to D2 at that position of D1.
        # Remember that we're working with lists of lists, so D2 depends on D1 or x for its content.
        for y in range(1, len(array[x])):
            if array[x][y][0] == next_letter:
                found = True
                break

        if not found:
            dummy = [next_letter, 1]
            array[x].append(dummy)
        else:
            array[x][y][1] = array[x][y][1] + 1


# inefficient because we're going through everything again. But it's easier to understand that way.
# We start a range 1 because the first character in the second dimension is the character itself. Don't have to check for it again.

print('')

for i in range(len(array)):
    for e in range(len(array[i])):
        print(array[i][e][0], end='(')
        print(array[i][e][1], end=') ')
    print('')

print('')

print(array)

# Now we have to create the password based off the structure we created.
Max_X = len(array)-1
# The length of the array is the number of rows that we have in our 3-dimensional array (refer to previous example for word "helloeee").
New_X = random.randint(0, Max_X)
random_letter = array[New_X][0][0]

print("Max_X = ", end='')
print(Max_X)
print('')
print("RESULT")


for times2 in range(19):
# This controls how many words we want to output.
    result = random_letter
    newletter = random_letter

    for times in range(14):
    # This controls how many characters our final output will have.
        for i in range(Max_X):
            if array[i][0][0] == newletter:
                break
        New_X = i

        Max_Y = array[New_X][0][1] - 1
        New_Y = random.randint(0, Max_Y)

        # The logic behind what comes next is the following:
        # We have the count of how many times each character shows up in the text in total. This tells us how many following characters have been recorded.
        # Therefore, we can use this to determine the probability of the character which follows.
        # So, if we have "a" which is followed 5 times by "t" and 10 times by "i", we generate a random integer between 1 and 15, and we use that to pick the following character.
        # This is why we needed the third dimension which records how many time each character shows up in the text. This is an efficient method memory wise.

        s = 0
        for i in range(1, len(array[New_X]) - 1):
        # We start at range 1 because the first character (at index 0) is going to be the same as the one we're looking for.
            s = s + array[New_X][i][1]
            if s > New_Y:
                break
        New_Y = i

        newletter = array[New_X][New_Y][0]
        result = result + newletter

    print(result)

# The next level to this project is to have structures which records structures of words.
# In other words, if you want to improve the "humanization" of the output, you have the structure remember that "o" is often followed by by "he".
# Also, we could use syllables to create new word combinations. To do this, we can connect to a word API which can return syllables for us rather than having to write an algorithm.
