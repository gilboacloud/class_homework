from tabnanny import check

words= []
key_sence =[]
while True :
    get = str(input('please enter a word :'))
    key_sence.append(get.lower())
    #print(key_sence)
    if words.count(get) or key_sence.count(get.lower()) < 3 :
        words.append(get)
        print(words.count(get))
    else:
        print(f'you entered {get} more then twice')
        break