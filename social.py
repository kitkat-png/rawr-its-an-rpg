
friendship_levels = {
        "anna": 0,
        "bethany": 0,
        "dave": 0
}

def anna():
    """Socializing with Anna"""

    print("You go to Anna's cottage further out in the forest.")
    print("You knock on her door and she greets you with a smile.")
    print("She lets you inside and you both sit on her comfy pink floral sofa.")
    print("What will you do?")
    print("A. send positive vibes")
    print("B. send neutral vibes")
    print("C. send negative vibes")
    print("D. send very negative vibes")

    anna_vibes = input("> ")
    anna_vibes = anna_vibes.strip()
    anna_vibes = anna_vibes.lower()
    
    if anna_vibes == "a":
        print("You send positive vibes.")
        print("Anna is very happy.")
        friendship_levels["anna"] += 2
    elif anna_vibes == "b":
        print("You send neutral vibes.")
        print("Anna is happy to be around you.")
        friendship_levels["anna"] += 1
    elif anna_vibes == "c":
        print("You send negative vibes.")
        print("Anna is sad.")
        friendship_levels["anna"] -= 1
    elif anna_vibes == "d":
        print("You send very negative vibes.")
        print("Anna is very sad.")
        friendship_levels["anna"] -= 2

def bethany():
    """Socializing with Bethany"""

    print("You go to Bethany's small house on the far edge of town.")
    print("You knock on the door and she greets you with a tired smile.")
    print("Her house is decorated with lots of colorful art on the walls.")
    print("You both sit down on the sofa.")
    print("What will you do?")
    print("A. send positive vibes")
    print("B. send neutral vibes")
    print("C. send negative vibes")
    print("D. send very negative vibes")

    bethany_vibes = input("> ")
    bethany_vibes = bethany_vibes.strip()
    bethany_vibes = bethany_vibes.lower() 

    if bethany_vibes == "a":
        print("You send positive vibes.")
        print("Bethany is excited and happy.")
        friendship_levels["bethany"] += 2
    elif bethany_vibes == "b":
        print("You send neutral vibes.")
        print("Bethany is happy to spend time with you.")
        friendship_levels["bethany"] += 1
    elif bethany_vibes == "c":
        print("You send negative vibes.")
        print("Bethany is frustrated with you.")
        friendship_levels["bethany"] -= 1
    elif bethany_vibes == "d":
        print("You send very negative vibes.")
        print("Bethany is angry with you.")
        friendship_levels["bethany"] -= 2

def dave():
    """Socialize with Dave"""

    print("You go to Dave's apartment in the city.")
    print("You knock on his door and he answers with a warm smile.")
    print("You both sit on his couch and look at the array of paper cranes on his coffee table.")
    print("What will you do?")
    print("A. send positive vibes")
    print("B. send neutral vibes")
    print("C. send negative vibes")
    print("D. send very negative vibes")

    dave_vibes = input("> ")
    dave_vibes = dave_vibes.strip()
    dave_vibes = dave_vibes.lower()

    if dave_vibes == "a":
        print("You send positive vibes.")
        print("Dave is delighted.")
        friendship_levels["dave"] += 2
    elif dave_vibes == "b":
        print("You send neutral vibes.")
        print("Dave is cool with that.")
        friendship_levels["dave"] += 1
    elif dave_vibes == "c":
        print("You send negative vibes.")
        print("Dave is displeased.")
        friendship_levels["dave"] -= 1
    elif dave_vibes == "d":
        print("You send very negative vibes.")
        print("Dave is sad.")
        friendship_levels["dave"] -= 2

def socialize():
    """The main social interactions in the game start here"""

    print("You have decided to socialize!")
    print("Which friend do you wanna yap with?")
    print("A. Anna")
    print("B. Bethany")
    print("C. Dave")

    socialize_who = input("> ")
    socialize_who = socialize_who.strip()
    socialize_who = socialize_who.lower()

    if socialize_who == "a":
        anna()
    elif socialize_who == "b":
        bethany()
    elif socialize_who == "c":
        dave()

    print("Current friendship levels with each character:")
    print("Anna: " + str(friendship_levels["anna"]))
    print("Bethany: " + str(friendship_levels["bethany"]))
    print("Dave: " + str(friendship_levels["dave"]))
