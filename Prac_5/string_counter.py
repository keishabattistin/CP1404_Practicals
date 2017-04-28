user_input = input('Enter String: ')

user_words = user_input.split()

STRING_OCCURANCES = {}

for words in user_words:
    STRING_OCCURANCES.update({words: str(user_words.count(words))})

sort = sorted(STRING_OCCURANCES)
print("Text: ", user_input)

for i in sort:
    print("{:{}} : {}".format(i, len(max(sort)) + 6, STRING_OCCURANCES[i]))
