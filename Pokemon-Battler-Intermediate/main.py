import random

playerHP = 0
enemyHP = 0

def attack(player, playerMoves, enemy, enemyMoves):
    '''Handles the characters fighting.  Returns false when one of the 
    characters has been defeated'''
    global playerHP, enemyHP
    
    # get move from player.
    defense = ["shield", "dodge"]
    playerMove = ""
    playerDefense = ""
    while playerMove not in playerMoves:
        print("Possible moves:", sorted(playerMoves.keys()))
        playerMove = input("Enter a move: ")
        if playerMove not in playerMoves:
            print("Invalid input.", sorted(playerMoves.keys()))
    playerDamage = random.randint(playerMoves[playerMove][0], playerMoves[playerMove][1])
    while playerDefense not in defense:
        print("Possible defense:", defense)
        playerDefense = input("Enter a defense: ")
        if playerDefense not in defense:
            print("Invalid input.", defense)
            
    # get enemy move
    enemyMove = random.choice(list(enemyMoves.keys()))
    enemyDamage = random.randint(enemyMoves[enemyMove][0], enemyMoves[enemyMove][1])
    enemyDefense = random.choice(defense)
    
    # Player and computer attack each other
    playerSpeed = 10 / playerDamage
    playerDodge = random.random()
    playerShield = random.randint(0, 50)
    enemySpeed = 10 / enemyDamage
    enemyDodge = random.random()
    enemyShield = random.randint(0, 50)
    print(playerDamage, playerSpeed, playerDodge, playerShield)
    print(enemyDamage, enemySpeed, enemyDodge, enemyShield)
    if playerSpeed > enemySpeed:
        print("You attack quickly with {}.".format(playerMove))
        if enemyDefense == "dodge":
            if enemyDodge > playerSpeed:
                print("{} dodges you attack.".format(enemy))
            else:
                print("{} tries to dodge but your spell hits anyways.".format(enemy))
                enemyHP -= playerDamage
                print("Your {} attack does {} damage.".format(playerMove, playerDamage))
        else:
            if enemyShield > playerDamage:
                print("{} reacts quickly with a protego to deflect your attack.".format(enemy))
            else:
                print("You spell breaks through {}'s shield.".format(enemy))
                enemyHP -= playerDamage
                print("Your {} attack does {} damage.".format(playerMove, playerDamage))
        if enemyHP > 0:
            print("{} retaliates with {}.".format(enemy, enemyMove))
            if playerDefense == "dodge":
                if playerDodge > enemySpeed:
                    print("You quickly dodge the attack.")
                else:
                    print("You try to dodge but the {} hits you anyways".format(enemyMove))
                    playerHP -= enemyDamage
                    print("{}'s spell does {} damage.".format(enemy, enemyDamage))
            else:
                if playerShield > enemyDamage:
                    print("You quickly cast protego to shield from the attack.")
                else:
                    print("The {} breaks through your week shield.".format(enemyMove))
                    playerHP -= enemyDamage
                    print("{}'s spell does {} damage.".format(enemy, enemyDamage))
    
    else:
        print("{} moves quickly and attacks with {}.".format(enemy, enemyMove))
        if playerDefense == "dodge":
            if playerDodge > enemySpeed:
                print("You quickly dodge the attack.")
            else:
                print("You try to dodge but the {} hits you anyways".format(enemyMove))
                playerHP -= enemyDamage
                print("{}'s spell does {} damage.".format(enemy, enemyDamage))
        else:
            if playerShield > enemyDamage:
                print("You quickly cast protego to shield from the attack.")
            else:
                print("The {} breaks through your week shield.".format(enemyMove))
                playerHP -= enemyDamage
                print("{}'s spell does {} damage.".format(enemy, enemyDamage))
        if playerHP > 0:
            print("You cast {} to retaliate.".format(playerMove))
            if enemyDefense == "dodge":
                if enemyDodge > playerSpeed:
                    print("{} dodges you attack.".format(enemy))
                else:
                    print("{} tries to dodge but your spell hits anyways.".format(enemy))
                    enemyHP -= playerDamage
                    print("Your {} attack does {} damage.".format(playerMove, playerDamage))
            else:
                if enemyShield > playerDamage:
                    print("{} reacts quickly with a protego to deflect your attack.".format(enemy))
                else:
                    print("You spell breaks through {}'s shield.".format(enemy))
                    enemyHP -= playerDamage
                    print("Your {} attack does {} damage.".format(playerMove, playerDamage))
        
    # Check if the fight is over
    if playerHP <= 0:
        print("You have been defeated.")
        return False
    elif enemyHP <= 0:
        print("{} has been defeated.".format(enemy))
        return False
    
    print("You have {} HP left.".format(playerHP))
    print("{} has {} HP left.".format(enemy, enemyHP))
    return True
    
    
def main():
    '''Runs the main game loop'''
    global playerHP, enemyHP
    
    order = ["Harry Potter", "Hermione Granger", "Ron Weasley", 
            "Neville Longbottom", "Fred Weasley", "George Weasley",
            "Alastor Moody", "Nymphadora Tonks", "Remus Lupin", 
            "Kingsley Shacklebolt", "Sirius Black", "Molly Weasley"]
    
    deathEaters = ["Voldemort", "Bellatrix Lestrange", "Lucius Malfoy", 
            "Draco Malfoy", "Alecto Carrow", "Amycus Carrow", "Fenrir Grayback",
            "Vincent Crabbe", "Gregory Goyle", "Antonin Dolohov"]
    
    lightMoves = {"Avis Oppugno": (20, 30), "Bat-Bogey": (0,10), 
            "Confringo":(40, 50), "Confundo":(10, 20), "Deprimo": (40, 50), 
            "Diffindo": (20, 30), "Expelliarmus": (40, 50), "Expulso": (40, 50), 
            "Furnuculus": (0, 10), "Glisseo": (10, 20), "Impedimenta": (20, 30), 
            "Incarcerous": (30, 40), "Jelly-Legs": (5, 15), 
            "Petrificus Totalus": (40, 50), "Rictusempra": (0, 10), 
            "Stupefy":(40, 60), "Tarantallegra": (10, 20)}

    darkMoves = {"Avada Kedavra": (100, 101), "Crucio": (50, 60),  
            "Expulso": (20, 30), "Fiendfyre":(40, 50), "Flagrate": (10, 20), 
            "Impedimenta": (10, 20), "Imperio": (50, 60), "Incendio":(20, 30), 
            "Reducto": (20, 30), "Sectumsempra": (20, 30), "Stupefy": (40, 50)}
            
    # main game
    play = True
    while play:
        playerHP = random.randint(90, 100)
        enemyHP = random.randint(90, 100)
        
        # Get side
        print("Wizarding Battle\n")
        print("The war for the wizarding world has begun.  What side are you on?")
        prompt = True
        while prompt:
            side = input("Enter Order of the Phoenix (1) or Death Eaters (2):  ")
            if side.lower == "order of the phoenix" or side == "1":
                characters = order
                enemy = random.choice(deathEaters)
                playerMoves = lightMoves
                enemyMoves = darkMoves
                prompt = False
            elif side.lower == "death eaters" or side == "2":
                characters = deathEaters
                enemy = random.choice(order)
                playerMoves = darkMoves
                enemyMoves = lightMoves
                prompt = False
            else:
                print("Invalid input.")
        
        # Get character
        player = ""
        while player not in characters:
            print("Character choices: ", characters)
            player = input("Enter a character:  ")
        
        print("\nThe hated {} appears and starts to attack you.".format(enemy))
        
        fight = True
        while fight:
            fight = attack(player, playerMoves, enemy, enemyMoves)
        
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

