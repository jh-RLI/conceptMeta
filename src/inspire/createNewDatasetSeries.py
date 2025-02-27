# Collect metadata stem from all ETL-processes and create
# dataset-series metadata document
# ISSUE: How to create the dataset series metadata
# ... link all datasets individually
# or use a format different from INSPIRE ??

from datetime import datetime

from lxml import etree

from inspire.xmlWrap.namespaces import namespaces


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

    file_identifier = etree.SubElement(
        root,
        "{http://www.isotc211.org/2005/gmd}fileIdentifier",
        nsmap=namespaces,
        attrib=None,
    )

    file_identifier_text = etree.SubElement(
        file_identifier,
        "{http://www.isotc211.org/2005/gco}CharacterString",
        nsmap=namespaces,
        attrib=None,
    )
    file_identifier_text.text = metadata_info.get("file_identifier", "UNKNOWN")

    # Add language
    language = etree.SubElement(
        root,
        "{http://www.isotc211.org/2005/gmd}language",
        nsmap=namespaces,
        attrib=None,
    )
    etree.SubElement(
        language,
        "{http://www.isotc211.org/2005/gmd}LanguageCode",
        nsmap=namespaces,
        attrib=None,
        codeList="http://standards.iso.org/ittf/PubliclyAvailableStandards/ISO_19139_Schemas/resources/codelist/ML_gmxCodelists.xml#LanguageCode",  # noqa
        codeListValue=metadata_info.get("language", "eng"),
    )

    character_set = etree.SubElement(
        root,
        "{http://www.isotc211.org/2005/gmd}characterSet",
        nsmap=namespaces,
        attrib=None,
    )
    etree.SubElement(
        character_set,
        "{http://www.isotc211.org/2005/gmd}MD_CharacterSetCode",
        nsmap=namespaces,
        attrib=None,
        codeList="http://standards.iso.org/ittf/PubliclyAvailableStandards/ISO_19139_Schemas/resources/codelist/ML_gmxCodelists.xml#MD_CharacterSetCode",  # noqa
        codeListValue=metadata_info.get("character_set", "eng"),
    )

    add_resource_type(root, metadata_info)
    add_contact_info(root, metadata_info)
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


def add_contact_info(root: etree.Element, metadata_info: dict) -> None:
    contact = etree.SubElement(
        root,
        "{http://www.isotc211.org/2005/gmd}contact",
        nsmap=namespaces,
        attrib=None,
    )

    ci_responsible_party = etree.SubElement(
        contact,
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

    file_identifier_text = etree.SubElement(
        organisation_name,
        "{http://www.isotc211.org/2005/gco}CharacterString",
        nsmap=namespaces,
        attrib=None,
    )
    file_identifier_text.text = metadata_info["general_contact"].get(
        "organization_name", "UNKNOWN"
    )

    contact_info = etree.SubElement(
        ci_responsible_party,
        "{http://www.isotc211.org/2005/gmd}contactInfo",
        nsmap=namespaces,
        attrib=None,
    )
    ci_contact = etree.SubElement(
        contact_info,
        "{http://www.isotc211.org/2005/gmd}CI_Contact",
        nsmap=namespaces,
        attrib=None,
    )

    # ---------- Phone ---------- #
    # phone = etree.SubElement(
    #     ci_contact,
    #     "{http://www.isotc211.org/2005/gmd}phone",
    #     nsmap=namespaces,
    #     attrib=None,
    # )
    # ci_telephone = etree.SubElement(
    #     phone,
    #     "{http://www.isotc211.org/2005/gmd}CI_Telephone",
    #     nsmap=namespaces,
    #     attrib=None,
    # )
    # voice = etree.SubElement(
    #     ci_telephone,
    #     "{http://www.isotc211.org/2005/gmd}voice",
    #     nsmap=namespaces,
    #     attrib=None,
    # )
    # telephone_text = etree.SubElement(
    #     voice,
    #     "{http://www.isotc211.org/2005/gco}CharacterString",
    #     nsmap=namespaces,
    #     attrib=None,
    # )
    # telephone_text.text = metadata_info["general_contact"].get("phone", "UNKNOWN")

    # ---------- Mail Address ---------- #
    address = etree.SubElement(
        ci_contact,
        "{http://www.isotc211.org/2005/gmd}address",
        nsmap=namespaces,
        attrib=None,
    )
    ci_address = etree.SubElement(
        address,
        "{http://www.isotc211.org/2005/gmd}CI_Address",
        nsmap=namespaces,
        attrib=None,
    )
    administrative_area = etree.SubElement(
        ci_address,
        "{http://www.isotc211.org/2005/gmd}electronicMailAddress",
        nsmap=namespaces,
        attrib=None,
    )
    address_text = etree.SubElement(
        administrative_area,
        "{http://www.isotc211.org/2005/gco}CharacterString",
        nsmap=namespaces,
        attrib=None,
    )
    address_text.text = metadata_info["general_contact"].get("mail_address", "UNKNOWN")

    # ---------- Contact role> ---------- #

    role = etree.SubElement(
        ci_responsible_party,
        "{http://www.isotc211.org/2005/gmd}role",
        nsmap=namespaces,
        attrib=None,
    )

    etree.SubElement(
        role,
        "{http://www.isotc211.org/2005/gmd}CI_RoleCode",
        nsmap=namespaces,
        attrib=None,
        codeList="http://standards.iso.org/iso/19139/resources/gmxCodelists.xml#CI_RoleCode",  # noqa
        codeListValue=metadata_info["general_contact"].get("role", "UNKNOWN"),
    )


def temporal_refs(sub_element: etree.SubElement, metadata_info: dict):
    """ """

    temporal_info = etree.SubElement(
        sub_element,
        "{http://www.isotc211.org/2005/gmd}date",
        nsmap=namespaces,
        attrib=None,
    )

    temporal_element = etree.SubElement(
        temporal_info,
        "{http://www.isotc211.org/2005/gmd}CI_Date",
        nsmap=namespaces,
        attrib=None,
    )

    date = etree.SubElement(
        temporal_element,
        "{http://www.isotc211.org/2005/gmd}date",
        nsmap=namespaces,
        attrib=None,
    )

    dateTime_precision = etree.SubElement(
        date,
        "{http://www.isotc211.org/2005/gco}date",
        nsmap=namespaces,
        attrib=None,
    )

    dateTime_precision.text = metadata_info.get("resource_date", "2013-02-21")

    date_type_element = etree.SubElement(
        temporal_element,
        "{http://www.isotc211.org/2005/gmd}dateType",
        nsmap=namespaces,
        attrib=None,
    )

    etree.SubElement(
        date_type_element,
        "{http://www.isotc211.org/2005/gmd}CI_DateTypeCode",
        nsmap=namespaces,
        attrib=None,
        codeList="http://standards.iso.org/iso/19139/resources/gmxCodelists.xml#CI_DateTypeCode",  # noqa
        codeListValue=metadata_info.get("resource_date_type", "creation"),
    )


def add_citation(sub_element: etree.SubElement, metadata_info: dict):
    citation_info = etree.SubElement(
        sub_element,
        "{http://www.isotc211.org/2005/gmd}citation",
        nsmap=namespaces,
        attrib=None,
    )

    citation_element = etree.SubElement(
        citation_info,
        "{http://www.isotc211.org/2005/gmd}CI_Citation",
        nsmap=namespaces,
        attrib=None,
    )

    # Title
    title = etree.SubElement(
        citation_element,
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
    temporal_refs(citation_element, metadata_info)

    resource_id = etree.SubElement(
        citation_element,
        "{http://www.isotc211.org/2005/gmd}identifier",
        nsmap=namespaces,
        attrib=None,
    )

    resource_id_element = etree.SubElement(
        resource_id,
        "{http://www.isotc211.org/2005/gmd}MD_Identifier",
        nsmap=namespaces,
        attrib=None,
    )

    resource_id_code = etree.SubElement(
        resource_id_element,
        "{http://www.isotc211.org/2005/gmd}code",
        nsmap=namespaces,
        attrib=None,
    )

    resource_id_code.text = metadata_info.get("file_identifier", "UNKNOWN")


def descriptive_keywords(sub_element: etree.SubElement, metadata_info: dict):
    # Keywords
    descriptive_keywords = etree.SubElement(
        sub_element,
        "{http://www.isotc211.org/2005/gmd}descriptiveKeywords",
        nsmap=namespaces,
        attrib=None,
    )
    keyword_element = etree.SubElement(
        descriptive_keywords,
        "{http://www.isotc211.org/2005/gmd}MD_Keywords",
        nsmap=namespaces,
        attrib=None,
    )
    thesaurus_name = etree.SubElement(
        keyword_element,
        "{http://www.isotc211.org/2005/gmd}thesaurusName",
        nsmap=namespaces,
        attrib=None,
    )
    ci_citation = etree.SubElement(
        thesaurus_name,
        "{http://www.isotc211.org/2005/gmd}CI_Citation",
        nsmap=namespaces,
        attrib=None,
    )
    keyword_title = etree.SubElement(
        ci_citation,
        "{http://www.isotc211.org/2005/gmd}title",
        nsmap=namespaces,
        attrib=None,
    )
    keyword_title_anchor = etree.SubElement(
        keyword_title,
        "{http://www.isotc211.org/2005/gmx}Anchor",
        nsmap=namespaces,
        attrib=None,
        xlink="https://www.eionet.europa.eu/gemet/en/inspire-themes/",
    )
    keyword_title_anchor.text = "GEMET - INSPIRE themes, version 1.0"

    keywords = metadata_info.get("keywords", [])
    for keyword in keywords:
        keyword_tag = etree.SubElement(
            keyword_element,
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


def add_spatial_resolution_info(
    sub_element: etree.Element, metadata_info: dict
) -> None:
    spatial_resolution = etree.SubElement(
        sub_element,
        "{http://www.isotc211.org/2005/gmd}spatialResolution",
        nsmap=namespaces,
        attrib=None,
    )

    resolution_element = etree.SubElement(
        spatial_resolution,
        "{http://www.isotc211.org/2005/gmd}MD_Resolution",
        nsmap=namespaces,
        attrib=None,
    )

    # TODO: Only one of the following should be present
    if "distance" in metadata_info["spatial_resolution"]:
        equivalent_scale = etree.SubElement(
            resolution_element,
            "{http://www.isotc211.org/2005/gmd}equivalentScale",
            nsmap=namespaces,
            attrib=None,
        )

        representaion_fraction_element = etree.SubElement(
            equivalent_scale,
            "{http://www.isotc211.org/2005/gmd}MD_RepresentativeFraction",
            nsmap=namespaces,
            attrib=None,
        )

        denominator = etree.SubElement(
            representaion_fraction_element,
            "{http://www.isotc211.org/2005/gmd}denominator",
            nsmap=namespaces,
            attrib=None,
        )

        denominator_int_value = etree.SubElement(
            denominator,
            "{http://www.isotc211.org/2005/gco}integer",
            nsmap=namespaces,
            attrib=None,
        )

        denominator_int_value.text = str(
            metadata_info["spatial_resolution"]["equivalent_scale"]
        )
    elif metadata_info["spatial_resolution>"]["distance>"]:
        # TODO: Intervals not implemented yet
        distance = etree.SubElement(
            resolution_element,
            "{http://www.isotc211.org/2005/gmd}distance",
            nsmap=namespaces,
            attrib=None,
        )

        distance_value = etree.SubElement(
            distance,
            "{http://www.isotc211.org/2005/gco}Distance",
            nsmap=namespaces,
            attrib=None,
        )
        distance_value.text = metadata_info["spatial_resolution"]["distance"]


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

    add_citation(identification_info, metadata_info)

    # Abstract
    abstract = etree.SubElement(
        identification_info,
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

    # Group Keywords - added to root
    descriptive_keywords(data_identification, metadata_info)
    # Optional: Keywords add to identification info section
    # descriptive_keywords(identification_info, metadata_info)

    # Spatial Resolution
    add_spatial_resolution_info(data_identification, metadata_info)

    # resource language
    language = etree.SubElement(
        data_identification,
        "{http://www.isotc211.org/2005/gmd}language",
        nsmap=namespaces,
        attrib=None,
    )

    language = etree.SubElement(
        language,
        "{http://www.isotc211.org/2005/gmd}LanguageCode",
        nsmap=namespaces,
        attrib=None,
        codeList="http://www.loc.gov/standards/iso639-2/",
        codeListValue=metadata_info.get("resource_language", "eng"),
    )

    # language_text = etree.SubElement(
    #     language,
    #     "{http://www.isotc211.org/2005/gco}CharacterString",
    #     nsmap=namespaces,
    #     attrib=None,
    # )
    # language_text.text = metadata_info.get("resource_language", "eng")
    # # Default to English

    # Topic Category
    if not metadata_info["topic_category"]:
        print("No topic category found. At least one is required.")

    for i in metadata_info.get("topic_category", "geoscientificInformation"):
        topic_category = etree.SubElement(
            data_identification,
            "{http://www.isotc211.org/2005/gmd}topicCategory",
            nsmap=namespaces,
            attrib=None,
        )

        topic_category = etree.SubElement(
            topic_category,
            "{http://www.isotc211.org/2005/gmd}MD_TopicCategoryCode",
            nsmap=namespaces,
            attrib=None,
        )

        topic_category.text = i

    # # Resource Locator (URL)
    # TODO: Should be already added in MD_DigitalTransferOptions
    # if "resource_locator" in metadata_info:
    #     resource_locator = etree.SubElement(
    #         data_identification,
    #         "{http://www.isotc211.org/2005/gmd}resourceLocator",
    #         nsmap=namespaces,
    #         attrib=None,
    #     )
    #     url = etree.SubElement(
    #         resource_locator,
    #         "{http://www.isotc211.org/2005/gmd}URL",
    #         nsmap=namespaces,
    #         attrib=None,
    #     )
    #     url.text = metadata_info["resource_locator"]

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
            codeListValue=metadata_info["responsible_party"].get("role", "owner"),
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


def add_report_result_citation(sub_element: etree.SubElement, metadata_info: dict):
    citation = etree.SubElement(
        sub_element,
        "{http://www.isotc211.org/2005/gmd}CI_Citation",
        nsmap=namespaces,
        attrib=None,
    )

    citation_date = etree.SubElement(
        citation,
        "{http://www.isotc211.org/2005/gmd}date",
        nsmap=namespaces,
        attrib=None,
    )

    citation_date_element = etree.SubElement(
        citation_date,
        "{http://www.isotc211.org/2005/gmd}CI_Date",
        nsmap=namespaces,
        attrib=None,
    )

    date_type = etree.SubElement(
        citation_date_element,
        "{http://www.isotc211.org/2005/gmd}dateType",
        nsmap=namespaces,
        attrib=None,
    )

    date_type_code = etree.SubElement(
        date_type,
        "{http://www.isotc211.org/2005/gmd}CI_DateTypeCode",
        nsmap=namespaces,
        attrib=None,
        codeList="http://standards.iso.org/iso/19139/resources/gmxCodelists.xml#CI_DateTypeCode",  # noqa
        codeListValue=metadata_info.get("data_quality", {}).get(
            "date_type", "publication"
        ),
    )
    date_type_code.text = (
        metadata_info["data_quality"].get("date_type", "publication"),
    )


def add_report_domain_consistency(sub_element: etree.SubElement, metadata_info: dict):
    report = etree.SubElement(
        sub_element,
        "{http://www.isotc211.org/2005/gmd}result",
        nsmap=namespaces,
        attrib=None,
    )

    element_domain_consistency = etree.SubElement(
        report,
        "{http://www.isotc211.org/2005/gmd}DQ_DomainConsistency",
        nsmap=namespaces,
        attrib=None,
    )

    result = etree.SubElement(
        element_domain_consistency,
        "{http://www.isotc211.org/2005/gmd}result",
        nsmap=namespaces,
        attrib=None,
    )

    result_element = etree.SubElement(
        result,
        "{http://www.isotc211.org/2005/gmd}DQ_ConformanceResult",
        nsmap=namespaces,
        attrib=None,
    )

    bool_pass_element = etree.SubElement(
        result_element,
        "{http://www.isotc211.org/2005/gmd}pass",
        nsmap=namespaces,
        attrib=None,
    )

    bool_pass = etree.SubElement(
        bool_pass_element,
        "{http://www.isotc211.org/2005/gco}boolean",
        nsmap=namespaces,
        attrib=None,
    )
    bool_pass.text = metadata_info["data_quality"]["domain_conformance_result_pass"]

    specification = etree.SubElement(
        result,
        "{http://www.isotc211.org/2005/gmd}specification",
        nsmap=namespaces,
        attrib=None,
    )

    add_report_result_citation(specification, metadata_info)


def add_lineage(sub_element: etree.SubElement, metadata_info: dict) -> None:
    """
    Adds lineage information to the metadata document.

    Args:
        root (etree.Element): The root element of the XML document.
        metadata_info (dict): Dictionary containing metadata properties.
    """

    lineage = etree.SubElement(
        sub_element,
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


def add_data_quality_info(root: etree.Element, metadata_info: dict):
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

    if "lineage" in metadata_info:
        add_lineage(dq_data_quality, metadata_info)


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
        use_constraints = etree.SubElement(
            md_constraints,
            "{http://www.isotc211.org/2005/gmd}useConstraints",
            nsmap=namespaces,
            attrib=None,
        )
        etree.SubElement(
            use_constraints,
            "{http://www.isotc211.org/2005/gmd}MD_RestrictionCode",
            nsmap=namespaces,
            attrib=None,
            codeList="http://standards.iso.org/iso/19139/resources/gmxCodelists.xml#MD_RestrictionCode",  # noqa
            codeListValue=metadata_info["constraints"].get(
                "use_constraints_code_list", "otherRestrictions"
            ),
        )
        access_constraints = etree.SubElement(
            md_constraints,
            "{http://www.isotc211.org/2005/gmd}accessConstraints",
            nsmap=namespaces,
            attrib=None,
        )
        etree.SubElement(
            access_constraints,
            "{http://www.isotc211.org/2005/gmd}MD_RestrictionCode",
            nsmap=namespaces,
            attrib=None,
            codeList="http://standards.iso.org/ittf/PubliclyAvailableStandards/ISO_19139_Schemas/resources/Codelist/ML_gmxCodelists.xml#MD_RestrictionCode",  # noqa
            codeListValue=metadata_info["constraints"].get(
                "access_constraints_code_list", "otherRestrictions"
            ),
        )
        other_constraints = etree.SubElement(
            md_constraints,
            "{http://www.isotc211.org/2005/gmd}otherConstraints",
            nsmap=namespaces,
            attrib=None,
        )
        etree.SubElement(
            other_constraints,
            "{http://www.isotc211.org/2005/gmx}Anchor",
            nsmap=namespaces,
            attrib=None,
            xlink=metadata_info["constraints"].get(
                "other_constraints_anchor", "otherRestrictions"
            ),
        )
        # other_contrains_anchor.text = (
        #     metadata_info["constraints"].get(
        #         "other_constraints_anchor_text", "otherRestrictions"
        #     ),
        # )


def add_geographic_extent(root: etree.Element, metadata_info: dict) -> None:
    """
    Adds geographic extent (bounding box) to the metadata document.

    If /gmd:MD_Metadata/gmd:hierarchyLevel/gmd:MD_ScopeCode is dataset or series
    this field is required. For services it is optional.

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


def add_resource_type(sub_element: etree.SubElement, metadata_info: dict):
    resource_type = etree.SubElement(
        sub_element,
        "{http://www.isotc211.org/2005/gmd}hierarchyLevel",
        nsmap=namespaces,
        attrib=None,
    )
    md_scope_code = etree.SubElement(
        resource_type,
        "{http://www.isotc211.org/2005/gmd}MD_ScopeCode",
        nsmap=namespaces,
        attrib=None,
        codeList="http://standards.iso.org/ittf/PubliclyAvailableStandards/ISO_19139_Schemas/resources/Codelist/ML_gmxCodelists.xml#MD_ScopeCode",  # noqa
        codeListValue=metadata_info.get("resource_type", "dataset"),
    )
    md_scope_code.text = metadata_info.get("resource_type", "dataset")


def add_distribution_info(root: etree.Element, metadata_info: dict) -> None:
    """
    Adds distribution information to the metadata document.

    Args:
        root (etree.Element): The root element of the XML document.
        metadata_info (dict): Dictionary containing metadata properties.
    """
    # Create distributionInfo section
    distribution_info = etree.SubElement(
        root,
        "{http://www.isotc211.org/2005/gmd}distributionInfo",
        nsmap=namespaces,
        attrib=None,
    )
    md_distribution = etree.SubElement(
        distribution_info,
        "{http://www.isotc211.org/2005/gmd}MD_Distribution",
        nsmap=namespaces,
        attrib=None,
    )

    # Add distributor (required)
    if "distributor" in metadata_info:
        distributor = etree.SubElement(
            md_distribution,
            "{http://www.isotc211.org/2005/gmd}distributor",
            nsmap=namespaces,
            attrib=None,
        )
        md_distributor = etree.SubElement(
            distributor,
            "{http://www.isotc211.org/2005/gmd}MD_Distributor",
            nsmap=namespaces,
            attrib=None,
        )
        distributor_contact = etree.SubElement(
            md_distributor,
            "{http://www.isotc211.org/2005/gmd}distributorContact",
            nsmap=namespaces,
            attrib=None,
        )
        ci_responsible_party = etree.SubElement(
            distributor_contact,
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
        organisation_name_text.text = metadata_info["distributor"].get(
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
            codeListValue="distributor",
        )
        role_code.text = "distributor"

    # Add distribution format (optional but recommended)
    if "distribution_format" in metadata_info:
        distribution_format = etree.SubElement(
            md_distribution,
            "{http://www.isotc211.org/2005/gmd}distributionFormat",
            nsmap=namespaces,
            attrib=None,
        )
        md_format = etree.SubElement(
            distribution_format,
            "{http://www.isotc211.org/2005/gmd}MD_Format",
            nsmap=namespaces,
            attrib=None,
        )
        format_name = etree.SubElement(
            md_format,
            "{http://www.isotc211.org/2005/gmd}name",
            nsmap=namespaces,
            attrib=None,
        )
        format_name_text = etree.SubElement(
            format_name,
            "{http://www.isotc211.org/2005/gco}CharacterString",
            nsmap=namespaces,
            attrib=None,
        )
        format_name_text.text = metadata_info["distribution_format"].get(
            "name", "Unknown Format"
        )
        format_version = etree.SubElement(
            md_format,
            "{http://www.isotc211.org/2005/gmd}version",
            nsmap=namespaces,
            attrib=None,
        )
        format_version_text = etree.SubElement(
            format_version,
            "{http://www.isotc211.org/2005/gco}CharacterString",
            nsmap=namespaces,
            attrib=None,
        )
        format_version_text.text = metadata_info["distribution_format"].get(
            "version", "1.0"
        )

    # Add transfer options (optional but recommended)
    if "transfer_options" in metadata_info:
        transfer_options = etree.SubElement(
            md_distribution,
            "{http://www.isotc211.org/2005/gmd}transferOptions",
            nsmap=namespaces,
            attrib=None,
        )
        md_digital_transfer_options = etree.SubElement(
            transfer_options,
            "{http://www.isotc211.org/2005/gmd}MD_DigitalTransferOptions",
            nsmap=namespaces,
            attrib=None,
        )
        for option in metadata_info["transfer_options"]:
            online_resource = etree.SubElement(
                md_digital_transfer_options,
                "{http://www.isotc211.org/2005/gmd}onLine",
                nsmap=namespaces,
                attrib=None,
            )
            ci_online_resource = etree.SubElement(
                online_resource,
                "{http://www.isotc211.org/2005/gmd}CI_OnlineResource",
                nsmap=namespaces,
                attrib=None,
            )
            linkage = etree.SubElement(
                ci_online_resource,
                "{http://www.isotc211.org/2005/gmd}linkage",
                nsmap=namespaces,
                attrib=None,
            )
            url = etree.SubElement(
                linkage,
                "{http://www.isotc211.org/2005/gmd}URL",
                nsmap=namespaces,
                attrib=None,
            )
            url.text = metadata_info["transfer_options"][option].get(
                "url", "https://example.com"
            )

            # TODO: THis is optional
            name = etree.SubElement(
                ci_online_resource,
                "{http://www.isotc211.org/2005/gmd}name",
                nsmap=namespaces,
                attrib=None,
            )
            name_text = etree.SubElement(
                name,
                "{http://www.isotc211.org/2005/gco}CharacterString",
                nsmap=namespaces,
                attrib=None,
            )
            name_text.text = metadata_info["transfer_options"][option].get(
                "name", "example"
            )

            # TODO: Add optional CI_OnLineFunctionCode


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

    add_distribution_info(root, metadata_info)

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
