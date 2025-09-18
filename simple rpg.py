import random 
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

inventory = {
    "Fruit": 0,
    "Fish": 0,
}

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
        if plants_harvestable == False:
            print("None of your plants can be harvested right now.")
        else:
            print("You harvest your plants.")
            print("You get " + plants + " fruits.")

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

def main_actions():
    print("What would you like to do? ")
    print("A. go to garden")
    print("B. go fishing")
    print("C. check inventory")
    print("D. go to home")
    print("E. quit game")

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