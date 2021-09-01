from ParserBase import ParserBase
import json
import csv
import os
import requests

class CSVParser(ParserBase):

    def GetFormatExtension(self):
        return 'csv'

    def GetPathArgsCount(self):
        return 2

    def EnrichVehicleData(self, vehicle):
        # the
        response = requests.get(f"https://vpic.nhtsa.dot.gov/api/vehicles/DecodeVinValues/{vehicle['vin_number']}?format=json&modelyear={vehicle['model_year']}")
        vehiclesFullData = response.json()['Results'][0]
        vehicle['Model'] = vehiclesFullData['Model']
        vehicle['Manufacturer'] = vehiclesFullData['Manufacturer']
        vehicle['PlantCountry'] = vehiclesFullData['PlantCountry']
        vehicle['VehicleType'] = vehiclesFullData['VehicleType']
        return vehicle

    def Parse(self, paths):
        self.GenerateOutputDirectory()

        outputObj = {'file_name': os.path.basename(paths[0])}
        # the csv file contained multiple persons compared to xml files, this is why im converting dict['transaction']
        # from {} to [] , and there is 2 input files, so im changed how the output file is named accordingly

        outputObj = {'file_name': f'{os.path.basename(paths[0])}-{os.path.basename(paths[1])}', 'transaction': []}

        vehicleData = []
        with open(paths[1], encoding='utf-8') as vicFile:
            csvReader = csv.DictReader(vicFile)
            for rows in csvReader:
                vehicleData.append(rows)

        with open(paths[0], encoding='utf-8') as cusFile:
            csvReader = csv.DictReader(cusFile)
            for rows in csvReader:
                transObj = {'date': rows['date']}
                rows.pop('date')
                transObj['customer'] = rows
                transObj['vehicles'] = []

                for vehicle in vehicleData:
                    if vehicle['owner_id'] == rows['id']:
                        # cant pop the owner_id , cuz it will get iterated on later, this part could be optmized later by removing cars that already have owner once assigning
                        # to the transObj['vehicles']
                        shallowCopyVehicle = vehicle.copy()
                        shallowCopyVehicle.pop('owner_id')
                        self.EnrichVehicleData(shallowCopyVehicle)
                        transObj['vehicles'].append(shallowCopyVehicle)

                outputObj['transaction'].append(transObj)

        with open(
                f'output/{self.GetFormatExtension()}/{self.GetTimeStamp()}_{os.path.basename(paths[0])}-{os.path.basename(paths[1])}.json',
                'w',
                encoding='utf-8') as f:
            json.dump(outputObj, f, ensure_ascii=False, indent=4)
