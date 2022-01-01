# import main
User_input = input('Enter a sentence to count: ')
count = dict()
Words = User_input.split(' ' or '\n')
word_list = []
for word in Words:
    word_list.append(word.lower())
for word in word_list:
    if word in count:
        count[word] += 1
    else:
        count[word] = 1
# print(count)
# print(word_list)
for word in count:
    print(f'{word}: {count[word]}')