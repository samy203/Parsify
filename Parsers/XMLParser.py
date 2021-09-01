from ParserBase import  ParserBase
import xmltodict, json
import os


class XMLParser(ParserBase):

    def GetFormatExtension(self):
        return 'xml'

    def GetPathArgsCount(self):
        return 1

    def Parse(self, paths):
        self.GenerateOutputDirectory()

        outputObj = {'file_name': os.path.basename(paths[0])}

        with open(paths[0]) as fd:
            doc = xmltodict.parse(fd.read())
            vics = doc['Insurance']['Transaction']['Customer']['Units']['Auto']['Vehicle']
            doc['Insurance']['Transaction']['Customer'].pop('Units')
            outputObj['transaction'] = doc['Insurance']['Transaction']
            outputObj['transaction']['vehicles'] = vics

            with open(f'output/{self.GetFormatExtension()}/{self.GetTimeStamp()}_{os.path.basename(paths[0])}.json', 'w',encoding='utf-8') as f:
                json.dump(outputObj, f, ensure_ascii=False, indent=4)


