from ParserBase import  ParserBase
import xmltodict, json
import csv
import os


class CSVParser(ParserBase):

    def GetFormatExtension(self):
        return 'csv'

    def Parse(self, paths):
        self.GenerateOutputDirectory()

        customersData ={}
        with open(paths[0], encoding='utf-8') as cusFile:
            csvReader = csv.DictReader(cusFile)
            for rows in csvReader:
                key = rows['id']
                customersData[key] = rows

        vehicleData ={}
        with open(paths[1], encoding='utf-8') as vicFile:
            csvReader = csv.DictReader(vicFile)
            for rows in csvReader:
                key = rows['id']
                vehicleData[key] = rows



