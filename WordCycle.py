from num2words import num2words
# installed num2words
# install num2words from packages
loop_position = 1
Alpha = 1
cont = 0
end2 = 1
Sent = input('Enter a sentence to cycle: ')
x = ' '
for word in Sent:
    each = Sent.split()
for order in range(len(each)):
    print(f'{(num2words(loop_position, ordinal=1)).title()} loop: {x.join(each[Alpha::])} {x.join(each[cont:end2])}')
    loop_position += 1
    Alpha += 1
    end2 += 1
