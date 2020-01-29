import string

# Open text file in reading mode
file = "J. K. Rowling - Harry Potter and the Chamber of Secrets.txt"
document = open(file, "r")
# initilise empty dictionary
dict = dict()
totalWordCount = 0

def stripForWord(word):
    return word.lower().strip().strip(string.punctuation)


for line in document:
    for word in line.split():
        # skip none
        if word == "":
            continue
        # counting total words
        totalWordCount += 1
        # clean up
        word = stripForWord(word)


        # counting unique word
        try:
            dict[word] += 1
        except:
            dict[word] = 1

sorted = sorted(dict, key=lambda x: dict[x], reverse=True)

print(dict, "\n")
x = 20
print(f"Word Count Ranking Top {x}: ")
for i in sorted:
    if x > 0:
        x -= 1
        print(f"{i}  |  {dict[i]}")
    else:
        break
print(f"Total Word Count: {totalWordCount}")
print(f"Number of Unique Words: {len(dict)}")
