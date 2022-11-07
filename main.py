''' This "Chatpup" was created as a demo for Meet My Chatboy Friend project for Girls Who Code E-School class. '''

def play_game(name):
    '''initiate 🎾Throw the Ball game loop '''
    #throw ball
    count = 0
    while True:
        choice = input("Bark! what would you like to do ? throw, fake throw, leave ")
        if choice.lower() == "throw":
            count += 1
            time.sleep(2)
            print("you threw it SO far! WOOOO!")
            print("*running, running, running, running, RUN!*")
            time.sleep(2)
            print("    __             ")
            print("      (___()'`;🎾  ")
            print("      /,    /`     ")
            print("      \\''--\\     ")
            time.sleep(2)

            if count == 3:
                nap_time()
                break
        #fake throw ball
        elif choice.lower() == "fake throw" or "fakethrow" or "fake":
            print("*flinches")
            time.sleep(2)
            print("*stares intensely*")
            time.sleep(2)
            print("Do you think this is a game, " + name + "?")
            time.sleep(2)
            print("whoops... haha yes, we are playing a game!")
        elif choice.lower() == "leave":
            print("Oh, okay... ")
            break
        else:
            print("not sure what you mean, but please play with me ):")
            break


def nap_time():
    '''Chatpup gets sleepy and takes a nap and exits the 🎾Throw the Ball game loop'''
    sleepy = "*\ty\ta\tw\tn\ts\t*"
    print(sleepy.expandtabs(5))
    time.sleep(2)
    print("*Russell is getting tired... takes a 💤nap*")

import time
#chatpup meets user
print("HI THERE!... oh, sorry... am I in your personal space? Tricky concept.. but I just LOVE meeting new people!")
time.sleep(2)
print("*tail wag*")
time.sleep(1)
print("Let's start over...")
time.sleep(2)
name = input("Hi, what's your name? ")

print("Bark! Let's see if I can spell that:")
time.sleep(1)
#code for spell name
for letter in name:
    print(letter)
    time.sleep(1)

print("Greetings and Barkutations " + name + "! This chatpup was made so you can learn more about Ms. Llaguno's dog... ME.")
time.sleep(4)
print("My dog tag says that I'm Russell. I'm a little shy, but Mom would think otherwise because I am always barking and have quite a lot to say!")
time.sleep(5)
print("Before I get distracted, can you tell me about yourself?")
time.sleep(3)

#getting to know the user
print("Where are you from?")
place = input("You are from... ")
print("Bark! " + place + " sounds just as cool as you. 💭Hmm... I have to remember if my pawrents took me to any dog parks near the area.")
time.sleep(4)

print("Ok, next one... cats or dogs?")
time.sleep(2)
print("haha! jk, no need to say it... I already know. ")
time.sleep(2)
print("*tail wagging intensifies*")
time.sleep(2)

print("What are you passionate about?")
passion = input("You are passionate about... ")
print("Bark! That's amazing! " + passion + " is so cool. ")
time.sleep(2)

print("Tell me more! What is your personal goal?")
goal = input("Your goal is to... ")
print("*complete silence*")
time.sleep(2)
print("BARK! I really admire your goal to " + goal + ". I know that you can do it, Bark, Bark! ")
time.sleep(4)

print("Wow, " + name + ". You are pretty pawsome. and...")
time.sleep(3)
print("*sniff, sniff*")
time.sleep(2)
print("*sniff, sniff*")
time.sleep(2)
print("I don't sense much stranger danger from you. Let's be pals furever!")
time.sleep(3)
print("Ok, my turn!")
time.sleep(2)

#getting to know chatpup
while True:
    topic = input("What would you like to know about me? - origin, looks, hobby, goal, or none? ")
    #code for origin
    if topic.lower() == "origin":
        print("My name is Russell... Russell Westbark named after 🏀Russell Westbrook. I'm known as the ⚡️Puppy Turbo at the dog park. Just like the og Brodie, I have the zoomies and while he's getting buckets, I'm getting the squeakers from my toys.")
        time.sleep(4)
    #code for hobby
    elif topic.lower() == "hobby":
        print("I enjoy early morning runs with my pawrents and being rewarded with a 🥇puppuccino.")
        time.sleep(3)
    #code for looks
    elif topic.lower() == "looks":
        print("Here, I drew a pic of myself... ")
        print("       ___      ")
        print("    (/(^•^)\)   ")
        print("      /   \/)   ")
        print("      nu-un/    ")
        time.sleep(2)
        print("I have fluffy white fur, black eyes that will stare into your soul, and apparently the cutest paws ever.")
        time.sleep(4)
    #code for goal
    elif topic.lower() == "goal":
        # code for goal
        print("My goal is to make my pawrents happy and shower them with lots of love and cuddles")
        time.sleep(3)
        print("because I'm a good boy")
        time.sleep(2)
        print(".... a very veeeeeeeeerry good boy")
        print("       -=====-     ")
        print("        .-`-.      ")
        print("       /|6 6|\     ")
        print("      {/(_o_)\}    ")
        print("       _/ ^ \_     ")
        print("      (/ /^\ \)-'  ")
        print("       ""' '""     ")
        time.sleep(3)
    #code for none
    elif topic.lower() == "none" or "no" or "nothing":
        print("Oh, okay!")
        break
    else:
        print("Sorry, I didn't catch that.")

#chatpup wants to play a game
print("My pawrents say I have major ✨puppy energy✨")
time.sleep(2)
game = input("My favorite thing ever is playtime.... wait, do you want to play 🎾Throw the Ball with me? - yes or no ")
if game == "yes":
    time.sleep(2)

    play_game(name)
else:
    print("Oh, okay... ")

print("Thanks for chatting with me, " + name + "! See you soon!")
