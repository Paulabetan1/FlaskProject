from db import db

class Joke(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    nombreChiste = db.Column(db.String(250))
    textoChiste = db.Column(db.String(250))

    def __str__(self):
        return(
            f'id: {self.id}, '
            f'nombreChiste: {self.nombreChiste}, '
            f'textoChiste: {self.textoChiste}, '
        )