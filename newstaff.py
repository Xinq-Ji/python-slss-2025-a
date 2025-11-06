# Versoin1
# Show all the choices
# Ask the user for their choice
# data to find the most popolar
# bubble tea place aorund us


# Version1


def vote_listed_choices():
    print("Vote for your favourite form the list")
    print("Give the letter of your choose")

    CHOICES = ["Blenz", "Bubble Queen", "Sun Tea", "Heytea", "Coco", "Fresh T"]

    for choice in CHOICES:
        print(choice)


def main():
    vote_listed_choices()


if __name__ == "__main__":
    main()
