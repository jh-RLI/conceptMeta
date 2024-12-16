# Collect based on one of the options below (depends on how this can be done in nodeRed)

from pathlib import Path

from lxml import etree


def save_metadata_document(metadata_root: etree.Element, file_path: Path):
    """
    Saves the metadata document to a file.

    Args:
        metadata_root (etree.Element): The root element of the metadata XML document.
        file_path (Path): Path where the metadata document should be saved.
    """
    # Ensure the parent directory exists
    file_path.parent.mkdir(parents=True, exist_ok=True)

    # Write the XML to a file with pretty printing
    with open(file_path, "wb") as file:
        file.write(
            etree.tostring(
                metadata_root, pretty_print=True, xml_declaration=True, encoding="UTF-8"
            )
        )
