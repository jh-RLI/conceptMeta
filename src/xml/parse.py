from pathlib import Path

from lxml import etree


def parse_metadata(file_path: Path) -> etree._Element:
    parser = etree.XMLParser(ns_clean=True, recover=True, encoding="utf-8")
    with open(file_path, "rb") as f:
        xml_tree = etree.parse(f, parser=parser)
    return xml_tree.getroot()
