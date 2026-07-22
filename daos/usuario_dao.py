from modelos.usuario import Usuario
from config import db

class UsuarioDAO:
    @staticmethod
    def salvar(nome, email, senha):
        usuario = Usuario(nome, email, senha)

        db.session.add(usuario)
        db.session.commit()

        return usuario

    @staticmethod
    def buscar_por_email(email):
        return Usuario.query.filter_by(email=email).first()

    @staticmethod
    def autenticar(email, senha):
        return Usuario.query.filter_by(email=email, senha=senha).first()
