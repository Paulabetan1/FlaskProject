import requests
import json
from functools import reduce
import random
import os
from flask import abort

def get_joke(url: str):
    """Returns:
    status_code, text (tuple)"""
    response = requests.get(url)
    if response.status_code == 200:
        return json.loads(response.text)

class Mathmcm():
    def __init__(self, numbers):
        self.numbers= numbers

    def get(self):
        if "," in self.numbers:
            numbers = map(int, self.numbers.split(","))
        else:
            numbers = [int(self.numbers)]

        resultmcm = str(mcm_for(numbers))

        return resultmcm

def mcm(a, b):
    a = int(a)
    b = int(b)

    if a > b:
        greaterThan = a
    else:
        greaterThan = b

    while True:
        if greaterThan % a == 0 and greaterThan % b == 0:
            mcm = greaterThan
            break
        greaterThan += 1

    return mcm

def mcm_for(listNumbers):
    return reduce(lambda x, y: mcm(x, y), listNumbers)

class GetJokes():

    def __init__(self, option):
        self.jokes = []
        self.option = option

    def all_jokes(self):
        self.get_values_joke()
        match self.option:
            case 'chuck':
                return self.jokes[0]
            case 'dad':
                return self.jokes[1]
            case _:
                joke_random = random.choice(self.jokes)
                return joke_random
    
    def get_values_joke(self):
        joke = get_joke(os.environ.get('ENDPOINT_CHUCK'))
        chuck_joke = joke.get('value')
        joke = get_joke(os.environ.get('ENDPOINT_DAD'))
        dad_joke = joke['attachments'][0]['text']
        self.jokes.extend([chuck_joke, dad_joke])

def template(status, data, message ):
    response = {
        'status': status,
        'data': data,
        'message': message
        }
    return response
            

