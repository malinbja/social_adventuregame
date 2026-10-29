# M: Val att göra: skulle vi ta bort "How do you respond" från situations och lägga till i varje enskild fråga istället?
# Isf behöver scenario uni justeras. Nu i party blir det dubbelt
# för val c på sista frågan , check mot step och ta inte med frågan om att prova interaktionen igen. 

scenarios = {
    "a": "First day of university",
    "b": "Library",
    "c": "House party with people from uni",
    "q": "End the game"
}

drinks = {
    "be" : "Beer",
    "gt" : "Gin & tonic",
    "rc" : "Rom & coke",
    "wi" : "Wine",
    "wa" : "Water",
    "co" : "Coffee",
    "du" : "..How many alcohol units am I currently at?"
    }

#----------------main functions--------------------
# imported module for configuration of e.g. slow_print
import time
name = " "

def slow_print(text):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(0.03)
    print()

def set_name():
    global name
    name = input("\nWhat is your name? ")
    return name


# function start_game is what starts the game, controls the introducing text and will call on a menu function for scenarios to play
   
def start_game():
    slow_print("Welcome to the adventures of social interactions!")
    set_name()
    slow_print(f"\nHello {name}, let's see what you want to explore today.")
    choose_scenario()


# function choose_scenario controls the menu for the alternative senarios to play
def choose_scenario():
    while True:
        print("\nChoose a scenario:\n")
        for scenario in scenarios:
            print(f"{scenario}) {scenarios[scenario]}")
        
        scenario_choice = input("\nYou chose: ").lower()
        
        if scenario_choice in scenarios:
            if scenario_choice == "a":
                play_scenario(scenario_uni)
                return
            
            elif scenario_choice == "b":
                play_scenario(scenario_lib)
                return
            
            elif scenario_choice == "c":
                play_scenario(scenario_party)
                return
            
            elif scenario_choice == "q":
                slow_print("\nGoodbye, see you another time!")
                return
        
        slow_print("\nUnavailable option, try again.")
        
#-------------end main-------------------------------------
        
#----------START scenario uni---------------

#intro and outro text in a list, could also be a duple..
intro_outro_uni = ["\nThis is the first day at uni. You are standing outside the lecture hall, \nwaiting for your first introductury lecture on computer science to start. \nA person who seems to be of the same age as you is standing next to you." ,
               "End scenario 'First day at university'\n"]

#questions. dictionary med frågor. nycklarna är numrerade i ordningen frågorna kommer i scenariot
questions_uni = {1 : "The person turns to you and says: \n'Hi, my name is Bob. What is your name?'",
             2 : "Bob asks a second questions: \n'Do you have any experience in this topic from before?'"}

#responses q1-n. En dictionary med möjliga svar a-d för q1, q2 osv.
responses_q1_uni = {
    "a": {"text": "Hi my name is {name}.", "type":"speech"},
    "b": {"text": "Hi.", "type": "speech"},
    "c": {"text": "I don't know.", "type": "speech"},
    "q": {"text": "[exit the game]", "type": "action"}
}

responses_q2_uni = {
    "a": {"text": "Yes I have been coding a bit before. I enjoy it.", "type": "speech"},
    "b": {"text": "No I am completely new at this.", "type": "speech"},
    "c": {"text": "I don't know.", "type": "speech"},
    "q": {"text": "[exit the game]", "type": "action"}
}

#respons reaction till svaren till frågorna q1-n. En dictionary med reaktionen till svaren a-d för q1, q2 osv.
resp_reaction_q1_uni = {"a" : "Bob answers: 'Hi {name}, nice to meet you!'",
                    "b" : "Bob looks a little perplexed as you didn't answer with your name.",
                    "c" : "Bob looks a bit puzzled but then he givas a small chuckle, assuming \nyou made a joke not knowing your own name. "}
resp_reaction_q2_uni = {"a" : "Bob seems impressed to hear that you have some knowledge in the area and says: 'That will probably be very useful in this course! Come, let's go and find good seats before it starts.' \n\nWhat a great start to your studies - you just made a friend!\n",
                    "b" : "Bob smiles and says: 'That's nice to hear I'm not the only newbie here. Come, let's go and find good seats before it starts.'\n\nWhat a great start to your studies - you just made a friend!\n" ,
                    "c" : "Bob seem puzzled by your response."}

#endings, to be printed after fail-evaluation of the scenario
endings_uni = {"a" : "You successfully navigated your first day at uni! Well done!",
                    "b" : "You had some success and some less successful social interactions. Keep at it!" ,
                    "c" : "You did not succeed in this scenario. Keep working on your social interaction skills. "
               }

#situations, a dictionary of the libraries with questions, responses and response-reactions
situations_uni = {
    1: (questions_uni, responses_q1_uni, resp_reaction_q1_uni),
    2: (questions_uni, responses_q2_uni, resp_reaction_q2_uni),
}

#-----------------------END scenario uni-----------------------
#--------------------- START scenario library-------------------
#scenario_name is list of all the text to a specific scenario
#scenario_uni = []

#intro and outro text in a list, could also be a duple..
intro_outro_lib = ["\nYou have been assigned to a group to work together on a programming project. \nYou have decided to meet up in the library to study together, so you get to the library. \nYou see the students in your group sitting at a table and walks towards them. \nOne of the students waves to you and points to the empty chair at the table." ,
                   "End scenario 'Study session in the library'\n"]


#questions. dictionary med frågor. nycklarna är numrerade i ordningen frågorna kommer i scenariot
questions_lib = {1: "Student says: \n'Hey there, grab a seat! I'm Vicky, what's your name?'",
                 2: "Kevin turns to you and ask: \n'Tell us a little about yourself. Are you from Uppsala?'",
                 3: "Cornelia asks you: \n'So you're name is {name} and you are from Stockholm. What else can you tell us about yourself?'",
                 4: "Vicky opens her note book while saying: \n'Alright, let's get started with this project. {name}, do you have any suggestions?'",
                 5: "Cornelia: 'So it's decided then, we make a food planner. {name}, could you be in charge of the inventory part?'",
                 6: "To be written"}

#responses q1-n. En dictionary med möjliga svar a-d för q1, q2 osv.
responses_q1_lib = {
    "a": {"text": "Hi everyone, I am {name}!", "type": "speech"},
    "b": {"text": "Hello.", "type": "speech"},
    "c": {"text": "stay quiet, but grab the empty seat.", "type": "action"},
    "q": {"text": "[exit the game]", "type": "action"}
}

responses_q2_lib = {
    "a": {"text": "Actually I am from Stockholm originally, but I moved to Uppsala for studies. How about you guys?", "type": "speech"},
    "b": {"text": "No, Im not.", "type": "speech"},
    "c": {"text": "feel very shy and fail to answer Kevins question.", "type": "action"},
    "q": {"text": "[exit the game]", "type": "action"}
}

responses_q3_lib = {
    "a": {"text": "Well, I love to paint and sing on my free time. I'm also very interested in programming, which is why I chose to study data science.", "type": "speech"},
    "b": {"text": "Oh, ehm... I'm not sure what to tell you, I like programming.", "type": "speech"},
    "c": {"text": "I don't really see why that matters.", "type": "speech"},
    "q": {"text": "[end the game]", "type": "action"}
}

responses_q4_lib = {
    "a": {"text": "Well, I thought about building a program for food planning. You could have an inventory for your ingredients and have the program suggesting what ingredients to cook with. What do you think?", "type": "speech"},
    "b": {"text": "Oh, I don't know... There are so many options. Something with food maybe.", "type": "speech"},
    "c": {"text": "Nah, I don't really care, what ever you wanna do...", "type": "speech"},
    "q": {"text": "[end the game]", "type": "action"}
}

responses_q5_lib = {
    "a": {"text": "Of course, I have some design ideas already. I'll get into it right away!", "type": "speech"},
    "b": {"text": "I guess I can make that part.", "type": "speech"},
    "c": {"text": "Sure, fine, whatever.", "type": "speech"},
    "q": {"text": "[end the game]", "type": "action"}
}

responses_q6_lib = {
    "a": {"text": "To be written", "type": "speech"},
    "b": {"text": "To be written", "type": "speech"},
    "c": {"text": "To be written", "type": "speech"},
    "q": {"text": "[end the game]", "type": "action"}
}   

#respons reaction till svaren till frågorna q1-n. En dictionary med reaktionen till svaren a-d för q1, q2 osv.
resp_reaction_q1_lib = {"a": "Vicky smiles at you and says: 'So this is Kevin and Cornelia.'\nKevin and Cornelia waves at you.",
                        "b": "Vicky smiles politely and says: 'Well, this is Kevin and Cornelia'. \nCornelia raises an eyebrow and says: 'You forgot to say your name.' \nYou blush and tell them your name is {name}.",
                        "c": "The other students exchanges confused glances and there's a moment of awkward silence. \nThen Vicky says: 'Ehm... Well, anyway, this is Kevin and Cornelia.' \nAs the group keeps looking at you, expecting you to respond, you quietly tell them your name is {name}.",}

resp_reaction_q2_lib = {"a": "Kevin gives you a smerk and answers: 'Stockholm is great, but nothing beats Uppsala. Born and raised!' \nCornelia nods agreeingly and says: 'I'm also born and raised here, but Vicky also moved here from... \nWhere was it, Vic?' \nVicky says: 'I came all the way from Arjeplog. It is a small town up in the north.'",
                        "b": "There's a bit of silence in the group, though your response was a bit uninformative. \nCornelia asks: 'Where are you from, then?' \nYou tell them that you are from Stockholm.",
                        "c": "The situation got clearly awkward. Cornelia rolls her eyes and turns to Vicky. \nVicky tries to be friendly and says: 'Can you tell us where you are from?' \nYou whisper a quiet 'Stockholm.' and feel ashamed."}

resp_reaction_q3_lib = {"a": "Kevin gets very interested and says: 'Oh, I love singing too. I'm actually in the choir of my student nation. Maybe you should join too!' \nYou smile and nod.",
                        "b": "Cornelia shrugs her shoulders and says: 'Well I guess that's the reason we all study data science.'",
                        "c": "Cornelia sighs loudly and gives Vicky an annoyed look.\nVicky hesitates for a moment, but says: 'We just want to get to know you, thats all...' \n The group atmosphere is noticeably stiff now."}

resp_reaction_q4_lib = {"a": "The group looks interested in your suggestion. \nKevin says: 'Nothing food related can go wrong, right?' \nVicky and Cornela nods agreeingly and you feel proud of your idea.",
                        "b": "Kevin nods slowly and says: 'Food is always nice i suppose.' \nCornelia suggests: 'Maybe some sort of food planner?' \nVicky looks at you and say: 'Is a planner of some sort what you have in mind?' \nYou nod and agrees that a food planning program should be a good project.",
                        "c": "The group notice that you are not very into the group project. \nVicky turns to the others in the group for ideas, while you remain silent. \nThe group decides to make a food planning program."}

resp_reaction_q5_lib = {"a": "Cornelia looks pleased and says: 'Great! I'll look up how to build a function for keeping track of available ingredients.' \nVicky adds: 'Me and Kevin can work together with how to program the suggestions for ingredients to use!.' \nYou get started on the project and work on it for a couple of hours.",
                        "b": "Cornelia nods and says: 'Well, if you prefer to do another part, let us know.' \nYou shake your head and reassure her that your fine with the inventory part.\nVicky says: 'I can start looking into how to program the suggestions for ingredients to use, maybe Kevin can help me with that?' \n Kevin nods and says: 'Sure thing, and maybe you can look into a function for keeping track of the inventory, Cornelia?' \nCornelia agrees and you get started with the project.",
                        "c": "The group exchanges looks, Cornelia sighs, Kevin rolls his eyes and Vicky feels a bit tired of your lack of engagement.\n The group starts planning what to get done, and there is some tention during your study session."}

resp_reaction_q6_lib = {"a": "To be written",
                       "b": "To be written",
                       "c": "To be written"}

#endings, to be printed after fail-evaluation of the scenario
endings_lib = {"a" : "You successfully navigated this scenario in the library! Well done!",
                    "b" : "You had some success and some less successful social interactions. Keep at it!" ,
                    "c" : "You did not succeed in this scenario. Keep working on your social interaction skills. "
               }


#situations, a dictionary of the libraries with questions, responses and response-reactions
situations_lib = {
    1: (questions_lib, responses_q1_lib, resp_reaction_q1_lib),
    2: (questions_lib, responses_q2_lib, resp_reaction_q2_lib),
    3: (questions_lib, responses_q3_lib, resp_reaction_q3_lib),
    4: (questions_lib, responses_q4_lib, resp_reaction_q4_lib),
    5: (questions_lib, responses_q5_lib, resp_reaction_q5_lib),
    6: (questions_lib, responses_q6_lib, resp_reaction_q6_lib)
}


#-----------------------END scenario library-----------------------

#--------------------- START House party with people from uni-------------------
#intro and outro text in a list, could also be a duple..
intro_outro_party = ["\nIt is Friday night and all your classmates are invited to a party at Quinn's house, a girl in your class.\nYou are approaching the frontdoor and can already hear the music and loud chatter inside.\n You reach the door and ring the bell. Quinn opens and welcomes you: " ,
               "End scenario 'House party with people from uni'\n"]

#questions. dictionary med frågor. nycklarna är numrerade i ordningen frågorna kommer i scenariot
questions_party = {1 : "\n 'Hello {name}, so glad you made it! Come in, you can put the shoes here, jacket there. And do you need to put anything in the fridge?'",
                   2 : " \nYou enter the kitchen. A group of four people are standing by the sink, mixing what seems to be ramen soup with spirits. \n\nWhat do you do next?\n",
                   3 : "What happens after the noodles.. An opening to talk and or participate?",
                   4 : "Final kitchen interaction.. How do you respond"}

#responses q1-n. En dictionary med möjliga svar a-d för q1, q2 osv. +
#respons reaction till svaren till frågorna q1-n. En dictionary med reaktionen till svaren a-d för q1, q2 osv.
responses_q1_party = {"a" : {"text": "Great, yes I brought a few beers.", "type" : "speech"},
                     "b" : {"text": "Thank you, oh no I don't think so.", "type" : "speech"},
                     "c" : {"text" : "I didn't bring any food.", "type" : "speech"}, 
                     "q" : {"text" : "[exit the game]", "type" : "action"}
                      }
resp_reaction_q1_party = {"a" : "Quinn answers: 'Awesome, it's getting a bit full but feel free to move things around in there. Also, there's a bowl of punch on the kitchen counter - please help yourself!'\n\nSomeone calls for Quinn in the livingroom, she gives you a big smile and then turns around toward the hustle and bustle. \nYou leave your shoes and jacket in the hallway and head into the kitchen.",
                          "b" : "Quinn ansers: 'Alright, if you change your mind just go ahead anyway. Also, there's a bowl of punch on the kitchen counter - please help yourself!'\nSomeone calls for Quinn in the livingroom, she gives you a big smile and then turns around toward the hustle and bustle. \nYou leave your shoes and jacket in the hallway and head into the kitchen.",
                          "c" : "Quinn looks a bit puzzled but then she givas a small chuckle and says: \n'That's cool, if you also forgot drinks, there's a bowl of punch on the kitchen counter - please help yourself!' \nSomeone calls for Quinn in the livingroom, she gives you a big smile and then turns around toward the hustle and bustle. \nYou leave your shoes and jacket in the hallway and head into the kitchen."
                          }

responses_q2_party = {"a" : {"text" : "Put your stuff in the fridge and says: 'Something half funny about noodles and alcohol'", "type" : "action"},
                     "b" : {"text" : "Watch the group while getting a cup of the pink punch. ", "type" : "action"},
                     "c" : {"text" : "You stop by the kitchen counter an watches the experiments from a safe distance.", "type" : "action"},
                     "d" : {"text" : "drink", "type" : "action"},
                     "q" : {"text" : "[exit the game]", "type" : "action"}
                      }
resp_reaction_q2_party = {"a" : "The group reacts to the half joke.",
                     "b" : "The drink tastes like a hubba bubba-chewing gum mixed with hand sanitizer and you instinctly spit it back into the cup. \nMore reaction from the group.",
                     "c" : "Stuff happening with the noodles",
                     "d" : "drink - no print, loop to options"
                          }

responses_q3_party = {"a" : {"text" : "Answers something.", "type" : "speech"}, 
                     "b" : {"text" : "Another type of answer.", "type" : "speech"}, 
                     "c" : {"text" : "Look away and stay silent. ", "type" : "speech"}, 
                     "d" : {"text" : "drink", "type" : "action"}, 
                     "q" : {"text" : "[exit the game]", "type" : "action"} 
                      }
resp_reaction_q3_party = {"a" : "reaction to answer  a",
                     "b" : "reaction to answer b",
                     "c" : "maybe reaction to c.",
                     "d" : "drink - no print, loop to options"
                          }

responses_q4_party = {"a" : {"text" : "Response a, stays part of the convo.", "type" : "speech"}, 
                     "b" : {"text" : "Response b, stays present in the group", "type" : "speech"}, 
                     "c" : {"text" : "Response c, stays passive", "type" : "action"}, 
                     "d" : {"text" : "drink", "type" : "action"}, 
                     "q" : {"text" : "[exit the game]", "type" : "action"} 
                            }
resp_reaction_q4_party = {"a" : "Response to q4 answer a. \n!",
                     "b" : "Response to q4 answer b. \n",
                     "c" : "Response to q4 answer c. \n",
                     "d" : "drink - no print, loop to options"}

#endings, to be printed after fail-evaluation of the scenario
endings_party = {"a" : "\nWhat an eventful night! You did a good job putting yourself out there tonight and you managed to successfully engage with your classmates. Good job! You successfully navigated your first house party at uni! Well done!",
                    "b" : "\nWhat an eventful night! You did a good job putting yourself out there tonight and you managed to successfully engage with your classmates. Good job! You had some success and some less successful social interactions. Keep at it!" ,
                    "c" : "\nWhat an eventful night! You did not completely emerge in the social activities but at least you participated the whole night trough. Good job but keep working on your social interaction skills. "
               }

#situations, a dictionary of the libraries with questions, responses and response-reactions
situations_party = {
    1: (questions_party, responses_q1_party, resp_reaction_q1_party),
    2: (questions_party, responses_q2_party, resp_reaction_q2_party),
    3: (questions_party, responses_q3_party, resp_reaction_q3_party),
    4: (questions_party, responses_q4_party, resp_reaction_q4_party)
}

#----------------INTOX state-----------------------------------
#intoxicated state with alternative situations
#questions. dictionary med frågor. nycklarna är numrerade i ordningen frågorna kommer i scenariot
intro_outro_intox_party = ["\nIt is Friday night and all your classmates are invited to a party at Quinn's house, a girl in your class.\nYou are approaching the frontdoor and can already hear the music and loud chatter inside.\n You reach the door and ring the bell. Quinn opens and welcomes you: " ,
               "End scenario 'intox-House party with people from uni'\n"]

questions_intox_party = {3 : "You are drunk.. What happens after the noodles.. An opening to talk and or participate?",
                   4 : "You are drunk.. Final kitchen interaction.. How do you respond"}

responses_q3_intox_party = {"a" : {"text" : "Drunk, Answers something.", "type" : "speech"}, 
                     "b" : {"text" : "Drunk, Another type of answer.", "type" : "speech"}, 
                     "c" : {"text" : "Drunk, Look away and stay silent. ", "type" : "speech"}, 
                     "d" : {"text" : "drink", "type" : "action"}, 
                     "q" : {"text" : "[exit the game]", "type" : "action"} 
                      }
resp_reaction_q3_intox_party = {"a" : "You are drunk. reaction to answer  a",
                     "b" : "You are drunk. reaction to answer b",
                     "c" : "You are drunk. maybe reaction to c.",
                     "d" : "You are drunk. drink - no print, loop to options"
                          }

responses_q4_intox_party = {"a" : {"text" : "Drunk, Response a, stays part of the convo.", "type" : "speech"}, 
                     "b" : {"text" : "Drunk, Response b, stays present in the group", "type" : "speech"}, 
                     "c" : {"text" : "Drunk, Response c, stays passive", "type" : "action"}, 
                     "d" : {"text" : "drink", "type" : "action"}, 
                     "q" : {"text" : "[exit the game]", "type" : "action"} 
                            }
resp_reaction_q4_intox_party = {"a" : "You are drunk. Response to q4 answer a. \n",
                     "b" : "You are drunk. Response to q4 answer b. \n",
                     "c" : "You are drunk. Response to q4 answer c. \n",
                     "d" : "drink - no print, loop to options"}

#endings, to be printed after fail-evaluation of the scenario
endings_intox_party = {"a" : "\nYou successfully got plastered. Well done! \nWhat an eventful night! You did a good job putting yourself out there tonight and you managed to successfully engage with your classmates. Good job!",
                    "b" : "\nWhat an eventful night! You did a good job putting yourself out there tonight and you managed to successfully engage with your classmates. Good job! You had some success and some less successful social interactions and you got hammered. Keep at it!" ,
                    "c" : "\nWhat an eventful night! You did not completely emerge in the social activities but at least you participated the whole night trough. Good job! But keep working on your social interaction skills. "
               }

#the alternative situations when intoxicated. A dictionary of the libraries with questions, responses and response-reactions
situations_intox_party = {
    1: (questions_party, responses_q1_party, resp_reaction_q1_party),
    2: (questions_party, responses_q2_party, resp_reaction_q2_party),
    3: (questions_intox_party, responses_q3_intox_party, resp_reaction_q3_intox_party),
    4: (questions_intox_party, responses_q4_intox_party, resp_reaction_q4_intox_party)
}
#----------------------END House party with peopla from uni-------------

#---------------SCENARIOS to be called upon in play_scenario-------------

#scenario, one list per scenario which gets all the scenario texts from the bundled situations as well as the intro_outr texts
scenario_uni = [intro_outro_uni, situations_uni, endings_uni]
scenario_lib = [intro_outro_lib, situations_lib, endings_lib]
scenario_party = [intro_outro_party, situations_party, endings_party, situations_intox_party, intro_outro_intox_party, endings_intox_party]


#------------------start of scenario functions----------------------

# a number to navigate where in the scenario the user is, corresponds to questions, responses and resp_reactions
# at the end os a situation the number should increase os stay the same in order to iniate next step, or play same step again?
step = 1
fail = 0
drink_units = 0

#function move on, to continue the story
def move_on():
    input("\n[Press enter to continue]")

def intro(text):
    slow_print(text[0])
    
def outro(text):
    slow_print(f"\n{text[1]}")
    global step
    global fail
    global drink_units
    step = 1
    fail = 0
    drink_units = 0
    input("[Press enter to go back to main menu - Choose scenario]")
    choose_scenario()
    #return to main

#this function subtrakts 1 from the global parameter step which decides which situation is beaing played out.
    #it is used after one of the vague answer options to give the user a second chance at the specifik situation
def try_again():
    global step
    global fail
    answer = input("\nYour response might have been a bit vague or lacking some information. \n\nWould you like to try the interaction again? [y / n]: ")
    if answer == "y":
        step -= 1
        fail -= 1
    return

def quit_scenario():
    global step
    global fail
    global drink_units
    step = 1
    fail = 0
    drink_units = 0
    choose_scenario()

#this function displays how many units of alcohol the user is at
def show_drink_units():
    slow_print(f"\nYour current level of alcohol intoxicatiob is {drink_units} units. \nYou can lover the count by drinking water or coffee.")
    move_on()

#for scnearios with drinking option, this function adds or subtracts alcohol units from the global parameter drink_units
def drink():
    global drink_units
    while True:
        slow_print("\nWhat do you drink?\n")
        for d in drinks:
            print(f"{d} : {drinks[d]}")
        answer = input("\nI take a sipp of: ")
        if answer in ("be", "wi"):
            drink_units += 1
            return
        elif answer in ("gt", "rc"):
            drink_units += 2
            return
        elif answer == "co":
            drink_units -= 2
            return
        elif answer == "wa":
            drink_units -= 1
            return
        elif answer == "du":
            show_drink_units()
        else:
            slow_print("\nUnavailable option, try again.") 

#function to evaluate fail-ratio for the scenario and choose suitable end-feedback
def ending(situations, endings):
    if fail >= len(situations)/2:
        slow_print(f"\n{endings["c"].format(name=name)}")
    elif fail < len(situations)/3:
        slow_print(f"\n{endings["a"].format(name=name)}")
    else:
        slow_print(f"\n{endings["b"].format(name=name)}")
    

# function show_response controls how the chosen option shall be printed, type is to separate a talking response from an acting response
def show_response(answer, responses):
    chosen = responses[answer]
    if chosen["type"] == "speech":
        slow_print(f'\nYou: "{chosen["text"].format(name=name)}"')
    else:
        slow_print(f'\nYou {chosen["text"]}')

def situation(question, responses, resp_reaction):
    global step
    global fail
    slow_print(f"\n{question[step].format(name=name)}")
    slow_print("\nHow do you respond?\n")
    while True:
        for n in responses:
            print(f"{n}) {responses[n]['text'].format(name=name)}")
        answer = input("\nYour response: ")
        if answer in responses:
            show_response(answer, responses) 
            if answer == "c":
                slow_print(f"\n{resp_reaction[answer].format(name=name)}")
                try_again()
                step += 1
                fail += 1
                return
            elif answer in ("a", "b"):
                slow_print(f"\n{resp_reaction[answer].format(name=name)}")
                step += 1
                return
            elif answer == "d":
                drink()
            elif answer == "q":
                quit_scenario()
        else:
            slow_print("\nOoops, it seems you chose and unavailable response. \nTry again, here are the options that are available:\n")

#a funcion which calls the situation dictionary based on the number of the global variable step
def next_step(situations):
    if step in situations:
        question, responses, resp_reaction = situations[step]
        situation(question, responses, resp_reaction)

def alt_scenario(current_scenario):
    scenario = current_scenario
    intro_outro = scenario[4]
    situations = scenario[3]
    while step in situations:
        if fail >= len(situations)/2:
            slow_print("\nYou failed socially, better luck next time.")
            outro(intro_outro)
            return
        elif drink_units >= 5:
            next_step(situations)
            move_on()
            return
        else:
            play_scenario(scenario)
    outro(intro_outro)

def play_scenario(scenario_choice):
    scenario = scenario_choice
    intro_outro = scenario[0]
    situations = scenario[1]
    endings = scenario[2]
    intro(intro_outro)
    move_on()
    while step in situations:
        if fail >= len(situations)/2:
            slow_print("\nYou failed socially, better luck next time.")
            outro(intro_outro)
            return
        elif drink_units >= 5:
            alt_scenario(scenario)
        else:
            next_step(situations)
            move_on()
    ending(situations, endings)
    outro(intro_outro)


#Testkörning
#start_game()
