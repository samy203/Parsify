from ParserBase import ParserBase
import xmltodict
import json
import os
import requests
from pymongo import MongoClient


class XMLParser(ParserBase):

    def GetFormatExtension(self):
        return 'xml'

    def GetPathArgsCount(self):
        return 1

    def EnrichVehicleData(self, vehicle):
        response = requests.get(
            f"https://vpic.nhtsa.dot.gov/api/vehicles/DecodeVinValues/{vehicle['VinNumber']}?format=json&modelyear={vehicle['ModelYear']}")
        vehiclesFullData = response.json()['Results'][0]
        vehicle['Model'] = vehiclesFullData['Model']
        vehicle['Manufacturer'] = vehiclesFullData['Manufacturer']
        vehicle['PlantCountry'] = vehiclesFullData['PlantCountry']
        vehicle['VehicleType'] = vehiclesFullData['VehicleType']
        return vehicle

    def Parse(self, paths, output):
        self.GenerateOutputDirectory()

        outputObj = {'file_name': os.path.basename(paths[0])}

        # reading the file and rearranging data
        with open(paths[0]) as fd:
            doc = xmltodict.parse(fd.read())
            vehicles = doc['Insurance']['Transaction']['Customer']['Units']['Auto']['Vehicle']
            for v in vehicles:
                self.EnrichVehicleData(v)
            doc['Insurance']['Transaction']['Customer'].pop('Units')
            outputObj['transaction'] = doc['Insurance']['Transaction']
            outputObj['transaction']['vehicles'] = vehicles

        if output == 'json':
            with open(f'output/{self.GetFormatExtension()}/{self.GetTimeStamp()}_{os.path.basename(paths[0])}.json',
                      'w', encoding='utf-8') as f:
                json.dump(outputObj, f, ensure_ascii=False, indent=4)
        elif output == 'db':
            client = MongoClient('localhost', 27017)
            db = client.trufla_staging
            collection = db.xml
            collection.insert(outputObj)
