from flask import Flask
from .views import imagem_blueprint

app = Flask(__name__)
app.config.from_object('config')
app.register_blueprint(imagem_blueprint)
