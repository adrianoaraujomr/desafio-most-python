from flask import Blueprint

imagem_blueprint = Blueprint('imagem', __name__)


@imagem_blueprint.route('/reduzir', method=['POST'])
def reduzir_espaco_branco():
    return 'reduzir_epaco_branco works'
