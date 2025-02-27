# Collect metadata stem from all ETL-processes and create
# dataset-series metadata document
# ISSUE: How to create the dataset series metadata
# ... link all datasets individually
# or use a format different from INSPIRE ??

# from datetime import datetime

from lxml import etree

from inspire.xmlWrap.namespaces import namespaces


def create_root_element() -> etree.Element:
    """
    Creates the root element for the INSPIRE metadata document.

    Returns:
        etree.Element: The root element.
    """
    return etree.Element(
        "{http://www.isotc211.org/2005/srv}SV_ServiceIdentification",
        nsmap=namespaces,
        attrib=None,
    )


def add_basic_metadata(root: etree.Element, metadata_info: dict) -> None:
    """
    Adds basic metadata fields to the root element.

    Args:
        root (etree.Element): The root element of the XML document.
        metadata_info (dict): Dictionary containing metadata properties.
    """
    # Add fileIdentifier
    # file_id = etree.SubElement(
    #     root,
    #     "{http://www.isotc211.org/2005/gmd}fileIdentifier",
    #     nsmap=namespaces,
    #     attrib=None,
    # )
    # file_id_text = etree.SubElement(
    #     file_id,
    #     "{http://www.isotc211.org/2005/gco}CharacterString",
    #     nsmap=namespaces,
    #     attrib=None,
    # )
    # file_id_text.text = metadata_info.get("fileIdentifier", "UNKNOWN")


def add_identification_info(root: etree.Element, metadata_info: dict) -> None:
    """
    Adds identification information to the metadata document.

    Args:
        root (etree.Element): The root element of the XML document.
        metadata_info (dict): Dictionary containing metadata properties.
    """
    identification_info = etree.SubElement(
        root,
        "{http://www.isotc211.org/2005/gmd}identificationInfo",
        nsmap=namespaces,
        attrib=None,
    )

    data_identification = etree.SubElement(
        identification_info,
        "{http://www.isotc211.org/2005/srv}SV_ServiceIdentification",
        nsmap=namespaces,
        attrib=None,
    )

    citation = etree.SubElement(
        data_identification,
        "{http://www.isotc211.org/2005/gmd}citation",
        nsmap=namespaces,
        attrib=None,
    )

    citation_sub = etree.SubElement(
        citation,
        "{http://www.isotc211.org/2005/gmd}CI_Citation",
        nsmap=namespaces,
        attrib=None,
    )

    # Title
    # srv:SV_ServiceIdentification/gmd:citation/gmd:CI_Citation/gmd:title
    title = etree.SubElement(
        citation_sub,
        "{http://www.isotc211.org/2005/gmd}title",
        nsmap=namespaces,
        attrib=None,
    )
    title_text = etree.SubElement(
        title,
        "{http://www.isotc211.org/2005/gco}CharacterString",
        nsmap=namespaces,
        attrib=None,
    )
    title_text.text = metadata_info.get("title", "Dataset Title")


def create_inspire_metadata_document(
    process_id: str, metadata_info: dict
) -> etree.ElementTree:
    """
    Creates an INSPIRE-compliant metadata XML document.

    Args:
        metadata_info (dict): Dictionary containing required metadata properties.

    Returns:
        etree.ElementTree: XML tree for the INSPIRE metadata document.
    """
    metadata_info = metadata_info["new_inspire_metadata"]
    # Create root element
    root = create_root_element()

    # Add basic metadata
    add_basic_metadata(root, metadata_info)

    return etree.ElementTree(root)


# # Example usage
# metadata_info_example = {
#     "fileIdentifier": "dataset-series-id",
#     "title": "Example Dataset Title",
#     "abstract": "This is an example abstract for a dataset.",
#     "keywords": ["keyword1", "keyword2", "keyword3"],
#     "language": "eng",
#     "bbox": {
#         "west": -10.0,
#         "east": 10.0,
#         "south": -5.0,
#         "north": 5.0,
#     },
# }

# metadata_tree = create_inspire_metadata_document(metadata_info_example)
# metadata_tree.write(
#     "inspire_metadata.xml", pretty_print=True, xml_declaration=True, encoding="UTF-8"
# )
