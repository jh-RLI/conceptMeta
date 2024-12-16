"""
This is a tool to read INSPIRE metadata XML documents and
integrate them into the Berlin Wärmekataster data pipeline
to manage metadata, data to support different data versions.
"""

from xml.parse import parse_metadata

from extractInspireInfoStrategy import (
    AbstractExtractor,
    DistributionVersionExtractor,
    MetadataExtractorContext,
    TitleExtractor,
)
from settings import META_FILE_PATH


def main():
    print("Hello from conceptmeta!")

    # Parse the metadata document
    xml_root = parse_metadata(META_FILE_PATH)

    # Extract Title
    title_extractor = TitleExtractor()
    context = MetadataExtractorContext(title_extractor)
    print("Title:", context.extract(xml_root))

    # Extract Abstract
    abstract_extractor = AbstractExtractor()
    context.set_strategy(abstract_extractor)
    print("Abstract:", context.extract(xml_root))

    # Extract Distribution Version
    version_extractor = DistributionVersionExtractor()
    context.set_strategy(version_extractor)
    print("Distribution Version:", context.extract(xml_root))


if __name__ == "__main__":
    main()
