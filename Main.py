print("Welcome to my first game!")

name = input("What is your name? ")
age = int(input("What is your age? "))
health = 10

if age >= 18:
    print("You are old enough to play!")

    wants_to_play = input("Do you want to play? ").lower()
    if wants_to_play == "yes":
        print("Let's play!")
        weapon = input("Pick a weapon. (Sword/Mace/Crossbow): ").lower()
        print("You are starting with", health, "health.")

        left_or_right = input("First choice... Left or Right? (Left/Right): ").lower()
        if left_or_right == "left":
            ans = input("Nice, you follow the path and reach a lake... Do you swim across or go around? (Across/Around): ").lower()

            if ans == "around":
                print("You went around and reached the other side of the lake.")
            elif ans == "across":
                print("You managed to get across, but were bit by an aligator and lost 5 health.")
                health -= 5

            ans = input("You notice a house and a river. Which do you go to? (River/House): ").lower()
            if ans == "house":
                print("You go to the house and run into a very poorly set trap, losing 5 health.")
                health -= 5

                if health <=0:
                    print("You now have 0 health and lost the game...")
                else:
                    print("You still managed to survive and find shelter...You win!")

            else:
                print("You fell in the river and lost...")

        else:
            print("You run into the devil Asmodeus and die in excruciating pain.")

    else:
        print("Shame...")        

else:
    print("You are not old enough to play...")
