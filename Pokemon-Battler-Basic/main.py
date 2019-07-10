import random

myHP = 0
enemyHP = 0

def attackPokemon(name, myMoves, wildPokemon, enemyMoves):
    '''Handles the Pokemon fighting.  Returns false when one of the pokemon has
    been defeated.'''
    global myHP, enemyHP
    
    # get move from player.
    myMove = ""
    while myMove not in myMoves:
        print("Possible moves:", myMoves)
        response = input("Enter a move: ")
        if myMove not in myMoves:
            myMove = response
        else:
            print("Invalid input.", myMoves)
    
    # get enemy move
    enemyMove = random.choice(enemyMoves)
    
    # player and computer pokemon attack each other
    speed = random.random()
    if speed > 0.5:
        print("{} moves quickly to attack first.".format(name))
        damage = random.randint(10, 45)
        enemyHP -= damage
        print("Your {} attack does {} damage.".format(myMove, damage))
        if enemyHP > 0:
            damage = random.randint(10, 45)
            myHP -= damage
            print("The wild {} retaliates with a {} attack.  It does {} damage.".format(wildPokemon, enemyMove, damage))

    else:
        print("The wild {} moves quickly to attack first.".format(wildPokemon))
        damage = random.randint(10, 45)
        myHP -= damage
        print("Its {} attack does {} damage.".format(enemyMove, damage))
        if myHP > 0:
            damage = random.randint(10, 45)
            enemyHP -= damage
            print("{} retaliates with a {} attack.  It does {} damage.".format(name, myMove, damage))
    
    if myHP <= 0:
        print("Your Pokemon has been defeated.")
        return False
    elif enemyHP <= 0:
        print("The Wild Pokemon has been defeated.")
        return False
        
    print("{} has {} HP left".format(name, myHP))
    print("Wild {} has {} HP left \n".format(wildPokemon, enemyHP))
    return True


def main():
    '''Runs the main game loop.'''
    global myHP, enemyHP
    play = True
    while play:
        pokemon = ["Bulbasaur", "Charmander", "Squirtle"]

        # Get computer's pokemon.
        wildPokemon = random.choice(pokemon)
        print("A wild {} has appeared.".format(wildPokemon))
        if wildPokemon == "Bulbasaur":
            enemyMoves = ["Tackle", "Vine Whip"]
            enemyHP = random.randint(105, 152)
        elif wildPokemon == "Charmander":
            enemyMoves = ["Scratch", "Ember"]
            enemyHP = random.randint(99, 146)
        else:
            enemyMoves = ["Tackle", "Water Gun"]
            enemyHP = random.randint(104, 151)
        
        # Get player's pokemon.
        myPokemon = ""
        while myPokemon not in pokemon:
            response = input("Choose Pokemon. [Bulbasaur/Charmander/Squirtle]: ").lower()
            if response == "bulbasaur":
                myPokemon = pokemon[0]
                myMoves = ["Tackle", "Vine Whip"]
                myHP = random.randint(105, 152)
            elif response == "charmander":
                myPokemon = pokemon[1]
                myMoves = ["Scratch", "Ember"]
                myHP = random.randint(99, 146)
            elif response == "squirtle":
                myPokemon = pokemon[2]
                myMoves = ["Tackle", "Water Gun"]
                myHP = random.randint(104, 151)
            else:
                print("Invalid input.")
        name = input("Enter your Pokemon's name:  ")

        fight = True
        while fight:
            fight = attackPokemon(name, myMoves, wildPokemon, enemyMoves)
        
        prompt = True
        while prompt:
            response = input("Play again? [y/n]")
            if response == "y":
                prompt = False
            elif response == "n":
                play = False
                prompt = False
            else:
                print("Invalid input.")

if __name__ == "__main__":
    main()