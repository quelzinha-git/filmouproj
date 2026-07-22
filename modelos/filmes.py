from config import db

class Filme(db.Model):
    __tablename__ = 'filmes'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    genero = db.Column(db.String(100), nullable=False)
    ano = db.Column(db.Integer, nullable=False)

    def __init__(self, nome, genero, ano):
        self.nome = nome
        self.genero = genero
        self.ano = ano