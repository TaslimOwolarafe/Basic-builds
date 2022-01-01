listed = ['Be', 'strong', 'programming', 'is', 'not', 'for', 'the', 'weak']
lengths = []
short = 'The shortest word is:\n'
long = 'The longest word is:\n'
for word in listed:
    lengths.append(len(word))
    x = max(lengths)
    y = min(lengths)
for word in listed:
    if len(word) == x:
        long += str(word) + f' = {str(x)}\n'
        # print(f'Longest word:\n{word}')
for word in listed:
    if len(word) == y:
        short += str(word) + f' = {str(y)}\n'
print(short)
print(long)
        # print(f'Shortest word: \n {word}')
# print(x, y)
# print(min(lengths))
#print(lengths)