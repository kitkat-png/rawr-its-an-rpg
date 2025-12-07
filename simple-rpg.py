import random
import social
import sys

# 4 interactions = a full day
interactions = 0
days = 0

# gardening info
plants = 5
plants_status = "dry"
plants_harvestable = False

# fishing info
fish_in_river = True

# home info
wall_color = "white"
floor = "light wood"
poster_amount = 0
potted_plant_amount = 0

inventory = {"Fruit": 0, "Fish": 0, "Wood": 0}


def update():
    """Updates stuff like the garden, used when another day passes"""

    # inserts global variables so we can use them
    global plants_status
    global plants_harvestable
    global fish_in_river

    if plants_status == "wet":
        plants_harvestable = True

    plants_status = "dry"

    fish_in_river = True


def animal_interaction():
    """Makes it so that there's a 1 in 5 chance every time you pick an interaction of you meeting an animal"""

    chances_of_interaction = random.randint(1, 5)
    which_animal = random.randint(1, 3)

    if which_animal == 1:
        which_animal = "cat"
    elif which_animal == 2:
        which_animal = "squirrel"
    elif which_animal == 3:
        which_animal = "pigeon"

    if chances_of_interaction == 5:
        print("You encounter a " + which_animal + " on your way to your destination.")
        print("What do you do?")
        print("A. pet")
        print("B. feed")
        print("C. ignore")

        interact_with_animal = input("> ")
        interact_with_animal = interact_with_animal.strip()
        interact_with_animal = interact_with_animal.lower()

        global interactions

        if interact_with_animal == "a":
            print("You pet the " + which_animal + " and you're both happy.")
            interactions += 1
        elif interact_with_animal == "b":
            if which_animal == "cat":
                # if you have fish you give it to the cat
                if inventory["Fish"] > 0:
                    print("You give some fish to the cat.")
                    print("It brings you both happiness")
                    inventory["Fish"] -= 1
                else:
                    print("You don't have any fish to give the cat.")
            else:
                # if you have fruit, you give it to the animal
                if inventory["Fruit"] > 0:
                    print("You give some fruit to the " + which_animal + ".")
                    print("It brings you both happiness.")
                    inventory["Fruit"] -= 1
                    interactions += 1
                else:
                    print("You don't have any fruit to give the " + which_animal + ".")
        elif interact_with_animal == "c":
            print("You ignore the " + which_animal + " and move on.")


def tablet():
    """Has interactions for playing on your tablet (aka minigames)"""

    print("You get your tablet out of your bag.")
    print("There are three games to choose from.")
    print("A. guess the number")
    print("B. personality quiz")
    print("Which one do you wanna play?")

    chosen_game = input("> ")
    chosen_game = chosen_game.strip()
    chosen_game = chosen_game.lower()

    if chosen_game == "a":
        random_number = random.randint(1, 100)
        print("A random number between 1 and 100 has been chosen.")

        def input_the_number():
            guessed_number = int(input("> "))

            if guessed_number > random_number:
                print("Wrong number. Too high.")
                input_the_number()
            elif guessed_number < random_number:
                print("Wrong number. Too low.")
                input_the_number()
            else:
                print("You successfully guessed the number!")

        input_the_number()
    elif chosen_game == "b":
        print("Welcome to the personality quiz.")
        print("Here we will be seeing if you're a glorpus or a gooboo.")

        def quiz():
            """A function for the quiz in case the person wants to do it again and again"""

            # the glorpus is gentle and kind and loving
            glorpus_points = 0
            # the gooboo cares a lot about appearances and being seen as good
            gooboo_points = 0

            # in case you can't tell, this quiz is one big jab towards the gender binary

            print("Which of these is your favorite place to sleep?")
            print("A. at a friend's house")
            print("B. in my own bed")
            print("C. when I'm dead")
            print("D. on the floor of the cafeteria")

            answer1 = input("> ")
            answer1 = answer1.strip()
            answer1 = answer1.lower()

            if answer1 == "a":
                glorpus_points += 1
            elif answer1 == "b":
                gooboo_points += 1
            elif answer1 == "c":
                gooboo_points += 1
            elif answer1 == "d":
                glorpus_points += 1

            print("Where do you want to go to brunch?")
            print("A. wherever my friends wanna go")
            print("B. nowhere")
            print("C. the cemetery")
            print("D. somewhere with pancakes")

            answer2 = input("> ")
            answer2 = answer2.strip()
            answer2 = answer2.lower()

            if answer2 == "a":
                gooboo_points += 1
            elif answer2 == "b":
                glorpus_points += 1
            elif answer2 == "c":
                glorpus_points += 1
            elif answer2 == "d":
                gooboo_points += 1

            print("Which of these is most likely?")
            print("A. the existence of a god or gods")
            print("B. magic existing")
            print("C. the world blowing up in three days")
            print("D. me getting a good job")

            answer3 = input("> ")
            answer3 = answer3.strip()
            answer3 = answer3.lower()

            if answer3 == "a":
                gooboo_points += 1
            elif answer3 == "b":
                glorpus_points += 1
            elif answer3 == "c":
                glorpus_points += 1
            elif answer3 == "d":
                gooboo_points += 1

            print("Pick a taste")
            print("A. sweet")
            print("B. sour")
            print("C. spicy")
            print("D. tangy")

            answer4 = input("> ")
            answer4 = answer4.strip()
            answer4 = answer4.lower()

            if answer4 == "a":
                gooboo_points += 1
            elif answer4 == "b":
                glorpus_points += 1
            elif answer4 == "c":
                gooboo_points += 1
            elif answer4 == "d":
                glorpus_points += 1

            print("Glorpus points: " + str(glorpus_points))
            print("Gooboo points: " + str(gooboo_points))

            if glorpus_points > gooboo_points:
                print("You are a glorpus!")
                print("This means you are gentle, kind, and authentic.")
            elif glorpus_points < gooboo_points:
                print("You are a glooboo!")
                print(
                    "This means you care a lot about being seen as a good and acceptable person."
                )
            elif glorpus_points == gooboo_points:
                print("You got a tie!")

            print("Do you wanna do the quiz again? y/n")

            do_quiz_again = input("> ")
            do_quiz_again = do_quiz_again.strip()
            do_quiz_again = do_quiz_again.lower()

            if do_quiz_again == "y":
                quiz()

        quiz()


def wood_chopping():
    """Has interactions for chopping wood"""

    print("You go to the forest to get some wood.")
    print("How many trees will you chop down? (choose 1-4)")
    trees_chopped = input("> ")
    trees_chopped = trees_chopped.strip()
    trees_chopped = int(trees_chopped)

    while trees_chopped > 4 or trees_chopped < 0:
        print("Choose a valid 1-4 number.")
        trees_chopped = input("> ")
        trees_chopped = trees_chopped.strip()
        trees_chopped = int(trees_chopped)

    wood_gotten = trees_chopped * random.randint(4, 6)
    inventory["Wood"] += wood_gotten

    print("You got " + str(wood_gotten) + " logs of wood.")
    print("You also make sure to replant at least most of the trees.")


def fishing():
    """Has interactions for going fishing"""

    print("You go to the river to fish.")

    global fish_in_river

    if fish_in_river:
        fish_amount = random.randint(1, 5)
        print("You catch " + str(fish_amount) + " fish.")
        inventory["Fish"] += fish_amount
        fish_in_river = False
    else:
        print("There aren't any fish in the river.")


def garden():
    """Has interactions for going to the garden"""

    print("You go to your garden.")
    print("The air feels nice and fresh.")

    print("Do you:")
    print("A. water your plants if they're dry")
    print("B. harvest any plants that are ready")
    print("C. plant more plants")

    garden_action = input("> ")
    garden_action = garden_action.strip()
    garden_action.lower()

    global plants
    global plants_status
    global plants_harvestable

    if garden_action == "a":
        # if the plants are dry we water them
        if plants_status == "dry":
            print("You water your dry plants")
            plants_status = "wet"
        else:
            print("Your plants have already been watered today.")
    elif garden_action == "b":
        # if the plants can be harvested we harvest them
        if not plants_harvestable:
            print("None of your plants can be harvested right now.")
        else:
            print("You harvest your plants.")
            print("You get " + str(plants) + " fruits.")

            inventory["Fruit"] += 1
    elif garden_action == "c":
        # we plant as many new plants as you want
        print("How many more plants do you want to plant?")
        how_many_plants = input("> ")
        print("You plant " + how_many_plants + " new plants.")
        plants += int(how_many_plants)


def home_decor():
    """Has interactions for going home and checking out your decor"""

    print("You go home and take a look at how you've got things set up.")

    global wall_color
    global floor
    global poster_amount
    global potted_plant_amount

    print("The wall color is " + wall_color + ".")
    print("The floor is made up of " + floor + ".")
    print("There are " + str(poster_amount) + " posters on the walls.")
    print("There are " + str(potted_plant_amount) + " potted plants.")

    print("Is there anything you'd like to change?")
    print("A. the walls")
    print("B. the floor")
    print("C. amount of posters")
    print("D. amount of potted plants")

    change = input("> ")
    change = change.strip()
    change = change.lower()

    if change == "a":
        print("What color do you want to make the walls?")
        wall_color = input("> ")
    elif change == "b":
        print("What material do you want the floor to be?")
        floor = input("> ")
    elif change == "c":
        print("How many posters do you want up?")
        poster_amount = int(input("> "))
    elif change == "d":
        print("How many potted plants do you want?")
        potted_plant_amount = int(input("> "))

    print("Would you like to change anything else?")
    print("y/n")
    keep_changing = input("> ")
    keep_changing = keep_changing.strip()
    keep_changing = keep_changing.lower()

    if keep_changing == "y":
        home_decor()


def check_inventory():
    """Displays inventory information"""

    print("Fruits: " + str(inventory["Fruit"]))
    print("Fish: " + str(inventory["Fish"]))
    print("Wood: " + str(inventory["Wood"]))

    main_actions()


def main_actions():
    print("What would you like to do? ")
    print("A. go to garden")
    print("B. go fishing")
    print("C. check inventory")
    print("D. go to home")
    print("E. play on tablet")
    print("F. chop wood")
    print("G. go socialize")
    print("H. quit game")

    what_to_do = input("> ")
    what_to_do = what_to_do.strip()
    what_to_do = what_to_do.lower()

    global interactions

    if what_to_do == "a":
        animal_interaction()
        garden()
        interactions += 1
        check_if_full_day()
    elif what_to_do == "b":
        animal_interaction()
        fishing()
        interactions += 1
        check_if_full_day()
    elif what_to_do == "c":
        # checking inventory doesn't count as an interaction
        check_inventory()
    elif what_to_do == "d":
        animal_interaction()
        home_decor()
        interactions += 1
        check_if_full_day()
    elif what_to_do == "e":
        tablet()
        interactions += 1
        check_if_full_day()
    elif what_to_do == "f":
        animal_interaction()
        wood_chopping()
        interactions += 1
        check_if_full_day()
    elif what_to_do == "g":
        animal_interaction()
        social.socialize()
        interactions += 1
        check_if_full_day()
    elif what_to_do == "h":
        print("Interactions today: " + str(interactions))
        print("Full days played: " + str(days))
        sys.exit()


def check_if_full_day():
    global interactions
    global days
    if interactions >= 4:
        print("It's time for you to rest.")
        print("You go home and rest so you are ready for the next day.")
        interactions = 0
        days += 1
        update()
        main_actions()
    else:
        main_actions()


main_actions()
