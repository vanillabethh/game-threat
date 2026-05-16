print('Hello! I hope you are having a good day so I can ruin it.')
print('Prepare yourself mentally.')
print('We are going to play a game.')
print('...and you won\'t like it')
print()

run = True
while run == True:
    wannaPlay = input("Will you play with me?(yes/no): ").lower()
    if wannaPlay == 'yes':
        print('That\'s great! You didn\'t have a choice anyways.')
    elif wannaPlay == 'no':
        print('Haha let\'s get started!')
    else:
        print('Don\'t play me right now just say yes or no.')
