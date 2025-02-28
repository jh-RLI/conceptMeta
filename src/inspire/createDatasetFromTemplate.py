import json

from lxml import etree

from inspire.xmlWrap import namespaces as NS
from settings import INSPIRE_KEY_SIMPLIFICATION_MAPPING_FILE_PATH, INSPIRE_TEMPLATES_DIR

# Construct the path to the XML template file
xml_file_path = INSPIRE_TEMPLATES_DIR / "inspire-dataset.xml"
# Load XML file
DATASET_TEMPLATE = etree.parse(xml_file_path)

# def create_dataset_from_template(config: dict, template=DATASET_TEMPLATE):
#     """
#     Create a new dataset from the INSPIRE template.
#     """
#     if not config:
#         raise ValueError("Configuration is required")

#     # Get the root element
#     root = template.getroot()

#     # Find the specific section
#     section = root.find(".//TargetSection")

#     if section is not None:
#         # Create new element
#         new_element = etree.Element("NewElement")
#         new_element.text = "New Value"

#         # Append new element
#         section.append(new_element)

#         # # Save the modified XML
#         # root.write(
#         #     f"dataset_{config.get('dataset_name')}.xml",
#         #     encoding="utf-8",
#         #     xml_declaration=True,
#         #     pretty_print=True,
#         # )
#         return etree.ElementTree(root)
#     else:
#         print("Target section not found")

# Define the namespaces used in the XML template
# NS = {
#     "gmd": "http://www.isotc211.org/2005/gmd",
#     "gco": "http://www.isotc211.org/2005/gco",
#     "gmx": "http://www.isotc211.org/2005/gmx",
#     "gml": "http://www.opengis.net/gml/3.2",
#     "xlink": "http://www.w3.org/1999/xlink",
# }


def create_dataset_from_template(
    process_id: str, config: dict, template=DATASET_TEMPLATE
):
    """
    Create a new INSPIRE metadata document by updating the template
    with values from config.

    The template is expected to have placeholder elements
    (indicated by <!-- add value -->)for the following keys:

      - fileIdentifier
      - characterSet
      - dateStamp
      - citationTitle
      - identifier
      - abstract
      - contactOrg
      - contactEmail
      - pointOfContactOrg
      - pointOfContactEmail
      - creationDate
      - identifierDateTypeCode
      - distributionFormatName
      - distributionFormatVersion
      - transferProtocol
      - transferAppProfile
      - transferResourceName
      - transferURL
      - dataQualityDate
      - dataQualityDateTypeCode
      - lineageStatement
      - spatialResolutionDenominator
      - westBoundLongitude
      - eastBoundLongitude
      - southBoundLatitude
      - northBoundLatitude
      - temporalBegin
      - topicCategory

    The config dict should provide values for these keys as needed.

    Returns:
      An ElementTree containing the modified XML.
    """
    if not config:
        raise ValueError("Configuration is required")

    # Construct the path to the XML template file
    xml_file_path = INSPIRE_TEMPLATES_DIR / "inspire-dataset.xml"
    # Load XML file
    template = etree.parse(xml_file_path)

    metadata_info = config["new_inspire_metadata"]

    # Load the mapping from the JSON file.
    with open(INSPIRE_KEY_SIMPLIFICATION_MAPPING_FILE_PATH, "r") as f:
        mapping_data = json.load(f)

    # Retrieve the mapping for INSPIRE metadata.
    mapping = mapping_data.get("inspire", {})
    if not mapping:
        raise ValueError("Mapping for 'inspire' not found in JSON file.")

    # Get the root element of the template.
    root = template.getroot()

    # Iterate over the mapping and update each element if the config provides a value.
    for key, xpath in mapping.items():
        if key in metadata_info and metadata_info[key]:
            elem = root.find(xpath, namespaces=NS)
            if elem is not None:
                elem.text = config[key]

    return etree.ElementTree(root)


def add_distribution_from_template(config: dict, dataset_template=DATASET_TEMPLATE):
    """
    Add a distribution element from its template into the dataset XML.

    Expected config keys:
      - url: Distribution resource URL
      - contact: Distribution contact information


    The following is taken from the documentation:
    -> https://lxml.de/tutorial.html


    >>> root = etree.XML("<root>data</root>")
    >>> print(root.tag)
    root
    >>> etree.tostring(root)
    b'<root>data</root>'

    We can read the template with etree or as a string and then add
    add the template content for distributions. Before we add it we
    can manipulate the content to add user inputs from the YAML file.°
    """
    # Load and get the distribution element from its template
    distribution = etree.parse(
        INSPIRE_TEMPLATES_DIR / "inspire-distribution.xml",
        parser=None,
    ).getroot()

    # Update or add URL element
    if url := config.get("url"):
        (
            distribution.find(".//URL")
            or etree.SubElement(
                distribution,
                "{http://www.isotc211.org/2005/gmd}URL",
                nsmap=NS,
                attrib=None,
            )
        ).text = url

    # Update or add Contact element
    if contact := config.get("contact"):
        (
            distribution.find(".//Contact") or etree.SubElement(distribution, "Contact")
        ).text = contact

    # Get the root of the dataset and find or create the DistributionList element
    root = dataset_template.getroot()
    distribution_list = root.find(".//DistributionList") or etree.SubElement(
        root,
        "{http://www.isotc211.org/2005/gmd}DistributionList",
        nsmap=NS,
        attrib=None,
    )

    # Append the updated distribution element
    distribution_list.append(distribution)

    # Write the modified dataset back to file
    dataset_template.write(
        f"distribution_{config.get('dataset_name')}.xml",
        encoding="utf-8",
        xml_declaration=True,
        pretty_print=True,
    )


# # Example usage (saving is handled elsewhere):
# if __name__ == "__main__":
#     config = {
#         "fileIdentifier": "unique-file-id-12345",
#         "characterSet": "utf8",
#         "dateStamp": "2025-02-28T09:00:00+00:00",
#         "citationTitle": "Example INSPIRE Dataset",
#         "identifier": "http://example.com/dataset/12345",
#         "abstract": "A sample INSPIRE metadata record.",
#         "contactOrg": "Example Organisation",
#         "contactEmail": "contact@example.org",
#         "pointOfContactOrg": "Example Data Team",
#         "pointOfContactEmail": "data@example.org",
#         "creationDate": "2025-02-28",
#         "identifierDateTypeCode": "creation",
#         "distributionFormatName": "GML",
#         "distributionFormatVersion": "3.2",
#         "transferProtocol": "WFS",
#         "transferAppProfile": "http://example.com/appProfile",
#         "transferResourceName": "Online Data Access",
#         "transferURL": "http://example.com/data",
#         "dataQualityDate": "2025-02-27",
#         "dataQualityDateTypeCode": "publication",
#         "lineageStatement": "Data compiled from various sources.",
#         "spatialResolutionDenominator": "1000",
#         "westBoundLongitude": "-10.00",
#         "eastBoundLongitude": "10.00",
#         "southBoundLatitude": "45.00",
#         "northBoundLatitude": "55.00",
#         "temporalBegin": "2020-01-01",
#         "topicCategory": "environment",
#     }

#     modified_tree = create_dataset_from_template(config)
#     # The modified_tree can now be saved using your existing functionality:
#     # modified_tree.write("modified_inspire_dataset.xml", encoding="utf-8",
#     # xml_declaration=True, pretty_print=True)
