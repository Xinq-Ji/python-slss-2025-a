import time

print("Welcome, player.")
time.sleep(1.5)
print("Your adventure will start in:")
time.sleep(0.7)
print("3")
time.sleep(1)
print("2")
time.sleep(1)
print("1")
time.sleep(1)
print("It is 3 am.")
time.sleep(1)
print("You lay awake in bed, unable to sleep.")
time.sleep(1.5)
print("Your stomach is growling, and you feel an intense wave of hunger.")
time.sleep(2)
print("You toss and turn, until finally, you decide that you have had enough.")
time.sleep(2.2)
print(
    "You're going to make a trip to the fridge downstairs, NOW, or else you're going to end up tired AND hungry in the morning."
)
time.sleep(3)
print("You shove your blanket to the side and reach your foot down.")
time.sleep(2)

while True:
    foot = input("Do you reach left or right with your foot? (left/right)")
    if foot == "left":
        break
    elif foot == "right":
        break
    else:
        print("Invalid input, please try again.")

if foot == "left":
    print("You reach left with your foot.")
    time.sleep(1.5)
    print("You successfully find your slippers and put them on.")
    time.sleep(2)
    print("You walk out of your room and down the stairs.")
    time.sleep(1.5)
    print("As you walk down the hallway and into the kitchen, you hear a faint sound.")
    time.sleep(2.5)
    print(
        "It's similar to that of a branch snapping off a tree, but seemingly coming from the kitchen."
    )
    time.sleep(2.7)
    print("You might've just imagined it, you tell yourself.")
    time.sleep(1.5)
    print("You walk into the kitchen and reach for the lightswitch.")
    time.sleep(2)

    while True:
        on = input("Do you turn on the light? (yes/no)")
        if on == "yes":
            break
        elif on == "no":
            break
        else:
            print("Invalid input, please try again.")

    if on == "yes":
        print("You turn on the light.")
        time.sleep(1.3)
        print("You are blinded immediately, but only momentarily.")
        time.sleep(2)
        print(
            "After you recover your vision, you realize that two cockroaches are skittering towards you at lightning speed."
        )
        time.sleep(3)
        print(
            "You think to yourself that maybe today is not the day to go to the fridge."
        )
        time.sleep(2.5)
        print("You start sprinting down the hallway and up the stairs.")
        time.sleep(2)
        print(
            "You dash under your blankets and wonder, where did those two disgusting pests even come from?"
        )
        time.sleep(2.7)
        print(
            "Did they only appear in your house in the middle of the night, when everyone was asleep?"
        )
        time.sleep(2.7)
        print("You hope that no cockroach is able to get upstairs and into your bed.")
        time.sleep(2)
        print(
            "You eventually drift off to sleep, dreaming about two cockroaches chasing you as you sprint around your house."
        )

    else:
        print("You think to yourself, nah, let's save some electricity.")
        print(
            "You hold out your hands in front of you to make sure you don't bump into anything."
        )
        time.sleep(2.5)
        print(
            "You're pretty confident you won't though, after all, you know your house pretty well."
        )
        time.sleep(2.5)
        print(
            "As you slowly make your way towards the fridge, you feel something brush against the side of your foot."
        )
        time.sleep(3)
        print("You don't think much of it and dismiss it as the wind.")
        time.sleep(2)
        print(
            "You open the fridge and take out the slice of cake that you were saving for breakfast."
        )
        time.sleep(2.5)
        print(
            "You close the fridge and happily munch on your cake in complete darkness."
        )
        time.sleep(2)
        print(
            "You wonder what you're gonna eat for breakfast now that you're eating the cake right now."
        )
        time.sleep(2.5)
        print("You toss the last two bites worth of cake back in the fridge.")
        time.sleep(2)
        print("You decide that your full enough after eating majority of the slice.")
        time.sleep(2)
        print("You walk back down the hallway towards the stairs and up to your room.")
        time.sleep(2)
        print(
            "You tuck yourself into bed and quickly fall asleep after not feeling hungry any longer."
        )
        time.sleep(2.5)
        print("Your night is filled with sweet dreams of stuffing your face with cake.")


else:
    print("You reach right with your foot.")
    time.sleep(1.5)
    print("You swing your foot around, trying to find where your sippers are.")
    time.sleep(2)
    print("Suddenly, you feel a hand grab your foot.")
    time.sleep(1.5)
    print("You freeze in fear, before quickly yanking your foot back.")
    time.sleep(2)
    print("You cover yourself with your blanket.")
    time.sleep(1.5)
    print("You are no longer hungry, just scared, VERY scared.")
    time.sleep(1.7)
    print("You tell yourself that you are never getting up at 3 am again.")
    time.sleep(2)
    print(
        "You spend the rest of the night shivering in fear before falling into an uneasy sleep."
    )
