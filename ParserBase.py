from abc import ABC, abstractmethod
import time
from pathlib import Path


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

    @abstractmethod
    def EnrichVehicleData(self, vehicle):
        # this function could be implemented in the base class if the keys of vin_number and model is the same in all
        # input files, but since the key differs eg: XML file -> VinNumber while in CSV -> vin_number , so to avoid
        # the typical if else hoard and violating the open close principle I left it to each class to implement its own
        # EnrichVehicleData
        pass
