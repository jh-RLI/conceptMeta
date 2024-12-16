# Collect based on one of the options below (depends on how this can be done in nodeRed)

from pathlib import Path

from lxml import etree

from settings import OUTPUT_PATH


def save_metadata_document(metadata_root: etree.Element, file_name: str):
    """
    Saves the metadata document to a file.

    Args:
        metadata_root (etree.Element): The root element of the metadata XML document.
        file_path (Path): Path where the metadata document should be saved.
    """

    xml_file_name = f"{file_name}.xml"
    path = Path(OUTPUT_PATH / xml_file_name)
    # Ensure the parent directory exists
    path.parent.mkdir(parents=True, exist_ok=True)

    # Write the XML to a file with pretty printing
    with open(path, "wb") as file:
        file.write(
            etree.tostring(
                metadata_root, pretty_print=True, xml_declaration=True, encoding="UTF-8"
            )
        )
