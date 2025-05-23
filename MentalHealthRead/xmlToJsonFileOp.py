import xmltodict
import json

def xml_json_file(xml_file_path, json_file_path):
    with open(xml_file_path, "r") as xml_file:
        xml_content = xml_file.read()

        parsed_data = xmltodict.parse(xml_content)
        json_data = json.dumps(parsed_data, indent=4)

    with open(json_file_path, "+w") as json_file:
        json_file.write(json_data)

# xml_json_file(xml_file_path="sample.xml", json_file_path="sample.json")

# Input XML is from World Health Statistics data visualizations dashboard > SDG Target 3.c | Health workforce - https://apps.who.int/gho/data/node.sdg.3-c-data?lang=en
# Online xml validator is used to capture special characters, missing tags etc., as the file size is large https://www.xmlvalidation.com/ 
# As teh char '&' was troublesome for dictionary, it has been replaced by 'and' in the xml file
xml_json_file(xml_file_path="healthcare_workforce.xml", json_file_path="healthcare_workforce.json")
    