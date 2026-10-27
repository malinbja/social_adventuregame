scenarios = {
    "a": "First day of university",
    "b": "Library",
    "c": "Pub",
    "q": "End the game"
}

questions = {
    "uni": {
        "q1":"Hello, my name is Edgar. What's your name?",
        "q2":"Nice to meet you! Have you studied math before?",
        "q3":"Oh, me neither! Are you nervous about the course?"
    }
}

options = {
    "uni": {
        "q1": {
            "a": {"text": "Hi, my name is {name}!", "type": "speech"},
            "b": {"text":"Hi.", "type": "speech"},
            "c": {"text": "stay quiet, looking down at your shoes", "type": "action"},
            "q": {"text": "end the game", "type": "action"}
        },
        "q2": {
            "a":{"text": "Yes, I love math and am really looking forward to this course!", "type": "speech"},
            "b":{"text": "No.", "type": "speech"},
            "c":{"text": "stay quiet", "type": "action"},
            "q":{"text": "end the game", "type" : "action"}
        },
        "q3": {
            "a": {"text": "A little, but I'm excited to learn something new!", "type": "speech"},
            "b": {"text": "Yeah, I guess.", "type": "speech"},
            "c": {"text": "stay quiet and look away", "type": "action"},
            "q": {"text": "end the game", "type" : "action"}
        }
    }
}

reactions = {
    "uni": {
        "q1": {
            "a": "Edgar smiles at you.",
            "b": "Edgar nods.",
            "c": "Edgar looks a little confused. After waiting a moment, he assumes you are not interested and walks away.",
            "q": "Goodbye, see you another time!"
        },
        "q2": {
            "a": "Edgar nods excitedly and then checks the time.",
            "b": "Edgar looks a little confused.",
            "c": "Edgar waits for a response for a bit, but gives up and goes into the lecture.",
            "q": "Goodbye, see you another time!"
        },
        "q3": {
            "a": "Edgar nods in agreement and smiles.",
            "b": "Edgar gives you a smile.",
            "c": "Edgar gives up and leaves for the lecture.",
            "q": "Goodbye, see you another time!"
        }
    }
}

closing_dialogues = {
    "a": "The lecture is starting, let's go in and find good seats!",
    "b": "You'll get the hang of it."
}

# imported module for configuration of e.g. slow_print
import time

def slow_print(text):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(0.03)
    print()

# function get_response controls print of options after questions
def get_response(options, name):
    while True:
        print("\nHow do you respond?")
        for option in options:
            print(f"\n{option}) {options[option]['text'].format(name=name)}")
        
        response = input("\nYou chose: ").lower()
    
        if response in options:
            return response
        
        slow_print("\nUnavailable option, try again.")

# function show_response controls how the chosen option shall be printed, type is to separate a talking response from an acting response
def show_response(response, options, name):
    chosen = options[response]
    if chosen["type"] == "speech":
        slow_print(f'\nYou: "{chosen["text"].format(name=name)}"')
    else:
        slow_print(f'\nYou {chosen["text"]}.')

# function npc_reaction controls the reaction of npc and returns to the scenario
def npc_reaction(response, reactions):
    return reactions[response]

# function unsuccessful_ending controls what to be printed when bad ending
def unsuccessful_ending():
    slow_print("\nYou did not succeed socially, better luck next time.")

# function successful_ending controls what to be printed when good ending
def successful_ending():
    slow_print("\nCongratulations, you made a friend!")

# function ok_ending controls what to be printed when ending was not good, but not bad either
def ok_ending():
    slow_print("\nYou made it through the conversation, but didn't quite make a new friend. Maybe next time!")

# function start_game is what starts the game, controls the introducing text and will call on a menu function for scenarios to play
def start_game():
    slow_print("Welcome to the adventures of social interactions!")
    name = input("\nWhat is your name? ")
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
                university_scenario(name)
                return
            
            elif scenario_choice == "b":
                slow_print("\nLibrary scenario is coming soon!")
            
            elif scenario_choice == "c":
                slow_print("\nPub scenario is coming soon!")
            
            elif scenario_choice == "q":
                slow_print("\nGoodbye, see you another time!")
                return
        
        slow_print("\nUnavailable option, try again.")

# function university_scenario controls this specific scenario
def university_scenario(name):
    slow_print("\nWelcome to the first day of university!")
    input("\n(press enter)")
    slow_print("\nYou are standing outside a lecture hall. Another student is standing next to you.")
    input("\n(press enter)")
    slow_print(f"\nEdgar: {questions['uni']['q1']}")
    response = get_response(options['uni']['q1'], name)
    show_response(response, options['uni']['q1'], name)
    reaction = npc_reaction(response, reactions['uni']['q1'])
    slow_print(f"\n{reaction}")
    
    while response == "b":
        slow_print(f"\nEdgar: {questions['uni']['q1']}")
        response = get_response(options['uni']['q1'], name)
        show_response(response, options['uni']['q1'], name)
        reaction = npc_reaction(response, reactions['uni']['q1'])
        slow_print(f"\n{reaction}")
    
    if response == "a":
        slow_print(f"\nEdgar: {questions['uni']['q2']}")
        response_two = get_response(options['uni']['q2'], name)
        show_response(response_two, options['uni']['q2'], name)
        reaction_two = npc_reaction(response_two, reactions['uni']['q2'])
        slow_print(f"\n{reaction_two}")
        
        if response_two == "a":
            slow_print(f"\nEdgar: {closing_dialogues['a']}")
            successful_ending()
            return
        
        elif response_two == "b":
            slow_print(f"\nEdgar: {questions['uni']['q3']}")
            response_three = get_response(options['uni']['q3'], name)
            show_response(response_three, options['uni']['q3'], name)
            reaction_three = npc_reaction(response_three, reactions['uni']['q3'])
            slow_print(f"\n{reaction_three}")
            if response_three == "a":
                slow_print(f"\nEdgar: {closing_dialogues['a']}")
                successful_ending()
                return
            elif response_three == "b":
                slow_print(f"\nEdgar: {closing_dialogues['b']}")
                ok_ending()
                return
            elif response_three == "c":
                unsuccessful_ending()
                return
            elif response_three == "q":
                return
        
        elif response_two == "c":
            unsuccessful_ending()
            return
        elif response_two == "q":
            return
    
    elif response == "c":
        unsuccessful_ending()
        return
    
    elif response == "q":
        return
           