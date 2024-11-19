from models.cuidador import Cuidador
from models.perro import Perro

user_blueprint = Blueprint('user_bp', __name__, url_prefix="/users")

@user_blueprint.route('/')
def index():
    perros = Perro.query.all()
    return render_template('index.html', perros=perros)

@user_blueprint.route('/update')
def update():
    return "Ruta para actualizar perros"