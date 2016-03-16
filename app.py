import os
from flask import Flask, jsonify,request,render_template
import hashlib

app = Flask(__name__)

#Metodo que hace el hash
def convertir(palabra):
    stringEnByte = palabra.encode('utf-8')
    objetoHash = hashlib.sha256(stringEnByte)
    resp = objetoHash.hexdigest()
    return resp

@app.route('/', methods=['GET'])
def metodo1():
    return ('TODO OK')

@app.route('/status', methods=['GET'])
def metodo2():
    data = {'a':1}
    resp = jsonify(data)
    resp.status_code = 201
    return resp

@app.route('/validarFirma', methods=['POST'])
def metodo3():
    Mensaje = request.form['mensaje']
    Code = request.form['hash'].lower().strip()
    codigo = convertir(Mensaje)
    Valido = False
    if Code == codigo:
        Valido = True
    dict = {'mensaje': Mensaje , 'valido':Valido}
    return jsonify(dict)

if __name__ == '__main__':
    port = int(os.environ.get('PORT',5000))
    app.run(host='0.0.0.0', port=port)