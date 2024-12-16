# Collect metadata stem from all ETL-processes and create
# dataset-series metadata document
# ISSUE: How to create the dataset series metadata
# ... link all datasets individually
# or use a format different from INSPIRE ??

from xml.namespaces import namespaces

from lxml import etree


def create_inspire_metadata_document(
    process_id: str, metadata_info: dict
) -> etree.Element:
    """
    Creates an INSPIRE metadata XML document using lxml.

    Args:
        process_id (str): The ID of the ETL process.
        metadata_info (dict): Dictionary containing metadata information.

    Returns:
        etree.Element: The root element of the XML tree for the metadata document.
    """

    # Create root element
    root = etree.Element(
        "{http://www.isotc211.org/2005/gmd}MD_Metadata", nsmap=namespaces
    )

    # Add file identifier
    file_id = etree.SubElement(root, "{http://www.isotc211.org/2005/gmd}fileIdentifier")
    file_id_text = etree.SubElement(
        file_id, "{http://www.isotc211.org/2005/gco}CharacterString"
    )
    file_id_text.text = process_id

    # Add dataset title
    title = etree.SubElement(root, "{http://www.isotc211.org/2005/gmd}title")
    title_text = etree.SubElement(
        title, "{http://www.isotc211.org/2005/gco}CharacterString"
    )
    title_text.text = metadata_info["dataset_name"]

    # Add metadata storage path
    storage_path = etree.SubElement(
        root, "{http://www.isotc211.org/2005/gmd}metadataStoragePath"
    )
    storage_path_text = etree.SubElement(
        storage_path, "{http://www.isotc211.org/2005/gco}CharacterString"
    )
    storage_path_text.text = metadata_info["metadata_storage_path"]

    # Add additional elements here based on INSPIRE requirements
    # Example: Add language
    language = etree.SubElement(root, "{http://www.isotc211.org/2005/gmd}language")
    language_text = etree.SubElement(
        language, "{http://www.isotc211.org/2005/gco}CharacterString"
    )
    language_text.text = "eng"  # Assuming English; update as necessary

    return root
