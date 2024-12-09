import json
import random


def get_random_prompt():
    with open('prompt.json', 'r') as file:
        data = json.load(file)
    return random.choice(data)
