import xmltodict
import json

def xml_to_json(xml_string):
    # Parse XML
    dict_data = xmltodict.parse(xml_string)
    
    # Convert to JSON
    json_data = json.dumps(dict_data, indent=4)
    return json_data

# Example XML input
xml_input = """<root>
    <user>
        <name>Deepa</name>
        <location>Auckland, New Zealand</location>
        <skills>
            <skill>Azure</skill>
            <skill>API Engineering</skill>
        </skills>
    </user>
</root>"""

# Convert and print JSON output
json_output = xml_to_json(xml_input)
print(json_output)
