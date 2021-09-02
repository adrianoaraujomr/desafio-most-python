from numpy import frombuffer
from cv2 import imdecode, imencode, IMREAD_COLOR
from flask import Blueprint, request, make_response
from ..utils import remove_white_borders

imagem_blueprint = Blueprint('imagem', __name__)


@imagem_blueprint.route('/reduzir', methods=['POST'])
def reduzir_espaco_branco():
    imagem_bin = request.stream.read()
    imagem = convert_binary_image_to_opencv(imagem_bin)
    imagem_processada = remove_white_borders(imagem)
    imagem_bin = convert_opencv_image_to_binary(imagem_processada)
    response = make_response(imagem_bin)
    response.headers.set('Content-Type', 'image/png')
    return response


def convert_opencv_image_to_binary(imagem):
    retval, buffer = imencode('.png', imagem)
    return buffer.tobytes()


def convert_binary_image_to_opencv(imagem_bin):
    nparray = frombuffer(imagem_bin, dtype='uint8')
    return imdecode(nparray, IMREAD_COLOR)
