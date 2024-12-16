# This module implements methods to extract specific information
# form a INSPIRE metadata document
from abc import ABC, abstractmethod
from xml.namespaces import namespaces

from lxml import etree


class MetadataExtractor(ABC):
    @abstractmethod
    def extract(self, xml_tree: etree._Element) -> str:
        """Extracts a specific value from the given XML tree."""
        pass


class TitleExtractor(MetadataExtractor):
    def extract(self, xml_tree: etree._Element) -> str:
        title = xml_tree.find(".//gmd:title/gco:CharacterString", namespaces=namespaces)
        return title.text if title is not None else "Title not found"


class AbstractExtractor(MetadataExtractor):
    def extract(self, xml_tree: etree._Element) -> str:
        abstract = xml_tree.find(
            ".//gmd:abstract/gco:CharacterString", namespaces=namespaces
        )
        return abstract.text if abstract is not None else "Abstract not found"


class DistributionVersionExtractor(MetadataExtractor):
    def extract(self, xml_tree: etree._Element) -> str:
        version = xml_tree.find(
            ".//gmd:distributionFormat/gmd:MD_Format/gmd:version/gco:CharacterString",
            namespaces=namespaces,
        )
        return version.text if version is not None else "Version not found"


class MetadataExtractorContext:
    def __init__(self, strategy: MetadataExtractor):
        self.strategy = strategy

    def set_strategy(self, strategy: MetadataExtractor):
        """Allows changing the strategy at runtime."""
        self.strategy = strategy

    def extract(self, xml_tree: etree._Element) -> str:
        return self.strategy.extract(xml_tree)
