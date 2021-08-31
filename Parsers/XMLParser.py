from ParserBase import  ParserBase
import xmltodict, json
import os


class XMLParser(ParserBase):

    def GetFormatExtension(self):
        return 'xml'

    def Parse(self, paths):
        self.GenerateOutputDirectory()
        with open(paths[0]) as fd:
            doc = xmltodict.parse(fd.read())
            doc['file_name'] = os.path.basename(paths[0])
            with open(f'output/{self.GetFormatExtension()}/{self.GetTimeStamp()}_{os.path.basename(paths[0])}.json', 'w', encoding='utf-8') as f:
                json.dump(doc, f, ensure_ascii=False, indent=4)


