
###! LOGIC

##! The madlib generator is a fun interactive storytelling game, so we have templates of story, get random inputs form the user and concatenate the 2 to generate a story.

while True:
    print("\nStories: \n1. Silly adventure \n2. Space mission \n3. School day \n4. Food fight")
    option = input("Choose a story (1, 2, ...): ")
    madlib = ""
    
    if (option.strip()).lower() == "1":
        adjective = input("Adjective: ")
        animal = input("Animal: ")
        verb = input("Verb: ")
        place = input("Place: ")
        noun = input("Noun: ")
        exclamation = input("Exclamation: ")
        color = input("Color: ")
        noun2 = input("Noun: ")

        madlib = f"One day, a {adjective} {animal} decided to {verb} to the {place}. It carried a {noun} and shouted '{exclamation}!' when it saw a {color} {noun2}."
        
    elif (option.strip()).lower() == "2":
        name = input("Name: ")
        number = input("Number: ")
        noun = input("Noun: ")
        verb = input("Verb: ")
        planet = input("Planet: ")
        
        madlib = f"Captain {name} flew the spaceship at {number} miles per hour. The alien said, 'Take me to your {noun}!' So they {verb} all the way to {planet}."

    elif (option.strip()).lower() == "3":
        adjective = input("Adjective: ")
        verb = input("Verb: ")
        noun = input("Noun: ")
        name = input("Name: ")
        exclamation = input("Exclamation: ")
        place = input("Place: ")
        
        madlib = f"In class, the {adjective} teacher made us {verb} with a {noun}. My friend {name} screamed '{exclamation}!' and ran to the {place}."

    elif (option.strip()).lower() == "4":
        food = input("Food: ")
        adjective = input("Adjective: ")
        color = input("Color: ")
        verb = input("Verb: ")
        person = input("Person: ")
        body_part = input("Body part: ")
        
        madlib = f"At lunch, someone threw a {food} that was {adjective} and {color}. It {verb} across the room and landed on {person}'s {body_part}!"

    print(madlib)
    quit = input("\nContinue? (y/n): ")
    
    if (quit.strip()).lower() == "n":
        break

