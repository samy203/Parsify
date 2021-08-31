from abc import ABC, abstractmethod


class ParserBase(ABC):

    @abstractmethod
    def GetFormat(self):
        pass

    @abstractmethod
    def Parse(self, path):
        pass



