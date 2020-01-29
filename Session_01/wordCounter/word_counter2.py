import string

# Open text file in reading mode
file = "Doc1.txt"
content = open(file, "r")

# initialise empty dictionary
dict = dict()
# initialise a total word counter
totalWordCount = 0


def removeWhitespaces(target):
    """
    this function takes in a string, and returns it after removing all
    leading and trailing whitespeces

    logic: to find a starting index and ending index to slice the string
    """
    # initialise start and end variable
    start = 0
    end = len(target)
    # find the first non-space char
    for i in range(end):
        if target[i] != " ":
            start = i
            break
    # find the last non-space char
    while end >= 1:
        if target[end - 1] != " ":
            break
        end -= 1
    # slice the string and return
    return target[start:end]


def removePunctuations(target):
    """
    this function takes in a string, and returns it after removing all
    leading and trailing punctuations

    string.punctuation !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~

    logic: to find a starting index and ending index to slice the string
    """
    # initialise start and end variable
    start = 0
    end = len(target)
    # find the first non-punctuation char
    for i in range(end):
        if target[i] not in string.punctuation:
            start = i
            break
    # find the last non-punctuation char
    while end >= 1:
        if target[end - 1] not in string.punctuation:
            break
        end -= 1
    # slice the string and return
    return target[start:end]


def stripWord(word):
    """
    Make string lower case
    Remove leading and trailing whitespeces and Punctuations
    """
    return removePunctuations(removeWhitespaces(word.lower()))


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
