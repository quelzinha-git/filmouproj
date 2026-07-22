from flask import *
from daos.filme_dao import FilmeDAO

bpadmin = Blueprint('admin', __name__, url_prefix='/admin')

ADMIN_EMAIL = "admin@gmail.com"
ADMIN_SENHA = "123456"


@bpadmin.route('/login', methods=['GET', 'POST'])
def login():

    if request.method == 'POST':

        email = request.form.get('email')
        senha = request.form.get('senha')

        if email == ADMIN_EMAIL and senha == ADMIN_SENHA:
            session['admin'] = True
            return redirect('/admin/filmes')

        return render_template(
            'login_admin.html',
            erro='Email ou senha inválidos.'
        )

    return render_template('login_admin.html')


@bpadmin.route('/logout')
def logout():

    session.pop('admin', None)

    return redirect('/admin/login')


@bpadmin.route('/filmes')
def listar_filmes():

    if 'admin' not in session:
        return redirect('/admin/login')

    filmes = FilmeDAO.listar()

    return render_template(
        'lista_filmes.html',
        filmes=filmes
    )


@bpadmin.route('/adicionar_filme', methods=['GET', 'POST'])
def adicionar_filme():

    if 'admin' not in session:
        return redirect('/admin/login')

    if request.method == 'POST':

        nome = request.form.get('nome')
        genero = request.form.get('genero')
        ano = request.form.get('ano')

        FilmeDAO.salvar(nome, genero, ano)

        return redirect('/admin/filmes')

    return render_template('adicionar_filme.html')


@bpadmin.route('/remover_filme/<int:id>')
def remover_filme(id):

    if 'admin' not in session:
        return redirect('/admin/login')

    FilmeDAO.remover(id)

    return redirect('/admin/filmes')