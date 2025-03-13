name = input("Hey type your name: ")
print("Hello " + name + " Welcome to my game!")

Should_we_play = input("Do you want to play? ").lower()

if  Should_we_play == "yes" or Should_we_play == "y":
    print("We are gonna play!")
    weapon = input("Choice a weapon (sword/axe:) ").lower()
    direction = input(" Do you want to go left / right? ").lower()
    if direction == 'left':
        print("Okay you went left and fell of a cliff, game over!")
    elif direction =='right':
        choice = input("we went right, you see a bridge now you want to swim under it or cross it?")
        if choice =='swim'and weapon == 'axe':
            print("You got eaten by an alligator, you die, the end!", "No,i fought against the alligator" )
        else: 
            print("you found the gold and won!")
    else:
        print("Sorry not a valid reply, you die!")
else:
    print("we are not playing....!")

