'''
This module randomly generates lorem ipsum text with ssn numbers included
'''
import random

from lorem.text import TextLorem
from flask import Flask
from lorem.data import WORDS
from faker import Faker


fake = Faker()


app = Flask(__name__)


@app.route("/")
def random_ssn():
    # Generate a random number of lorem
    words = WORDS + [fake.ssn() for _ in range(random.randint(0, 11))] + [fake.email() for _ in range(random.randint(0, 11))]
    text_generator = TextLorem(words=words)
    return { "text": text_generator.text() }
