"""
This is a tool to read INSPIRE metadata XML documents and
integrate them into the Berlin Wärmekataster data pipeline
to manage metadata, data to support different data versions.
"""

from inspire.extractInspireInfoStrategy import (
    AbstractExtractor,
    DistributionVersionExtractor,
    MetadataExtractorContext,
    TitleExtractor,
)
from inspire.interface import register_etl_processes_and_create_metadata
from inspire.xmlWrap.parse import parse_metadata
from metaRegister.manageEtlInputDatasetsMetadata import (
    collect_metadata_path_for_etl_processes,
)


def main():
    print("Hello from conceptmeta!")

    staged_for_run = collect_metadata_path_for_etl_processes()

    for i in staged_for_run:
        print(f"Processing ETL process {i[0]}")
        # Parse the metadata document
        xml_root = parse_metadata(i[1])

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

        # TODO: Check if xml to dict might ease processing
        # TODO: Check if dict to xml is stable
        # parse_xml_to_dict(i[1])

    register_etl_processes_and_create_metadata()


if __name__ == "__main__":
    main()
