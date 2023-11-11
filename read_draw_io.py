#  Genarated with gpt-4-32k-0613
import xml.etree.ElementTree as ET
import matplotlib.pyplot as plt

def parse_xml(xmlfile):
    tree = ET.parse(xmlfile)
    root = tree.getroot()
    data_dict = {}
    for item in root.findall('./data'): # assuming data are located under the "data" tag
        key = item.get('key')
        value = float(item.get('value'))
        data_dict[key] = value
    return data_dict

def generate_chart(data_dict):
    keys = data_dict.keys()
    values = data_dict.values()

    plt.figure(figsize=(10, 5))
    plt.bar(keys, values)
    plt.xlabel('Keys')
    plt.ylabel('Values')
    plt.title('Diagram data')
    plt.grid(True)
    plt.show()

chart_xml = 'data/diagrams_dot_net_sample.drawio'
data_dict = parse_xml(chart_xml)
generate_chart(data_dict)