scenarios = {
    "a": "First day of university",
    "b": "Library",
    "c": "Pub",
    "q": "End the game"
}

endings = {
    "successful": "Congratulations, you have succeded socially in this round!",
    "unsuccessful": "You have failed socially, better luck next time.",
    "ok": "You made it through, but didn't quite make a new friend. Maybe next time!"
}

npc_names = {
    "uni": {
        "edgar": "Edgar"
        },
    "lib": {
        "student": "Sally",
        "librarian": "Kent"
        }
}

questions = {
    "uni": {
        "q1":"Hello, my name is Edgar. What's your name?",
        "q1b": "Sorry, I didn't catch your name. What was it?",
        "q2": "So, have you studied math before?",
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
        "q1b": {
            "a": {"text": "Oh, my name is {name}!", "type": "speech"},
            "b": {"text": "Ehm, my name... Oh...", "type": "speech"},
            "c": {"text": "got too nervous to respond", "type": "action"},
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
        "q1b": {
            "a": "Edgar shines up.",
            "b": "Edgar smiles reassuringly.",
            "c": "Edgar stands with you for a bit, but though he does not receive any response, he leaves for the lecture.",
            "q": "Goodbye, see you another time!"
        },
        "q2": {
            "a": "Edgar nods excitedly and then checks the time.",
            "b": "Edgar stays quiet for a little while.",
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

# function play_dialogue controls the printing of NPC questions and reactions, calling on functions for response, returning response
def play_dialogue(scenario_id, question_id, npc_id, name):
    slow_print(f"\n{npc_names[scenario_id][npc_id]}: {questions[scenario_id][question_id]}")
    response = get_response(options[scenario_id][question_id], name)
    
    if response != "q":
        show_response(response, options[scenario_id][question_id], name)
        reaction = npc_reaction(response, reactions[scenario_id][question_id])
        slow_print(f"\n{reaction}")
        
    return response

# function try_again controls the option to retry when making a bad choice in the game
def try_again():
    while True:
        retry = input("\nThat did not go very well... \nWould you like to try the interaction again? [y / n]: ").lower()
        
        if retry in ("y", "n"):
            return retry
        
        else:
            slow_print("\nUnavailable option, try again.")
            
#
def retry_dialogue(scenario_id, question_id, npc_id, name):
    response = play_dialogue(scenario_id, question_id, npc_id, name)
    
    while response == "c":
        retry = try_again()
        
        if retry == "y":
            response = play_dialogue(scenario_id, question_id, npc_id, name)
        else:
            break
    
    return response

# function prints the ending text
def show_ending(ending_type):
    slow_print(f"\n{endings[ending_type]}")
    input("\n[Press enter to return to the menu]")

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
            
            elif scenario_choice == "b":
                slow_print("\nLibrary scenario is coming soon!")
            
            elif scenario_choice == "c":
                slow_print("\nPub scenario is coming soon!")
            
            elif scenario_choice == "q":
                slow_print("\nGoodbye, see you another time!")
                return
        else:
            slow_print("\nUnavailable option, try again.")

# function university_scenario controls this specific scenario
def university_scenario(name):
    slow_print("\nWelcome to the first day of university!")
    input("\n(press enter)")
    slow_print("\nYou are standing outside a lecture hall. Another student is standing next to you.")
    input("\n(press enter)")
    
    response = retry_dialogue("uni", "q1", "edgar", name)
    
    if response == "b":
        response = retry_dialogue("uni", "q1b", "edgar", name)    

    if response in ("a", "b"):
        response_two = retry_dialogue("uni", "q2", "edgar", name)
        
        if response_two == "a":
            slow_print(f"\n{npc_names['uni']['edgar']}: {closing_dialogues['a']}")
            show_ending("successful")
            return
        
        elif response_two == "b":
            response_three = retry_dialogue("uni", "q3", "edgar", name)
            
            if response_three == "a":
                slow_print(f"\n{npc_names['uni']['edgar']}: {closing_dialogues['a']}")
                show_ending("successful")
                return
            
            elif response_three == "b":
                slow_print(f"\n{npc_names['uni']['edgar']}: {closing_dialogues['b']}")
                show_ending("ok")
                return

            elif response_three == "c":
                show_ending("unsuccessful")
                return

            elif response_three == "q":
                return
        
        elif response_two == "c":
            show_ending("unsuccessful")
            return
        
        elif response_two == "q":
            return

    elif response == "c":
        show_ending("unsuccessful")
        return

    elif response == "q":
        return
