import time
#This is a comment
def TheHiddenForest():
    print("")
    print("Its summer of 2018 and you're getting ready for a flight to your grandparents house in Alaska.")
    print("")
    time.sleep(3)
    print("You just entered the alaskan border and start to experience some turbulence.")
    print("")
    time.sleep(3)
    print("After a couple of minutes you see the oxygen mask start to fall from its compartment.")
    print("")
    time.sleep(3)
    choice=raw_input("Do you follow the saftey instructions or get up and try to find out whats happening? (Get up/Saftey first)")
    print("")
    while choice != 'Saftey first' and choice !='Get up':
        choice=raw_input('Invalid Answer. Try again(Get up/Saftey first)')
    if choice == 'Get up':
        print("")
        print('You start walking towards the cockpit and suddenly everthing goes black.')
        time.sleep(3)
        print("")
        print('You are dead.')
        return
    else:
        print('You take the mask and place it around your head when you look out the window and see the ground rapidly approaching.')
        print("")
        time.sleep(3)
        print('You have entered...')
        time.sleep(3)
        print(' _____ _            _   _ _     _     _             ______                  _   ')
        print('|_   _| |          | | | (_)   | |   | |            |  ___|                | |  ')
        print('  | | | |__   ___  | |_| |_  __| | __| | ___ _ __   | |_ ___  _ __ ___  ___| |_ ')
        print("  | | | '_ \ / _ \ |  _  | |/ _` |/ _` |/ _ \ '_ \  |  _/ _ \| '__/ _ \/ __| __|")
        print('  | | | | | |  __/ | | | | | (_| | (_| |  __/ | | | | || (_) | | |  __/\__ \ |_ ')
        print("  \_/ |_| |_|\___| \_| |_/_|\__,_|\__,_|\___|_| |_| \_| \___/|_|  \___||___/\__|")
        print("")
        time.sleep(3)
        print('You wake up with a headache and all you see is trees as far as the eye can see.')
        print("")
        time.sleep(3)
        choice=raw_input('Do you explore or do you search the plane? (Explore/Search)')
        while choice != 'Explore' and choice !='Search':
            choice=raw_input('Invalid Answer. Try again(Explore/Search)')
        if choice == 'Explore':
            print("")
            print('Thirty minutes into exploring you start to realize that you cant find your way back to the plane.')
            print("")
            time.sleep(3)
            print('You start to panic, and start shouting to try to find help.')
            print("")
            time.sleep(3)
            print('While shouting, a bear approaches, with the sound of his steps and roaring masked by your screaming.')
            print("")
            time.sleep(3)
            print('Two weeks later a body is found in a nearby lake, said to be mauled by a bear.')
            print("")
            time.sleep(3)
            print('The only way they were able to identify you is by the necklace your grandmother gave you as a charm to wish you a safe flight.')
            return
        else: #you chose Obi-Wan
            print("")
            print('You decide to search the plane for survivors.')
            time.sleep(3)
            choice=raw_input('While searching the plane you start to hear a buzz approaching.(Check/Ignore)')
            while choice != 'Check' and choice != 'Ignore':
                choice=raw_input('Invalid Answer.Try again. (Check/Ignore)')
            if choice == 'Check':
                print("")
                print('You check the buzz and see a helicopter flying towards you.')
                print("")
                time.sleep(3)
                print('He notices the crashed plane and finds you along with it.')
                print("")
                time.sleep(3)
                print("You've survived")
                return
            else:
                print("")
                print('You decide to ignore the buzz and are trapped in the hidden forest till death.')
                return