import time
import random


# Slow print function
def slow_print(text, base_delay=0.02):
    for char in text:
        print(char, end="", flush=True)
        if char in ".!?":
            time.sleep(base_delay * 8)  # longer pause for punctuation
        elif char in ",;":
            time.sleep(base_delay * 4)  # medium pause for commas
        else:
            time.sleep(base_delay + random.uniform(0, base_delay))  # slight randomness
    print()


# Choice validation
def get_choice():
    while True:
        choice = input("> ")
        if choice in ["1", "2", "3", "4"]:
            return choice
        else:
            slow_print("❌ Invalid choice. Please enter 1, 2, 3, or 4.")


# Ocean world
def ocean_world(user_name, hp, gold, friend_saved):
    slow_print(
        f"\n🌊 {user_name}, you dive into Ocean-World! The water sparkles and glistens like diamonds..."
    )
    time.sleep(1)

    # Round 1
    slow_print("Round 1: You see a sunken shipwreck. Do you...")
    slow_print("1) Explore the wreck 💎")
    slow_print("2) Fight a shark 🦈")
    slow_print("3) Befriend a mermaid 🧜‍♀️")
    slow_print("4) Rest on floating wood 🪵")
    choice = get_choice()
    if choice == "1":
        gold += 5
        slow_print(
            "You swim into the wreck carefully, brushing aside seaweed and shells..."
        )
        slow_print("Inside, you find shiny coins scattered across a chest! +5 gold ✨")
        slow_print(
            "The sound of bubbling water surrounds you as you gather the treasure."
        )
    elif choice == "2":
        hp -= 3
        gold += 3
        slow_print(
            "A massive shark appears! You fight fiercely and take some gold from its cave..."
        )
        slow_print("-3 HP, +3 gold")
        slow_print(
            "Your heart pounds as you surface, the water still rippling with danger."
        )
    elif choice == "3":
        friend_saved = True
        slow_print(
            "A mermaid approaches you with kindness, intrigued by your bravery..."
        )
        slow_print("She offers her friendship 💖 She may help you later.")
        slow_print("Her shimmering tail sways as she disappears into the blue abyss.")
    elif choice == "4":
        hp += 1
        slow_print(
            "You drift lazily on the floating wood, listening to the soothing waves..."
        )
        slow_print("+1 HP 🌸")
        slow_print("The sun warms your face and a gentle breeze lulls you into peace.")
    time.sleep(1)

    # Round 2
    slow_print("\nRound 2: You enter a coral cave. Inside...")
    slow_print("1) Search for pearls 🦪")
    slow_print("2) Fight a crab army 🦀")
    slow_print("3) Follow glowing fish 🐟")
    slow_print("4) Sleep in the cave 😴")
    choice = get_choice()
    if choice == "1":
        gold += 7
        slow_print(
            "You carefully search the cave, your hands brushing coral formations..."
        )
        slow_print("You find glimmering pearls hidden in the dark crevices! +7 gold")
        slow_print("Their luster reflects in your eyes as you pocket them.")
    elif choice == "2":
        hp -= 4
        gold += 4
        slow_print("A crab army appears, clicking their claws menacingly...")
        slow_print(
            "You fight bravely, enduring their attack to claim some treasure. -4 HP, +4 gold"
        )
        slow_print("Blood mingles with saltwater as you escape the cave.")
    elif choice == "3":
        hp += 2
        slow_print(
            "The glowing fish swim around you, guiding your way deeper into the cave..."
        )
        slow_print("You feel a warm healing sensation in your body. +2 HP")
        slow_print("Their glow fades as they vanish into the darkness.")
    elif choice == "4":
        hp -= 1
        slow_print("You rest in the cave, lulled by the sound of the sea...")
        slow_print("But a sea snake silently strikes. -1 HP")
        slow_print("You wake with a start, feeling the sting on your leg.")
    time.sleep(1)

    # Round 3
    slow_print("\nRound 3: You find an ancient temple...")
    slow_print("1) Solve puzzles 🧩")
    slow_print("2) Touch the magic orb 🔮")
    slow_print("3) Run away 🏃‍♂️")
    slow_print("4) Pray at the altar 🙏")
    choice = get_choice()
    if choice == "1":
        gold += 10
        slow_print(
            "You examine the puzzles carefully, tracing symbols etched into coral stone..."
        )
        slow_print("You solve them and uncover a hidden treasure! +10 gold")
        slow_print("The temple hums softly in approval.")
    elif choice == "2":
        hp -= 5
        slow_print("The orb pulses with light, drawing you closer...")
        slow_print("A sharp jolt strikes you, draining your strength. -5 HP")
        slow_print("But you feel knowledge blooming in your mind.")
    elif choice == "3":
        slow_print("Fear takes over. You sprint away from the temple.")
        slow_print("Your footsteps echo across the underwater ruins.")
    elif choice == "4":
        hp += 3
        slow_print("You kneel at the altar, whispering a prayer to the sea gods...")
        slow_print("+3 HP")
        slow_print("A warm wave of peace washes over you.")
    time.sleep(1)

    # Round 4
    slow_print("\nRound 4: A whirlpool appears!")
    slow_print("1) Swim against the current 🏊")
    slow_print("2) Let it pull you in 🌪️")
    slow_print("3) Call your mermaid friend 🧜‍♀️")
    slow_print("4) Hide behind rocks 🪨")
    choice = get_choice()
    if choice == "1":
        hp -= 3
        slow_print("You brace yourself and swim against the current...")
        slow_print("The water pushes hard. -3 HP")
        slow_print("Exhausted, you break free, gasping for breath.")
    elif choice == "2":
        gold += 5
        slow_print(
            "The whirlpool pulls you deep, revealing treasure glimmering below..."
        )
        slow_print("+5 gold")
        slow_print("You emerge clutching your prize.")
    elif choice == "3" and friend_saved:
        slow_print("Your mermaid friend appears instantly and guides you to safety 💖")
        slow_print("The whirlpool fades behind you.")
    elif choice == "3" and not friend_saved:
        hp -= 4
        slow_print("You call desperately for help... but no one comes.")
        slow_print("-4 HP")
        slow_print("The whirlpool spins you deeper into danger.")
    elif choice == "4":
        hp -= 2
        slow_print("You hide behind rocks, but the force scrapes you harshly.")
        slow_print("-2 HP")
    time.sleep(1)

    return hp, gold, friend_saved


# Desert world
def desert_world(user_name, hp, gold, friend_saved):
    slow_print(
        f"\n🏜️ {user_name}, you step into Desert-World. The sun scorches the golden sands..."
    )
    time.sleep(1)

    # Round 1
    slow_print("Round 1: You see a pyramid. Do you...")
    slow_print("1) Enter it 🏯")
    slow_print("2) Chase a golden scorpion 🦂")
    slow_print("3) Save a traveler 👤")
    slow_print("4) Rest under a palm tree 🌴")
    choice = get_choice()
    if choice == "1":
        gold += 8
        hp -= 2
        slow_print(
            "You enter the pyramid, stepping over shifting sands and ancient traps..."
        )
        slow_print("+8 gold, -2 HP")
        slow_print("Inside, the air is heavy with mystery.")
    elif choice == "2":
        gold += 3
        hp -= 3
        slow_print("The scorpion stings you as you chase it across the sand...")
        slow_print("+3 gold, -3 HP")
        slow_print("Its gold shell glints before vanishing.")
    elif choice == "3":
        friend_saved = True
        slow_print("You save a weary traveler from the scorching sands...")
        slow_print("They pledge loyalty to you 💖")
    elif choice == "4":
        hp += 2
        slow_print("You rest under the palm tree, listening to the wind...")
        slow_print("+2 HP")
        slow_print("The world feels still and safe.")
    time.sleep(1)

    # Round 2
    slow_print("\nRound 2: You stumble into a sandstorm...")
    slow_print("1) Push through 💪")
    slow_print("2) Hide in a cave 🏚️")
    slow_print("3) Follow a camel 🐪")
    slow_print("4) Do nothing 😶")
    choice = get_choice()
    if choice == "1":
        hp -= 4
        slow_print("The sand bites at your skin as you push forward...")
        slow_print("-4 HP")
        slow_print("But your determination fuels your steps.")
    elif choice == "2":
        hp += 1
        slow_print("The cave shelters you from the storm.")
        slow_print("+1 HP")
        slow_print("You listen to the wind howl outside.")
    elif choice == "3":
        gold += 5
        slow_print("The camel leads you to a hidden oasis filled with treasure...")
        slow_print("+5 gold")
    elif choice == "4":
        hp -= 1
        slow_print("You stand still as the storm buries you in sand...")
        slow_print("-1 HP")
    time.sleep(1)

    # Round 3
    slow_print("\nRound 3: You find an oasis.")
    slow_print("1) Drink water 💧")
    slow_print("2) Trade with nomads 🧿")
    slow_print("3) Swim in the pool 🏊")
    slow_print("4) Ignore and walk away 🚶")
    choice = get_choice()
    if choice == "1":
        hp += 4
        slow_print("The water is crystal clear, refreshing your body and soul.")
        slow_print("+4 HP")
    elif choice == "2":
        if gold >= 2:
            gold -= 2
            hp += 5
            slow_print("You trade gold for healing herbs.")
            slow_print("-2 gold, +5 HP")
        else:
            slow_print("You don’t have enough gold.")
    elif choice == "3":
        hp += 2
        slow_print("You swim, feeling weightless and renewed.")
        slow_print("+2 HP")
    elif choice == "4":
        slow_print("You ignore the oasis and keep walking.")
    time.sleep(1)

    # Round 4
    slow_print("\nRound 4: A sand dragon appears!")
    slow_print("1) Fight it ⚔️")
    slow_print("2) Run away 🏃")
    slow_print("3) Call your traveler friend 👤")
    slow_print("4) Hide underground 🕳️")
    choice = get_choice()
    if choice == "1":
        hp -= 5
        gold += 5
        slow_print("You strike at the dragon, taking wounds but claiming treasure.")
        slow_print("-5 HP, +5 gold")
    elif choice == "2":
        hp -= 2
        slow_print("You run with all your might, barely escaping.")
        slow_print("-2 HP")
    elif choice == "3" and friend_saved:
        slow_print("Your traveler friend appears, fighting beside you.")
        slow_print("The dragon retreats 💖")
    elif choice == "3" and not friend_saved:
        hp -= 4
        slow_print("You call for help, but no one answers...")
        slow_print("-4 HP")
    elif choice == "4":
        hp -= 3
        slow_print("The dragon scorches your hiding place.")
        slow_print("-3 HP")
    time.sleep(1)

    return hp, gold, friend_saved


# Boss fight
def boss_fight(user_name, hp, gold, friend_saved):
    slow_print("\n⚡ FINAL BOSS ⚡")
    slow_print("A giant monster blocks your path, roaring with fury!")
    time.sleep(1)

    if gold >= 15:
        slow_print("You buy a mighty weapon with your gold! ⚔️")
        slow_print("With great strength, you defeat the boss! 🎉")
        return True
    elif friend_saved:
        slow_print(
            "You don’t have enough gold... but your friend fights beside you! 🤝"
        )
        slow_print("Together, you win! 🎉")
        return True
    else:
        slow_print("You have no weapon and no ally... the boss crushes you 💀")
        return False


# Main game loop
while True:
    user_name = input("Please Enter your name: ")
    slow_print(
        f"\nHello {user_name}! 🌟 Welcome to the game: Choose Your Own Adventure 🎮\n"
    )

    hp = 10
    gold = 0
    friend_saved = False

    # Choose a world
    while True:
        adventure_setting = input(
            "Would you like to go into Ocean-World 🌊 or Desert-World 🏜️? \n" + "> "
        )
        if "ocean" in adventure_setting.lower():
            hp, gold, friend_saved = ocean_world(user_name, hp, gold, friend_saved)
            break
        elif "desert" in adventure_setting.lower():
            hp, gold, friend_saved = desert_world(user_name, hp, gold, friend_saved)
            break
        else:
            slow_print("That’s not a valid choice! Please enter again.")

    # Boss fight
    boss_fight(user_name, hp, gold, friend_saved)

    # Restart or exit
    while True:
        choice = input(
            "\nDo you want to continue playing (continue) or exit (exit)? "
        ).lower()
        if choice == "continue":
            slow_print("\nRestarting the adventure...\n")
            break
        elif choice == "exit":
            slow_print("Thanks for playing! Goodbye 👋")
            quit()
        else:
            slow_print(f"{choice} is not a valid choice.")
            time.sleep(1)
