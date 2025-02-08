
import requests

# Your API key
API_KEY = "M6951BMW3N07Q1TMFYH1JK31EM"

# API URL
url = "https://api.climatiq.io/data/v1/estimate"

# Headers
headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

# Payload (data to send)
payload = {
    "emission_factor": {
        "activity_id": "electricity-supply_grid-source_residual_mix",
        "data_version": "^6"
    },
    "parameters": {
        "energy": 4200,
        "energy_unit": "kWh"
    }
}

# Sending the request
response = requests.post(url, headers=headers, json=payload)

# Print the response
print(response.status_code)  # Should be 200 if successful
print(response.json())  # Print the response JSON

