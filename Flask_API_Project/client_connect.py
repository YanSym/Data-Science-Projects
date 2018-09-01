###########
# CLIENT
###########

import json
import requests
import socket
import pandas as pd


PORT = "8888"

hostname = socket.gethostname()
CURRENT_IP = socket.gethostbyname(hostname)



header = {'Content-Type': 'application/json', 'Accept': 'application/json'}


data_test = [[1,1],[2,2],[3,3],[4,4],[9,9],[10,10]]

df_test = pd.DataFrame(data_test)


data = df_test.to_json(orient='records')


address_post = "http://" + CURRENT_IP + ":" + PORT + "/predict"
resp = requests.post(address_post, data = json.dumps(data), headers= header)

print (resp)
print (resp.json())

