# code for checking successful deployment to ibm cloud

import requests

import json

# NOTE: you must manually set API_KEY below using information retrieved from your IBM Cloud account.
API_KEY = "T75XQkw5mNPkD-wVnMryQDBzmUgFQnVUdNm7JHxHrfd2"
token_response = requests.post('https://iam.cloud.ibm.com/identity/token', data={"apikey":
 API_KEY, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'})
mltoken = token_response.json()["access_token"]

header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}

# NOTE: manually define and pass the array(s) of values to be scored in the next line
#payload_scoring = {"input_data": [{"fields": [array_of_input_fields], "values": [array_of_values_to_be_scored, another_array_of_values_to_be_scored]}]}

payload_scoring = {"input_data": [{"field": [[ "Store", "Dept", "Size", "IsHoliday", "CPI", "Temperature","Type_B","Type_C","MarkDown4","month","Year"]], "values": [[22.02, 44.21, 137424.93, 1, 167.45, 35.57, 0.5, 1, 0, 2, 2010]]}]}



response_scoring = requests.post('https://us-south.ml.cloud.ibm.com/ml/v4/deployments/4a25eff4-14fd-4175-9371-43622968b7e5/predictions?version=2022-06-19', json=payload_scoring,
 headers={'Authorization': 'Bearer ' + mltoken})
print("Scoring response")
predictions=response_scoring.json()
output=predictions['predictions'][0]['values'][0][0]
print(output)
