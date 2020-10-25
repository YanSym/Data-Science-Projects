import os
import pandas as pd
import joblib
from flask import Flask, jsonify, request
import pickle
import socket
import time

app = Flask(__name__)
PORT = 8888
hostname = socket.gethostname()
CURRENT_IP = socket.gethostbyname(hostname)

# rota de escoragem
@app.route('/predict', methods=['POST'])
def apicall():

    try:
        test_json = request.get_json()
        df_test = pd.read_json(test_json, orient='records')

    except Exception as e:
        raise e

    if df_test.empty:
        return(bad_request())

    else:
        start_time = time.time()
        clf = joblib.load('clf_ligacao.pkl')
        print ('*'*40)
        print ('Iniciando escoragem de {} observações...'.format(len(df_test)))
        predictions = [round(value,6) for value in clf.predict(df_test)]
        responses = jsonify(predictions=pd.DataFrame(predictions).to_json(orient="values"))
        delta_time = round((time.time() - start_time),2)
        print ('Escoragem finalizada...')
        print ('Tempo de execução (segundos): {}'.format(delta_time))
        print ('*'*40)
        responses.status_code = 200
        return (responses)
    
@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

# inicializa servidor
app.run(host=CURRENT_IP, debug=True, port=PORT)