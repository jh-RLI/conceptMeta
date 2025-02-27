from pathlib import Path

import xmltodict
from lxml import etree


def parse_metadata(file_path: Path) -> etree._Element:
    parser = etree.XMLParser(ns_clean=True, recover=True, encoding="utf-8")
    with open(file_path, "rb") as f:
        xml_tree = etree.parse(f, parser=parser)
    return xml_tree.getroot()


def parse_xml_to_dict(file_path):
    """
    Reads an XML file, parses it into a Python dictionary, and returns it.

    Args:
        file_path (str): The path to the XML file.

    Returns:
        dict: A Python dictionary representation of the XML content.
    """
    try:
        with open(file_path, "r", encoding="utf-8") as xml_file:
            # Read the XML content
            xml_content = xml_file.read()

        # Parse the XML content to a dictionary
        parsed_dict = xmltodict.parse(xml_content)
        return parsed_dict

    except Exception as e:
        print(f"An error occurred while parsing the XML file: {e}")
        return None
