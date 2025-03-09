import random

def get_user_input(word_type):
    return input(f"Enter a {word_type}: ")

def generate_story():
    templates = [
        "Today I went to the {place}. There I saw a {adjective} {animal} {verb} on a {noun}.",
        "My best friend is {name}. We love to {verb} together while eating {food}.",
        "In the land of {place}, a {adjective} dragon {verb} over a {noun} and scared the {animal}.",
        "Yesterday, I found a {adjective} {animal} in my {place}. It was trying to {verb} my {food}.",
        "The {adjective} wizard from {place} used his magic to turn a {animal} into a {noun}.",
        "Once upon a time, {name} discovered a {adjective} portal in the {place}. It led to a world full of {animal}s that loved to {verb}."
    ]
    
    story_template = random.choice(templates)
    placeholders = {"place", "adjective", "animal", "verb", "noun", "name", "food"}
    user_inputs = {key: get_user_input(key) for key in placeholders}
    
    story = story_template.format(**user_inputs)
    print("\nYour Mad Libs Story:")
    print(story)

if __name__ == "__main__":
    generate_story()
