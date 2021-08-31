from abc import ABC, abstractmethod
import time

class ParserBase(ABC):

    @abstractmethod
    def GetFormatExtension(self):
        pass

    @abstractmethod
    def Parse(self, paths):
        pass

    def GetTimeStamp(self):
        return time.time()


