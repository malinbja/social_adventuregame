scenarios = {
    "a": "First day of university",
    "b": "Library",
    "c": "Pub",
    "q": "End the game"
}


#----------------main functions--------------------
# imported module for configuration of e.g. slow_print
import time

def slow_print(text):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(0.03)
    print()
    
# function show_response controls how the chosen option shall be printed, type is to separate a talking response from an acting response
def show_response(response, options, scenario):
    chosen = options[response]
    if chosen["type"] == "speech":
        slow_print(f'\nYou: "{chosen["text"].format(scenario=scenario)}"')
    else:
        slow_print(f'\nYou {chosen["text"]}.')

# function start_game is what starts the game, controls the introducing text and will call on a menu function for scenarios to play
   
def start_game():
    slow_print("Welcome to the adventures of social interactions!")
    name = input("\nWhat is your name? ")
    slow_print(f"\nHello {name}, let's see what you want to explore today.")
    choose_scenario(name)


# function choose_scenario controls the menu for the alternative senarios to play
def choose_scenario(name):
    while True:
        print("\nChoose a scenario:")
        for scenario in scenarios:
            print(f"\n{scenario}) {scenarios[scenario]}")
        
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
               "What a great start to your studies - you just made a friend!"]

#questions. dictionary med frågor. nycklarna är numrerade i ordningen frågorna kommer i scenariot
questions_uni = {1 : "The person turns to you and says: \n'Hi, my name is Bob. What is your name?'",
             2 : "Bob asks a second questions: \n'Do you have any experience in this topic from before?'"}

#responses q1-n. En dictionary med möjliga svar a-d för q1, q2 osv.
responses_q1_uni = {"a" : "Hi my name is Name.",
                "b" : "Hi.",
                "c" : "I don't know.",
                "q" : "[exit the game]"}
responses_q2_uni = {"a" : "Yes I have been coding a bit before. I enjoy it.",
                "b" : "No I am completely new at this.",
                "c" : "I don't know.",
                "q" : "[exit the game]"} 

#respons reaction till svaren till frågorna q1-n. En dictionary med reaktionen till svaren a-d för q1, q2 osv.
resp_reaction_q1_uni = {"a" : "Bob answers: 'Hi Name, nice to meet you!'",
                    "b" : "Bob looks a little perplexed as you didn't answer with your name.",
                    "c" : "Bob looks a bit puzzled but then he givas a small chuckle, assuming \nyou made a joke not knowing your own name. "}
resp_reaction_q2_uni = {"a" : "Bob seems impressed to hear that you have some knowledge in the area and says: 'That will probably be very useful in this course! Come, let's go and find good seats before it starts.'",
                    "b" : "Bob smiles and says: 'That's nice to hear I'm not the only newbie here. Come, let's go and find good seats before it starts.'" ,
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

#function move on, to continue the story
def move_on():
    input("\n[Press enter to continue]")

def intro(text):
    print(text[0])
    
def outro(text):
    print("\n", text[1])
    #return to main

#this function subtrakts 1 from the global parameter step which decides which situation is beaing played out.
    #it is used after one of the vague answer options to give the user a second chance at the specifik situation
def try_again():
    global step
    answer = input("\nYour response might have been a bit vague or lacking some information. \nWould you like to try the interaction again? [y / n]: ")
    if answer == "y":
        step -= 1
    return

def situation(question, responses, resp_reaction):
    global step
    print("\n", question[step])
    print("\nHow do you respond?\n")
    while True:
        for n in responses:
            print(f"{n} : {responses[n]}")
        answer = input("\nYour response: ")
        if answer == "c":
            print("\n", resp_reaction[answer])
            try_again()
            step += 1
            return
        elif answer in ("a", "b"):
            print("\n", resp_reaction[answer])
            step += 1
            return
        else:
            print("\nOoops, it seems you chose and unavailable response. \nTry again, here are the options that are available:\n")

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
        next_step(situations)
        move_on()
    outro(intro_outro)




#Testkörning
#play_scenario(scenario_uni)