#!/usr/bin/python3
"""
Simple XML Serialization and Deserialization
"""
import xml.etree.ElementTree as ET


def serialize_to_xml(data, filename):
    root = ET.Element("data")
    for key, value in data.items():
        ET.SubElement(root, key).text = str(value)
    ET.ElementTree(root).write(filename, encoding="utf-8",
                               xml_declaration=True)


def deserialize_from_xml(filename):
    try:
        tree = ET.parse(filename)
        return {child.tag: child.text for child in tree.getroot()}
    except FileNotFoundError:
        print("Error: File not found.")
        return None
