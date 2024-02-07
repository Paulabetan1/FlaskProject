from db import db

class Joke(db.Model):
    joke_id = db.Column(db.Integer, primary_key = True)
    jokeName = db.Column(db.String(250))
    textJoke = db.Column(db.String(250))

    def __str__(self):
        return(
            f'joke_id: {self.joke_id}, '
            f'jokeName: {self.jokeName}, '
            f'textJoke: {self.textJoke}, '
        )