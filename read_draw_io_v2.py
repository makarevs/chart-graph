import xml.etree.ElementTree as ET
import networkx as nx
from pyvis.network import Network
import matplotlib.pyplot as plt

def parse_xml(xmlfile):
    # Parse XML
    tree = ET.fromstring(xmlfile)
    root = tree.find('.//root')

    # Construct NetworkX graph
    graph = nx.DiGraph()

    # Add nodes to graph
    for node in root.findall("mxCell[@vertex='1']"):
        if node.get("value"):   # if node name exists
            node_name = node.get("value")
            node_name = node_name.replace("&amp;nbsp;&lt;div&gt;", '').replace('&lt;p&gt;','').replace('&lt;/p&gt;','').replace('&lt;/div&gt;','')   # Cleanup node name
            node_id = node.get("id")
            graph.add_node(node_id, name=node_name)

    # Add edges to graph
    for edge in root.findall("mxCell[@edge='1']"):
        if edge.get("source") and edge.get("target"):   # if edge exists
            source_id = edge.get("source")
            target_id = edge.get("target")
            edge_label = edge.get("value")
            graph.add_edge(source_id, target_id, label=edge_label)

    return graph

def visualize_graph(graph):
    net = Network()
    for node in graph.nodes(data=True):
        # Add each node to the PyVis graph
        net.add_node(node[0], label=node[1]['name'])

    for edge in graph.edges(data=True):
        # Add each edge to the PyVis graph
        net.add_edge(edge[0], edge[1], label=edge[2]['label'])

    # Generate visualization in PyVis
    net.show("example.html")
    # nx.draw(net)
    # plt.show()

def read_xml_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()

chart_xml = 'data/diagrams_dot_net_sample.drawio'
xml_string = read_xml_file(chart_xml)  # replace with the path to your XML file

graph = parse_xml(xml_string)  # Replace <your_xml_String> with your XML string
visualize_graph(graph)

print("The end!")