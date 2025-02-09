# get words until a word is repeated

words= []

while True :
    get = str(input('please enter a word :'))
    if get not in words:
        words.append(get)

    else:
        print(f'you entered {get} more then once')
        break