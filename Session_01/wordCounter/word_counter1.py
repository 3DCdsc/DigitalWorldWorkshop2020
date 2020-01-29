import string

# Open text file in reading mode
file = "Doc1.txt"
content = open(file, "r")

# initialise empty dictionary
dict = dict()
# initialise a total word counter
totalWordCount = 0


def stripWord(word):
    """
    Make string lower case
    Remove leading and trailing whitespeces and Punctuations
    """
    return word.lower().strip().strip(string.punctuation)


# traversing content line by line
for line in content:
    # traversing strings splitted by string.split()
    for word in line.split():
        # skip empty strings, None, and whitespece
        if word in ("", " ", None):
            continue

        # increment total word count by 1
        totalWordCount += 1

        # clean up the word
        word = stripWord(word)

        # if the word already exist in the dictionary
        if dict[word]:
            # increment the word count by 1
            dict[word] += 1
        # else, if the word does not exist in the dictionary
        else:
            # add the word to the dictionary, and set the word count to 1
            dict[word] = 1

# sort the words(keys) in the dictionary by the no. of occurrences(values)
sortedKeys = sorted(dict, key=lambda x: dict[x], reverse=True)

# print out the whole dictionary
print(dict, "\n")

# print Top x of most frequently used words
x = 20
print(f"Word Count Ranking Top {x}: ")
for i in sortedKeys:
    if x > 0:
        x -= 1
        print(f"{i}  |  {dict[i]}")
    else:
        break

# print no. of total words and unique words
print(f"Total Word Count: {totalWordCount}")
print(f"Number of Unique Words: {len(dict)}")
