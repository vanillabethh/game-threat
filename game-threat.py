print('Hi! My name is Chris.')
print()
print('You don\'t know me, but I\'ve been admiring you for a while now.')
print()
print('If you\'re not busy, maybe we can hang out sometime.')
print()

run = True
while run == True:
    wannaTalk = input("I know it\'s very sudden, but would you like to chat for a bit?(yes/no): ").lower()
    if wannaTalk == 'yes':
        print()
        print('Thank God. I thought you were going to say no haha.')
        print()
    
    elif wannaTalk == 'no':
        print()
        print('Maybe next time.')
        print()
        run = False
    else:
        print()
        print('...')
        print()
        
    looks = input('Sorry I just think you\'re so pretty.(umm/thanks): ').lower()
    if looks == 'umm':
        print()
        print('Sorry too soon.')
        print()
        run = False
    elif looks == 'thanks':
        print()
        print('Your hair must smell nice.')
        print()
        run = False
    else:
        print()
        print('...')
        print()
        

print('I can walk you home if you\'d like.')
print()
print('No?')
print()
print('...')
print()
print('See you soon.')
print()

print('YOU HAVE ARRIVED HOME "SAFELY".')
print()

print('YOU ARE NOW GETTING READY FOR BED.')
print()
print('AS YOU\'RE EYES ARE ABOUT TO SHUT, YOU RECIEVE A TEXT MESSAGE FROM AN UNKNOWN NUMBER.')
print()

print('Unknown: Glad you made it home safe.')
print()
print('YOU NEVER TOLD ANYONE YOU ARRIVED HOME.')
print()

creep = True
while creep == True:
    text = input('Unknown:Hey maybe we can hang out tomorrow?(umm/no): ').lower()
    if text == 'umm':
        print('I\'ll be waiting for you at the same spot.')
        print()
        creep = False
    elif text == 'no':
        print('Our paths will cross again.')
        print()
        creep = False
    else:
        print('That\'s okay. See ya tomorrow.')
        print()
        

print()
print('IT IS NOW 12:00 AM. YOU WAKE UP TO A LOUD ALERT FROM YOUR SECURITY CAMERAS.')
print()
print('ALERT')
print('THERE IS A TALL SHADOWY FIGURE ATTEMPTING TO ENTER THROUGH THE BACK DOOR.')
print()
print('5 MINUTES LATER.')
print()
print('ALERT')
print('THERE IS A TALL SHADOWY FIGURE ATTEMPTING TO ENTER THROUGH THE FRONT DOOR.')
print()

camera = True
while camera == True:
    choice = input('A:Call the police or B:Go check it out?(A/B)').upper()
    if choice == 'A':
        print('The phone lines have been disconnected. Hide.')
        print()
        camera = False
    elif choice == 'B':
        print('He knows you are awake now. Keep checking your cameras to stay vigilant.')
        print()
        camera = False
    else:
        print('Stalling won\'t help.')
        print()

print()
print('IT IS NOW 3:00 AM.')
print()
print('ALERT')
print('SOMEONE IS ATTEMPTING TO OPEN BEDROOM WINDOW.')
print()

window = True
while window == True:
    bedroomWindow = input('Lock bedroom window?(yes/no): ').lower()
    if bedroomWindow == 'yes':
        print('You have locked your bedroom window. He\'s mad now.')
        print()
        window = False
    elif bedroomWindow == 'no':
        print('He is now inside.')
        print() 
        window = False
    else:
        print('HURRY HE\'S ALMOST INSIDE!')
        print()

print()
print('RUN TO YOUR NEIGHBORS HOUSE TO SURVIVE THE NIGHT!')
print()

neighbor = True
while neighbor == True:
    print('Your neighbor Lisa answers the door.')
    print('Lisa looks behind you with fear and drags you inside while locking the door.')
    print('Lisa: There was a hooded figure running after you.')
    print()
    callOne = input('Lisa: Dial 911 NOW!(911): ')
    if callOne == '911':
        print('Police: We will be there shortly.')
        print()
        neighbor = False
    else:
        print('Lisa: HURRY!')
        print()

print('THE TALL FIGURE LEAVES AS POLICE SIRENS WERE HEARD IN THE DISTANCE.')
print()

print('A DETECTIVE TAKE YOURS AND LISA\'S STATEMENTS BEFORE THEY START THEIR INVESTIGATION.')
# TODO your hairbrush is missing 

              
  
 

        
    
      



