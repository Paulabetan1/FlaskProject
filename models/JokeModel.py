from db import db

class Joke(db.Model):
    joke_id = db.Column(db.Integer, primary_key = True)
    joke_name = db.Column(db.String(250))
    text_joke = db.Column(db.String(250))

    def __str__(self):
        return(
            f'joke_id: {self.joke_id}, '
            f'joke_name: {self.joke_name}, '
            f'text_joke: {self.text_joke}, '
        )