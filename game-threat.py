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



