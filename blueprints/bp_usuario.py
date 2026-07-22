from flask import *
from modelos.usuario import Usuario
from daos.usuario_dao import UsuarioDAO


bpusuario = Blueprint('usuario', __name__, url_prefix='/usuario')


@bpusuario.route('/')
def inicial():
    return render_template('index.html')


@bpusuario.route('/cadastro', methods=['GET', 'POST'])
def cadastro():

    if request.method == 'POST':

        nome = request.form.get('nome')
        email = request.form.get('emailusuario')
        senha = request.form.get('senhausuario')
        senha2 = request.form.get('senha2')

        if senha == senha2:

            UsuarioDAO.salvar(email=email, senha=senha, nome=nome)


            texto = 'Cadastro realizado com sucesso!'
            return render_template('login.html', msg=texto)

        else:

            texto = 'As senhas não coincidem!'
            return render_template('cadastro.html', msg=texto)

    return render_template('cadastro.html')


@bpusuario.route('/login', methods=['GET', 'POST'])
def login():

    if request.method == 'POST':

        email = request.form.get('email')
        senha = request.form.get('senha')

        usuario = UsuarioDAO.autenticar(email, senha)

        if not usuario:
            texto = 'Email ou senha incorretos!'
            return render_template('login.html', msg=texto)

        session['usuario'] = usuario.email

        return redirect('/usuario/principal')

    return render_template('login.html')

@bpusuario.route('/principal')
def principal():

    if 'usuario' in session:
        return render_template('principal.html')

    return redirect('/usuario/login')



@bpusuario.route('/pesquisar')
def pesquisar():
    nome_busca = request.args.get('nome_filme')

    filmes_todos = [
        ['O Mágico de Oz', 'Fantasia/Musical', 1939,'resumo teste'],
        ['Casablanca', 'Romance/Drama', 1942,'resumo teste'],
        ['O poderoso chefão', 'Policial/Drama', 1972,'resumo teste'],
        ['Guerra nas Estrelas', 'Ficção científica', 1977,'resumo teste'],
        ['E.T.: O Extraterrestre', 'Ficção científica', 1982,'resumo teste'],
        ['De Volta para o Futuro', 'Ficção científica/Comédia', 1985,'resumo teste'],
        ['Jurassic Park: O Parque dos Dinossauros', 'Aventura/Ficção científica', 1993,'resumo teste'],
        ['O Rei Leão', 'Animação/Aventura', 1994,'resumo teste'],
        ['Forrest Gump: O Contador de Histórias', 'Drama/Romance', 1994,'resumo teste'],
        ['Titanic', 'Romance/Drama', 1997,'resumo teste'],
        ['Matrix', 'Ficção científica', 1999,'resumo teste'],
        ['Harry Potter e a Pedra Filosofal', 'Fantasia/Aventura', 2001,'resumo teste'],
        ['O Senhor dos Anéis: A Sociedade do Anel', 'Fantasia/Épico', 2001,'resumo teste'],
        ['Diário de uma Paixão', 'Romance/Drama', 2004,'resumo teste'],
        ['Orgulho e Preconceito', 'Romance/Drama', 2005,'resumo teste'],
        ['Batman: O Cavaleiro das Trevas', 'Ação/Policial', 2008,'resumo teste'],
        ['Avatar', 'Ficção Científica/Ação', 2009,'resumo teste'],
        ['La La Land: Cantando Estações', 'Romance/Musical', 2016,'resumo teste'],
        ['Nasce uma Estrela', 'Romance/Drama', 2018,'resumo teste'],
        ['Vingadores: Ultimato', 'Ação/Super-herói', 2019,'resumo teste']
    ]

    if nome_busca:
        lista_final = []
        for filme in filmes_todos:

            if nome_busca.lower() in filme[0].lower():
                lista_final.append(filme)
        return render_template('pesquisa.html', filmes=lista_final)

    return render_template('pesquisa.html', filmes=filmes_todos)

@bpusuario.route('/avaliacoes')
def avaliacoes():
    return render_template('avaliacoes.html')

@bpusuario.route('/sair')
def sair():

    session.pop('usuario', None)

    return redirect('/usuario/')

@bpusuario.route('/detalharfilme')
def detalhar_filme():

    nome = request.values.get('nome')
    resumo = request.values.get('resumo')
    return render_template('detalharfilme.html', nome=nome, resumo=resumo)