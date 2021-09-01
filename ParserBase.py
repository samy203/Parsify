from abc import ABC, abstractmethod
import time
from pathlib import Path
import requests


class ParserBase(ABC):

    @abstractmethod
    def GetFormatExtension(self):
        pass

    @abstractmethod
    def Parse(self, paths):
        pass

    @abstractmethod
    def GetPathArgsCount(self):
        pass

    def GetTimeStamp(self):
        return time.time()

    def GenerateOutputDirectory(self):
        base = Path('output')
        base.mkdir(exist_ok=True)

        extBase = Path(f'output/{self.GetFormatExtension()}')
        extBase.mkdir(exist_ok=True)

    def EnrichVehicleData(self, vehicle):
        response = requests.get(f"https://vpic.nhtsa.dot.gov/api/vehicles/DecodeVinValues/{vehicle['VinNumber']}?format=json&modelyear={vehicle['ModelYear']}")
        vehiclesFullData = response.json()['Results'][0]
        vehicle['Model'] = vehiclesFullData['Model']
        vehicle['Manufacturer'] = vehiclesFullData['Manufacturer']
        vehicle['PlantCountry'] = vehiclesFullData['PlantCountry']
        vehicle['VehicleType'] = vehiclesFullData['VehicleType']
        return vehicle
