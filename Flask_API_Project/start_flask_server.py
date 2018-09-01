###########
# SERVER
###########

import os
import pandas as pd
from sklearn.externals import joblib
from flask import Flask, jsonify, request
import pickle
import socket
from sklearn.externals import joblib


app = Flask(__name__)

PORT = 8888

hostname = socket.gethostname()
CURRENT_IP = socket.gethostbyname(hostname)


@app.route('/predict', methods=['POST'])
def apicall():

	try:
		test_json = request.get_json()
		test = pd.read_json(test_json, orient='records')


	except Exception as e:
		raise e


	if test.empty:
		return(bad_request())

	else:
		print("Loading the model...")

		clf = joblib.load('classifier.pkl') 

		print("The model has been loaded...doing predictions now...")
		predictions = clf.predict_proba(test)
		
		predictions = [round(value[1],2) for value in predictions] 

		# prediction


		final_predictions = pd.DataFrame(predictions)


		responses = jsonify(predictions=final_predictions.to_json(orient="values"))
		responses.status_code = 200
		
		return (responses)


app.run(host=CURRENT_IP,debug=True,port=PORT)
