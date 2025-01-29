# Collect metadata stem from all ETL-processes and create
# dataset-series metadata document
# ISSUE: How to create the dataset series metadata
# ... link all datasets individually
# or use a format different from INSPIRE ??

from datetime import datetime

from lxml import etree

from xmlWrap.namespaces import namespaces


def create_root_element() -> etree.Element:
    """
    Creates the root element for the INSPIRE metadata document.

    Returns:
        etree.Element: The root element.
    """
    return etree.Element(
        "{http://www.isotc211.org/2005/gmd}MD_Metadata", nsmap=namespaces, attrib=None
    )


def add_basic_metadata(root: etree.Element, metadata_info: dict) -> None:
    """
    Adds basic metadata fields to the root element.

    Args:
        root (etree.Element): The root element of the XML document.
        metadata_info (dict): Dictionary containing metadata properties.
    """
    # Add fileIdentifier
    file_id = etree.SubElement(
        root,
        "{http://www.isotc211.org/2005/gmd}fileIdentifier",
        nsmap=namespaces,
        attrib=None,
    )
    file_id_text = etree.SubElement(
        file_id,
        "{http://www.isotc211.org/2005/gco}CharacterString",
        nsmap=namespaces,
        attrib=None,
    )
    file_id_text.text = metadata_info.get("fileIdentifier", "UNKNOWN")

    # Add language
    language = etree.SubElement(
        root,
        "{http://www.isotc211.org/2005/gmd}language",
        nsmap=namespaces,
        attrib=None,
    )
    language_text = etree.SubElement(
        language,
        "{http://www.isotc211.org/2005/gco}CharacterString",
        nsmap=namespaces,
        attrib=None,
    )
    language_text.text = metadata_info.get("language", "eng")  # Default to English

    # Add dateStamp
    date_stamp = etree.SubElement(
        root,
        "{http://www.isotc211.org/2005/gmd}dateStamp",
        nsmap=namespaces,
        attrib=None,
    )
    date_stamp_text = etree.SubElement(
        date_stamp,
        "{http://www.isotc211.org/2005/gco}Date",
        nsmap=namespaces,
        attrib=None,
    )
    date_stamp_text.text = datetime.now().strftime("%Y-%m-%d")


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
        "{http://www.isotc211.org/2005/gmd}MD_DataIdentification",
        nsmap=namespaces,
        attrib=None,
    )

    # Title
    title = etree.SubElement(
        data_identification,
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

    # Abstract
    abstract = etree.SubElement(
        data_identification,
        "{http://www.isotc211.org/2005/gmd}abstract",
        nsmap=namespaces,
        attrib=None,
    )
    abstract_text = etree.SubElement(
        abstract,
        "{http://www.isotc211.org/2005/gco}CharacterString",
        nsmap=namespaces,
        attrib=None,
    )
    abstract_text.text = metadata_info.get("abstract", "Dataset Abstract")

    # Keywords
    descriptive_keywords = etree.SubElement(
        data_identification,
        "{http://www.isotc211.org/2005/gmd}descriptiveKeywords",
        nsmap=namespaces,
        attrib=None,
    )
    keyword_section = etree.SubElement(
        descriptive_keywords,
        "{http://www.isotc211.org/2005/gmd}MD_Keywords",
        nsmap=namespaces,
        attrib=None,
    )
    keywords = metadata_info.get("keywords", [])
    for keyword in keywords:
        keyword_tag = etree.SubElement(
            keyword_section,
            "{http://www.isotc211.org/2005/gmd}keyword",
            nsmap=namespaces,
            attrib=None,
        )
        keyword_text = etree.SubElement(
            keyword_tag,
            "{http://www.isotc211.org/2005/gco}CharacterString",
            nsmap=namespaces,
            attrib=None,
        )
        keyword_text.text = keyword

    # Resource Type
    resource_type = etree.SubElement(
        data_identification,
        "{http://www.isotc211.org/2005/gmd}resourceType",
        nsmap=namespaces,
        attrib=None,
    )
    resource_type_code = etree.SubElement(
        resource_type,
        "{http://www.isotc211.org/2005/gmd}MD_ScopeCode",
        nsmap=namespaces,
        attrib=None,
        codeList="http://standards.iso.org/ittf/PubliclyAvailableStandards/ISO_19139_Schemas/resources/Codelist/ML_gmxCodelists.xml#MD_ScopeCode",  # noqa
        codeListValue="dataset",
    )
    resource_type_code.text = "dataset"

    # Resource Locator (URL)
    if "resource_locator" in metadata_info:
        resource_locator = etree.SubElement(
            data_identification,
            "{http://www.isotc211.org/2005/gmd}resourceLocator",
            nsmap=namespaces,
            attrib=None,
        )
        url = etree.SubElement(
            resource_locator,
            "{http://www.isotc211.org/2005/gmd}URL",
            nsmap=namespaces,
            attrib=None,
        )
        url.text = metadata_info["resource_locator"]

    # Responsible Party
    if "responsible_party" in metadata_info:
        responsible_party = etree.SubElement(
            data_identification,
            "{http://www.isotc211.org/2005/gmd}pointOfContact",
            nsmap=namespaces,
            attrib=None,
        )
        ci_responsible_party = etree.SubElement(
            responsible_party,
            "{http://www.isotc211.org/2005/gmd}CI_ResponsibleParty",
            nsmap=namespaces,
            attrib=None,
        )
        organisation_name = etree.SubElement(
            ci_responsible_party,
            "{http://www.isotc211.org/2005/gmd}organisationName",
            nsmap=namespaces,
            attrib=None,
        )
        organisation_name_text = etree.SubElement(
            organisation_name,
            "{http://www.isotc211.org/2005/gco}CharacterString",
            nsmap=namespaces,
            attrib=None,
        )
        organisation_name_text.text = metadata_info["responsible_party"].get(
            "organisation_name", "Unknown Organisation"
        )
        role = etree.SubElement(
            ci_responsible_party,
            "{http://www.isotc211.org/2005/gmd}role",
            nsmap=namespaces,
            attrib=None,
        )
        role_code = etree.SubElement(
            role,
            "{http://www.isotc211.org/2005/gmd}CI_RoleCode",
            nsmap=namespaces,
            attrib=None,
            codeList="http://standards.iso.org/ittf/PubliclyAvailableStandards/ISO_19139_Schemas/resources/Codelist/ML_gmxCodelists.xml#CI_RoleCode",  # noqa
            codeListValue="owner",
        )
        role_code.text = metadata_info["responsible_party"].get("role", "owner")

    # Spatial Representation Type
    spatial_representation_type = etree.SubElement(
        data_identification,
        "{http://www.isotc211.org/2005/gmd}spatialRepresentationType",
        nsmap=namespaces,
        attrib=None,
    )
    spatial_representation_type_code = etree.SubElement(
        spatial_representation_type,
        "{http://www.isotc211.org/2005/gmd}MD_SpatialRepresentationTypeCode",
        nsmap=namespaces,
        attrib=None,
        codeList="http://standards.iso.org/ittf/PubliclyAvailableStandards/ISO_19139_Schemas/resources/Codelist/ML_gmxCodelists.xml#MD_SpatialRepresentationTypeCode",  # noqa
        codeListValue="vector",
    )
    spatial_representation_type_code.text = metadata_info.get(
        "spatial_representation_type", "vector"
    )


def add_reference_system(root: etree.Element, metadata_info: dict) -> None:
    """
    Adds reference system information to the metadata document.

    Args:
        root (etree.Element): The root element of the XML document.
        metadata_info (dict): Dictionary containing metadata properties.
    """
    if "reference_system" in metadata_info:
        reference_system_info = etree.SubElement(
            root,
            "{http://www.isotc211.org/2005/gmd}referenceSystemInfo",
            nsmap=namespaces,
            attrib=None,
        )
        reference_system = etree.SubElement(
            reference_system_info,
            "{http://www.isotc211.org/2005/gmd}MD_ReferenceSystem",
            nsmap=namespaces,
            attrib=None,
        )
        reference_system_identifier = etree.SubElement(
            reference_system,
            "{http://www.isotc211.org/2005/gmd}referenceSystemIdentifier",
            nsmap=namespaces,
            attrib=None,
        )
        rs_identifier = etree.SubElement(
            reference_system_identifier,
            "{http://www.isotc211.org/2005/gmd}RS_Identifier",
            nsmap=namespaces,
            attrib=None,
        )
        code = etree.SubElement(
            rs_identifier,
            "{http://www.isotc211.org/2005/gmd}code",
            nsmap=namespaces,
            attrib=None,
        )
        code_text = etree.SubElement(
            code,
            "{http://www.isotc211.org/2005/gco}CharacterString",
            nsmap=namespaces,
            attrib=None,
        )
        code_text.text = metadata_info["reference_system"]


def add_lineage(root: etree.Element, metadata_info: dict) -> None:
    """
    Adds lineage information to the metadata document.

    Args:
        root (etree.Element): The root element of the XML document.
        metadata_info (dict): Dictionary containing metadata properties.
    """
    if "lineage" in metadata_info:
        lineage_info = etree.SubElement(
            root,
            "{http://www.isotc211.org/2005/gmd}dataQualityInfo",
            nsmap=namespaces,
            attrib=None,
        )
        dq_data_quality = etree.SubElement(
            lineage_info,
            "{http://www.isotc211.org/2005/gmd}DQ_DataQuality",
            nsmap=namespaces,
            attrib=None,
        )
        lineage = etree.SubElement(
            dq_data_quality,
            "{http://www.isotc211.org/2005/gmd}lineage",
            nsmap=namespaces,
            attrib=None,
        )
        li_lineage = etree.SubElement(
            lineage,
            "{http://www.isotc211.org/2005/gmd}LI_Lineage",
            nsmap=namespaces,
            attrib=None,
        )
        statement = etree.SubElement(
            li_lineage,
            "{http://www.isotc211.org/2005/gmd}statement",
            nsmap=namespaces,
            attrib=None,
        )
        statement_text = etree.SubElement(
            statement,
            "{http://www.isotc211.org/2005/gco}CharacterString",
            nsmap=namespaces,
            attrib=None,
        )
        statement_text.text = metadata_info["lineage"]


def add_constraints(root: etree.Element, metadata_info: dict) -> None:
    """
    Adds constraints information to the metadata document.

    Args:
        root (etree.Element): The root element of the XML document.
        metadata_info (dict): Dictionary containing metadata properties.
    """
    if "constraints" in metadata_info:
        constraints_info = etree.SubElement(
            root,
            "{http://www.isotc211.org/2005/gmd}resourceConstraints",
            nsmap=namespaces,
            attrib=None,
        )
        md_constraints = etree.SubElement(
            constraints_info,
            "{http://www.isotc211.org/2005/gmd}MD_LegalConstraints",
            nsmap=namespaces,
            attrib=None,
        )
        access_constraints = etree.SubElement(
            md_constraints,
            "{http://www.isotc211.org/2005/gmd}accessConstraints",
            nsmap=namespaces,
            attrib=None,
        )
        access_constraints_code = etree.SubElement(
            access_constraints,
            "{http://www.isotc211.org/2005/gmd}MD_RestrictionCode",
            nsmap=namespaces,
            attrib=None,
            codeList="http://standards.iso.org/ittf/PubliclyAvailableStandards/ISO_19139_Schemas/resources/Codelist/ML_gmxCodelists.xml#MD_RestrictionCode",  # noqa
            codeListValue="otherRestrictions",
        )
        access_constraints_code.text = metadata_info["constraints"].get(
            "access_constraints", "otherRestrictions"
        )
        use_constraints = etree.SubElement(
            md_constraints,
            "{http://www.isotc211.org/2005/gmd}useConstraints",
            nsmap=namespaces,
            attrib=None,
        )
        use_constraints_code = etree.SubElement(
            use_constraints,
            "{http://www.isotc211.org/2005/gmd}MD_RestrictionCode",
            nsmap=namespaces,
            attrib=None,
            codeList="http://standards.iso.org/ittf/PubliclyAvailableStandards/ISO_19139_Schemas/resources/Codelist/ML_gmxCodelists.xml#MD_RestrictionCode",  # noqa
            codeListValue="otherRestrictions",
        )
        use_constraints_code.text = metadata_info["constraints"].get(
            "use_constraints", "otherRestrictions"
        )


def add_geographic_extent(root: etree.Element, metadata_info: dict) -> None:
    """
    Adds geographic extent (bounding box) to the metadata document.

    Args:
        root (etree.Element): The root element of the XML document.
        metadata_info (dict): Dictionary containing metadata properties.
    """
    if "bbox" in metadata_info:
        extent = etree.SubElement(
            root,
            "{http://www.isotc211.org/2005/gmd}extent",
            nsmap=namespaces,
            attrib=None,
        )
        geographic_element = etree.SubElement(
            extent,
            "{http://www.isotc211.org/2005/gmd}EX_GeographicBoundingBox",
            nsmap=namespaces,
            attrib=None,
        )
        west = etree.SubElement(
            geographic_element,
            "{http://www.isotc211.org/2005/gmd}westBoundLongitude",
            nsmap=namespaces,
            attrib=None,
        )
        west_text = etree.SubElement(
            west,
            "{http://www.isotc211.org/2005/gco}Decimal",
            nsmap=namespaces,
            attrib=None,
        )
        west_text.text = str(metadata_info["bbox"]["west"])

        east = etree.SubElement(
            geographic_element,
            "{http://www.isotc211.org/2005/gmd}eastBoundLongitude",
            nsmap=namespaces,
            attrib=None,
        )
        east_text = etree.SubElement(
            east,
            "{http://www.isotc211.org/2005/gco}Decimal",
            nsmap=namespaces,
            attrib=None,
        )
        east_text.text = str(metadata_info["bbox"]["east"])

        south = etree.SubElement(
            geographic_element,
            "{http://www.isotc211.org/2005/gmd}southBoundLatitude",
            nsmap=namespaces,
            attrib=None,
        )
        south_text = etree.SubElement(
            south,
            "{http://www.isotc211.org/2005/gco}Decimal",
            nsmap=namespaces,
            attrib=None,
        )
        south_text.text = str(metadata_info["bbox"]["south"])

        north = etree.SubElement(
            geographic_element,
            "{http://www.isotc211.org/2005/gmd}northBoundLatitude",
            nsmap=namespaces,
            attrib=None,
        )
        north_text = etree.SubElement(
            north,
            "{http://www.isotc211.org/2005/gco}Decimal",
            nsmap=namespaces,
            attrib=None,
        )
        north_text.text = str(metadata_info["bbox"]["north"])


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

    # Add identification info
    add_identification_info(root, metadata_info)

    # Add reference system
    add_reference_system(root, metadata_info)

    # Add lineage
    add_lineage(root, metadata_info)

    # Add constraints
    add_constraints(root, metadata_info)

    # Add geographic extent
    add_geographic_extent(root, metadata_info)

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
