# 3. Text-based Adventure Game
# This is a basic version of the Adventure game. It is completely text-based. 
# In this version of the game, users can move about through different rooms within a single setting, and based on the user input, 
# it will provide descriptions for each room.
# Movement direction is crucial here – you must create walls and set the directions in which the users can move through the rooms, 
# set movement restrictions, and also include a tracker that can track how far a user has walked or moved in the game. 
# Mentioning Python projects can help your resume look much more interesting than others.



visit = input("Which room you want to visit? master for Mater Bed Room | bedroom for Bed Room: ")
if visit == 'master':
    visit = input("Welcome to master bed room! \nWhere you want to go next? right for bedroom | left for dinning room")
    if visit == 'right':
        visit = input("Welcome to bedroom! \nThere is a study room in front of this bedroom. \nWould you like to visit the study room? yes | no: ")
        if visit == 'yes':
            visit = input("Welcome to study room!\nWould you like to stay here to read books or visit the Drawing room that is on the right side of this room? stay|visit: ")
            if visit == 'visit':
                print("Take rest in drawing room...\nSee you soon... Take Care")
            else:
                print("Enjoy Reading...\nTake Care")
        else:
            print("OK! Take rest in bedroom...\nTake Care")
    elif visit == 'left':
        print("Welcome in Dinning area! \n Enjoy your meal...\nTake Care")
    else: 
        print("Invalid direction: ")

elif visit == 'bedroom':
    print("Welcome to Bedroom!Take Rest")
else: 
    print("GameOver!")
