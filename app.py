from flask import *
from blueprints.bp_admin import bpadmin
from blueprints.bp_usuario import bpusuario
from config import db

app = Flask(__name__)
app.secret_key = 'KJ#H4k3jh412dasd'


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///meubanco.db'
db.init_app(app)

with app.app_context():
    db.create_all()

app.register_blueprint(bpadmin)
app.register_blueprint(bpusuario)


@app.route('/')
def inicial():
    return render_template('index.html')


app.run(debug=True, host='0.0.0.0', port=5007)