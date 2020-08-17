# create a mad libs game!

from random import randint
import copy

story = (
    "One day my {} friend and I decided to go to the {} game in {}. We really wanted to see the {} play the {}. So we {} our {} down to the {} and bought some {}s. We got into the game and It was a lot of fun. We ate some {} {} and drank some {} {}. We had a great time! We plan to go again next year!"
)

word_dict = {
    'adjective': ['greedy','dump','chubby','groovy','rich','harsh','tasty','slow'],
    'city name': ['Gujranwala','Lahore','Karachi','Islamabad','Multan','Sialkot'],
    'noun': ['people','map','music','dog','hamster','ball','hotdog','salad'],
    'action verb': ['run','fall','crawl','beat','cray','watch','swim','jump','bounce'],
    'sports noun': ['ball','bat','dice','uniform','helmet','scoreboard','player']
}

def get_word(type, local_dict):
    '''get a random word from the word_dict based on word type'''
    words = local_dict[type]
    cnt = len(words)-1
    index = randint(0,cnt)
    return local_dict[type].pop(index)

def create_story():
    '''create a random story from word dict'''
    #create a local copy of dict so that we can pop words as used
    local_dict = copy.deepcopy(word_dict)
    return story.format(
        get_word('adjective',local_dict),
        get_word('sports noun',local_dict),
        get_word('city name',local_dict),
        get_word('noun',local_dict),
        get_word('noun',local_dict),
        get_word('action verb',local_dict),
        get_word('noun',local_dict),
        get_word('noun',local_dict),
        get_word('noun',local_dict),
        get_word('adjective',local_dict),
        get_word('noun',local_dict),
        get_word('adjective',local_dict),
        get_word('noun',local_dict),
    )

story1 = create_story()

print(story1)