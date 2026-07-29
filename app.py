from flask import *
from blueprints.bp_admin import bpadmin
from blueprints.bp_usuario import bpusuario
from config import db
import os

app = Flask(__name__)
app.secret_key = 'KJ#H4k3jh412dasd'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///meubanco.db'
db.init_app(app)

with app.app_context():
    db.create_all()

    from modelos.filmes import Filme

    if Filme.query.count() == 0:
        filmes = [
            ['O Mágico de Oz', 'Fantasia/Musical', 1939],
            ['Casablanca', 'Romance/Drama', 1942],
            ['O Poderoso Chefão', 'Policial/Drama', 1972],
            ['Guerra nas Estrelas', 'Ficção Científica', 1977],
            ['E.T.: O Extraterrestre', 'Ficção Científica', 1982],
            ['De Volta para o Futuro', 'Ficção Científica/Comédia', 1985],
            ['Jurassic Park: O Parque dos Dinossauros', 'Aventura/Ficção Científica', 1993],
            ['O Rei Leão', 'Animação/Aventura', 1994],
            ['Forrest Gump: O Contador de Histórias', 'Drama/Romance', 1994],
            ['Titanic', 'Romance/Drama', 1997],
            ['Matrix', 'Ficção Científica', 1999],
            ['Harry Potter e a Pedra Filosofal', 'Fantasia/Aventura', 2001],
            ['O Senhor dos Anéis: A Sociedade do Anel', 'Fantasia/Épico', 2001],
            ['Diário de uma Paixão', 'Romance/Drama', 2004],
            ['Orgulho e Preconceito', 'Romance/Drama', 2005],
            ['Batman: O Cavaleiro das Trevas', 'Ação/Policial', 2008],
            ['Avatar', 'Ficção Científica/Ação', 2009],
            ['La La Land: Cantando Estações', 'Romance/Musical', 2016],
            ['Nasce uma Estrela', 'Romance/Drama', 2018],
            ['Vingadores: Ultimato', 'Ação/Super-herói', 2019]
        ]

        for nome, genero, ano in filmes:
            db.session.add(Filme(nome, genero, ano))

        db.session.commit()
        print("Quantidade de filmes:", Filme.query.count())

app.register_blueprint(bpadmin)
app.register_blueprint(bpusuario)


@app.route('/')
def inicial():
    return render_template('index.html')


app.run(debug=True, host='0.0.0.0', port=5007)