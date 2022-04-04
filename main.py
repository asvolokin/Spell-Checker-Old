import time

tic = time.perf_counter()
dictionary = {}
nouns = {}
with open('dictionary.txt') as dic:
    for words in dic:
        words = words.strip().lower()  # by stripping the line after of each word, it reduces the complexity to O(1)
        dictionary[words] = words
with open('nouns.txt') as dic:
    for words in dic:
        words = words.strip().lower()  # by stripping the line after each word, it reduces the complexity to O(1)
        nouns[words] = words


def possessive_nouns(f):
    r = r"'s"
    for word in f:
        if r in word:
            k = word.replace(r, '')
            if k in nouns:
                f.remove(word)


def plural_possessive_nouns(f):
    r = r"s'"
    for word in f:
        if r in word:
            k = word.replace(r, '')
            if k in nouns:
                f.remove(word)


def text(f):
    f = open(f, encoding='utf8')
    contents = f.read()
    f.close()
    spelling_errors = []
    contents = contents.lower()
    for p in """,.<>?/;:"[]{}|=_+)(*&^%$#@!`~""":  # gets rid of all punctuation
        contents = contents.replace(p, '')
    contents = contents.split()
    for word in contents:
        if word in dictionary:
            continue
        else:
            spelling_errors.append(word)
    possessive_nouns(spelling_errors)
    plural_possessive_nouns(spelling_errors)
    return spelling_errors


toc = time.perf_counter()

print(toc-tic)
print(text('test.txt'))
