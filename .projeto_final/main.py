# 24-API simples com Flask - Crie uma API que retorna lista de pacientes em JSON.
from flask import Flask



app = Flask(__name__)

# import projeto_final.route as route
from projeto_final.route import *


if __name__ == '__main__':
    app.run()