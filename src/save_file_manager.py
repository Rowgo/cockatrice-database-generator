import json
import os

class SaveFileManager():

    @staticmethod
    def save(key, value):
        data: dict
        try:
            with open('config.json', 'r') as file:
                data = json.load(file)
        
        except:
            data = {}
                
        data[key] = value

        with open('config.json', 'w') as file:
            json.dump(data, file, indent=4)

    @staticmethod
    def load(key):
        with open('config.json', 'r') as file:
            data = json.load(file)
            return data[key]