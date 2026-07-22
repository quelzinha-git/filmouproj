from modelos.filmes import Filme
from config import db

class FilmeDAO:

    @staticmethod
    def salvar(nome, genero, ano):

        filme = Filme(nome, genero, ano)

        db.session.add(filme)
        db.session.commit()

        return filme

    @staticmethod
    def listar():

        return Filme.query.all()

    @staticmethod
    def remover(id):

        filme = Filme.query.get(id)

        if filme:

            db.session.delete(filme)
            db.session.commit()