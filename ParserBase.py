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

    def GetTimeStamp(self):
        return time.time()

    def GenerateOutputDirectory(self):
        base = Path('output')
        base.mkdir(exist_ok=True)

        extBase = Path(f'output/{self.GetFormatExtension()}')
        extBase.mkdir(exist_ok=True)



