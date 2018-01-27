"""
@project PalavrasHttpEndpoint
@since 02/08/2017
@author Alencar Rodrigo Hentges <alencarhentges@gmail.com>

"""

import json
from flask import Flask
from flask import request
from utils.FraseUtil import FraseUtil
from utils import StringUtil

app = Flask(__name__)

@app.route('/palavras/analisar/',  methods=['GET'])
def analisarFrase():
    paramFrase = request.args.get('frase')

    if StringUtil.isEmpty(paramFrase):
        error = "A frase a ser analisada de ser passada via parâmetro(?frase={sua_frase})."
        return json.dumps({"error": error}), 400

    frase = FraseUtil.getFrase(paramFrase)
    return json.dumps(frase.palavras)