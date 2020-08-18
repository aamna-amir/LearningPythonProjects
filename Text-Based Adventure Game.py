# 3. Text-based Adventure Game
# This is a basic version of the Adventure game. It is completely text-based. 
# In this version of the game, users can move about through different rooms within a single setting, and based on the user input, 
# it will provide descriptions for each room.
# Movement direction is crucial here – you must create walls and set the directions in which the users can move through the rooms, 
# set movement restrictions, and also include a tracker that can track how far a user has walked or moved in the game. 
# Mentioning Python projects can help your resume look much more interesting than others.

rooms = {
    1: {'Master Bed Room': ['wall1','wall2','wall3','wall4'],
    2: 'Bed Room',
    3: 'Dinning Room',
    4: 'Drawing Room',
    5: 'Living Room',
    6: 'Study Room'
}

visit = None