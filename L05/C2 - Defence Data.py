#
# Generate a valid xml file at /tmp/vulnerable-countries.xml.
# It should contain a list of country nodes attached to a root node.
# Each country node should have a name attribute.
# The third node name should be Panama.
#

from xml.dom import minidom
import os 
  
root = minidom.Document()
  
xml = root.createElement('root') 
root.appendChild(xml)

def add_country(name):
	productChild = root.createElement('country')
	productChild.setAttribute('name', name)
	xml.appendChild(productChild)

add_country("USA")
add_country("China")
add_country("Panama")
  
xml_str = root.toprettyxml(indent ="\t") 
  
save_path_file = "/tmp/vulnerable-countries.xml"
  
with open(save_path_file, "w") as f:
    f.write(xml_str)
