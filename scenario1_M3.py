# Ändringar gjorda av P:
# 1. Bytt ut print till slow_print på allt förutom alternativ-listor (och ändrat till f-string där det behövdes)
# 2. I funktion def choose_scenario, tog bort \n ur print(f"{scenario}) {scenarios[scenario]}") och la till på slutet av print("\nChoose a scenario:\n")

#Ändringar gjorda av M efter P:
# 1. Justerat så response_reaction för sista frågan innehåller reaktionen + positivt eller negativ respons på sista valet.
# 2. Ändrat scenario outro-texten till "End scenario 'Scenario namnet'.
# 3. Uppdaterat funktionen outro till att skriva ut outro text, reseta step och fail till basvärdena och sen gå tillbaka till choose_scenario
# 4. La till outro-funktionen i play scenario även efter fail så man misslyckas och får gå tillbaka till menyn
# 5. Lite andra små textgrejer med nya rader, blankrad etc. 

scenarios = {
    "a": "First day of university",
    "b": "Library",
    "c": "Pub",
    "q": "End the game"
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
                slow_print("\nLibrary scenario is coming soon!")
            
            elif scenario_choice == "c":
                slow_print("\nPub scenario is coming soon!")
            
            elif scenario_choice == "q":
                slow_print("\nGoodbye, see you another time!")
                return
        
        slow_print("\nUnavailable option, try again.")
        
#-------------end main-------------------------------------
        
#scenario_name is list of all the text to a specific scenario
#scenario_uni = []

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

#situations, a dictionary of the libraries with questions, responses and response-reactions
situations_uni = {
    1: (questions_uni, responses_q1_uni, resp_reaction_q1_uni),
    2: (questions_uni, responses_q2_uni, resp_reaction_q2_uni),
}

#scenario, one list per scenario which gets all the scenario texts from the bundled situations as well as the intro_outr texts
scenario_uni = [intro_outro_uni, situations_uni]


#------------------start of scenario functions----------------------

# a number to navigate where in the scenario the user is, corresponds to questions, responses and resp_reactions
# at the end os a situation the number should increase os stay the same in order to iniate next step, or play same step again?
step = 1
fail = 0

#function move on, to continue the story
def move_on():
    input("\n[Press enter to continue]")

def intro(text):
    slow_print(text[0])
    
def outro(text):
    slow_print(f"\n{text[1]}")
    global step
    global fail
    step = 1
    fail = 0
    input("[Press enter to go back to main menu - Choose scenario]")
    choose_scenario()
    #return to main

#this function subtrakts 1 from the global parameter step which decides which situation is beaing played out.
    #it is used after one of the vague answer options to give the user a second chance at the specifik situation
def try_again():
    global step
    answer = input("\nYour response might have been a bit vague or lacking some information. \n\nWould you like to try the interaction again? [y / n]: ")
    if answer == "y":
        step -= 1
    return

# function show_response controls how the chosen option shall be printed, type is to separate a talking response from an acting response
def show_response(answer, responses):
    chosen = responses[answer]
    if chosen["type"] == "speech":
        slow_print(f'\nYou: "{chosen["text"].format(name=name)}"')
    else:
        slow_print(f'\nYou {chosen["text"]}.')

def situation(question, responses, resp_reaction):
    global step
    global fail
    slow_print(f"\n{question[step]}")
    slow_print("\nHow do you respond?\n")
    while True:
        for n in responses:
            print(f"{n}) {responses[n]['text'].format(name=name)}")
        answer = input("\nYour response: ")
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
        else:
            slow_print("\nOoops, it seems you chose and unavailable response. \nTry again, here are the options that are available:\n")

#a funcion which calls the situation dictionary based on the number of the global variable step
def next_step(situations):
    if step in situations:
        question, responses, resp_reaction = situations[step]
        situation(question, responses, resp_reaction)

def play_scenario(scenario_choice):
    scenario = scenario_choice
    intro_outro = scenario[0]
    situations = scenario[1]
    intro(intro_outro)
    move_on()
    while step in situations:
        if fail >= len(situations)/2:
            slow_print("\nYou failed socially, better luck next time.")
            outro(intro_outro)
            return
        else:
            next_step(situations)
            move_on()
    outro(intro_outro)




#Testkörning
start_game()
