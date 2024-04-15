import requests

url = 'https://www.carboninterface.com/api'
headers = {'Authorization': 'Bearer Q6eGoxxENeS3vpIoXkKOw'}


""" toyota = "2b1d0cd5-59be-4010-83b3-b60c5e5342da"

all_vehicle_makes = [] """


class CarbonAPI:
    def __init__(self):
        req = requests.get(url + "/v1/auth", headers=headers)
        reqJson = req.json()
        ## If 404, throw error
        if (req.status_code == 404):
            print("Error: 404")
        else:
            print("API is working")
            print(reqJson)

    def allVehicleMakes(self):
        req = requests.get(url + "/v1/vehicle_makes", headers=headers)
        #print(req.json())
        return req.json()
    
    def getVehicleMake(self, id):
        if (id == None):
            print("ID is required")

        req = requests.get(url + "/v1/vehicle_makes/" + id + "/vehicle_models", headers=headers)
            ### Push all vehicle makes names to all_vehicle_makes

        return req.json()
