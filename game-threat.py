print('Hi! My name is Chris.')
print()
print('You don\'t know me, but I\'ve been admiring you for a while now.')
print()
print('If you\'re not busy, maybe we can hang out sometime.')
print()
print('...and maybe we\'ll end up happily together haha.')
print()

run = True
while run == True:
    wannaTalk = input("Will you stay and talk to me?(yes/no): ").lower()
    if wannaTalk == 'yes':
        print()
        print('Thank God. I thought you were going to say no haha.')
        print('That could have ended really bad haha...at least for you.')
    
    elif wannaTalk == 'no':
        print()
        print('I don\'t like that answer. Sit down with me.')
        print()
        run = False
    else:
        print()
        print('Stop fucking playing with me right now.')
        print()
        run = False

    looks = input('You\'re so pretty. Do you think I\'m handsome?(yes/no): ').lower()
    if looks == 'yes':
        print()
        print('Good. That means we are a thing now.')
        print()
        run = False
    elif looks == 'no':
        print()
        print('With time you\'ll learn to love me.')
        print()
        run = False
    else:
        print()
        print('Haha you must think so. You\'re so nervous.')
        print()
        run = False

print('I can walk you home if you\'d like.')
print()
print('I wish you would stay at talk to me.')
print()
print('Stop taking steps further away from me')
print()
print('...')
print()
print('I\'ll see you later')
print()

print('YOU HAVE ARRIVED HOME "SAFELY".')
print()

print('YOU ARE GETTING READY FOR BED NOW.')
print()
print('AS YOU\'RE EYES ARE ABOUT TO SHUT, YOU RECIEVE A MESSAGE FROM AN UNKNOWN NUMBER.')
print()

print('Glad you made it home safe. I followed you home to make sure you were safe.')
print()
print('There could have been creeps out there.')
print()

creep = True
while creep == True:
    text = input('Hey maybe we can hang out again tomorrow?(yes/no): ').lower()
    if text == 'yes':
        print('I\'ll be waiting for you at the same spot.')
        print()
        creep = False
    elif text == 'no':
        print('Okay i\'ll come find you so we can hangout.')
        print()
        creep = False
    else:
        print('That\'s okay. See ya tomorrow.')
        print()
        creep = False

    
      



