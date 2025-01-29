from dataclasses import dataclass


@dataclass
class InspireMetadataInfoTemplateModel:
    """
    MD_Metadata/
    &&
    && contact/CI_ResponsibleParty
    """

    # REQUIRED LanguageCode
    metadata_language: str  # LanguageCode, codeListValue
    character_set: str  # MD_CharacterSetCode, codeListValue
    hierarchy_level: str  # MD_ScopeCode, codeListValue
    hierarchy_level_name: str  # CharacterString
    # REQUIRED: CI_ResponsiblePar
    # REQUIRED: organisationName
    organisation_name: (
        str  # CharacterString in contact / CI_ResponsibleParty / organisationName
    )
    # REQUIRED: electronicMailAddress
    organisation_email: str  # CharacterString in contact / CI_ResponsibleParty / contactInfo / CI_Contact / address / CI_Address / electronicMailAddress # noqa
    # Required: dateStamp
    metadata_date: str  # dateStamp / Date YYYY-MM-DD


@dataclass
class InspireResourceInfoTemplate:
    """
    MD_Metadata/MD_DataIdentification
    && gmd:pointOfContact/gmd:CI_ResponsibleParty
    && gmd:extent/gmd:EX_Extent
       gmd:temporalElement/gmd:EX_TemporalExtent/gmd:exten
       ++ gml:TimeInstant/gml:timePosition
    && gmd:descriptiveKeywords/gmd:MD_Keywords/gmd:thesaurusName/gmd:CI_Citation
       ++ gmd:date/gmd:CI_Date/gmd:date/gco:Date
       ++ gmd:dateType/gmd:CI_DateTypeCode
    && /gmd:descriptiveKeywords/gmd:MD_Keywords
        ++ gmd:keyword
    && /md:resourceConstraints/gmd:MD_LegalConstraints
        ++ accessConstraints / gmd:MD_RestrictionCode (code list otherRestrictions")
        ++ gmd:otherConstraints/gmx:Anchor
    && gmd:extent/gmd:EX_Extent/gmd:geographicElement/gmd:EX_GeographicBoundingBox

    """

    # REQUIRED: title
    title: str  # identificationInfo / MD_DataIdentification / citation / CI_Citation / title / CharacterString # noqa
    # REQUIRED: abstract
    abstract: (
        str  # identificationInfo / MD_DataIdentification / abstract / CharacterString
    )
    # REQUIRED: CI_ResponsibleParty
    # REQUIRED: organisationName
    organisation_name: str
    # REQUIRED: electronicMailAddress
    organisation_email: str
    # REQUIRED: gmd:role /gmd:CI_RoleCode
    role_code: str

    # REQUIRED: gmd:citation/gmd:CI_Citation/gmd:date/gmd:CI_Date/gmd:date
    # REQUIRED only one of the following 3
    # all date / time in ISO 8601 format
    publication: bool
    # max 1, spatial data should report date of last revision
    revision: bool
    # max 1
    creation: bool
    # REQUIRED: gmd:date/gmd:CI_Date/gmd:dateType/gmd:CI_DateTypeCode
    date_type_code: str
    # REQUIRED: gmd:CI_Date/gmd:date/gco:DateTime
    date_time: str

    # REQUIRED: if extend is used in time position
    # It is possible to add multiple extends
    start_position: str
    end_position: str
    indeterminate_position: str  # unknown" / "now"

    # REQUIRED but CASE-DEPEN   DING: gmd:descriptiveKeywords/gmd:MD_Keywords/gmd:thesaurusName/gmd:CI_Citation # noqa
    # Depending on the keyword this section needs more fields
    # Especially if the keyword is from a thesaurus
    keyword_vocab_title: str  # use Anchor if link to Vocabulary with xlink:href=
    keyword_vocab_date: str
    keyword_vocab_publication: bool
    # max 1, spatial data should report date of last revision
    keyword_vocab_revision: bool
    # max 1
    keyword_vocab_creation: bool
    # REQUIRED: gmd:date/gmd:CI_Date/gmd:dateType/gmd:CI_DateTypeCode
    keyword_vocab_date_type_code: str
    # REQUIRED: gmd:CI_Date/gmd:date/gco:DateTime
    keyword_vocab_date_time: str

    keyword_name: str  # use Anchor with xlink:href= pointing to the Vocabulary specified in keyword_vocab_title # noqa

    # REQUIRED: /md:resourceConstraints/gmd:MD_LegalConstraints/accessConstraints

    # TODO: Denke hier muss ein template eingefügt werden, nur der value constrain kann anders sein (vermutlich) # noqa
    # REQUIRED: /md:resourceConstraints/gmd:MD_LegalConstraints/otherConstraints
    value_other_constraints: str  # Anchor element possible values "conditionsUnknown" / noConditionsApply" / Free text code list ConditionsApplyingToAccessAndUse # noqa

    # REQUIRED: gmd:extent/gmd:EX_Extent/gmd:geographicElement/gmd:EX_GeographicBoundingBox # noqa
    # at least 1 in dataset & series 0 or more in service
    west_bound_longitude: float
    east_bound_longitude: float
    south_bound_latitude: float
    north_bound_latitude: float


@dataclass
class InspireDataQualityTemplate:
    """
    dataQualityInfo/DQ_DataQuality

    && gmd:report/gmd:DQ_DomainConsistency/gmd:result/
        ++ DQ_ConformanceResult
            ++ gmd:specification/gmd:CI_Citation
    """

    title: str
    date: str
    # dateType
    publication: bool
    # max 1, spatial data should report date of last revision
    revision: bool
    # max 1
    creation: bool


@dataclass
class InspireResourceTypeTemplate:
    """
    dataset, dataset series

    /gmd:MD_Metadata/gmd:hierarchyLevel/gmd:MD_ScopeCode
    CODELISTVALUE: dataset / series
    """

    scope_code: str


@dataclass
class InspireIdentificationInfoTemplate:
    """
    gmd:MD_Metadata

    Must be added to to the first gmd:MD_DataIdentification as only one
    element should be present.

    Meaning this section will be added to the exsiting section
    above where citation is also part of?????

    gmd:identificationInfo/MD_DataIdentification

    && gmd:citation/gmd:CI_Citation/gmd:identifier/gmd:MD_Identifier
        ++ /gmd:code

    && gmd:descriptiveKeywords/gmd:MD_Keywords
        ++ gmd:thesaurusName/gmd:CI_Citation/gmd:title #
        with GEMET- INSPIRE themes, version 1.0

    && gmd:spatialResolution/gmd:MD_Resolution/gmd:equivalentScale/gmd:MD_RepresentativeFraction/gmd:denominator/gco:Integer # noqa
    && gmd:spatialResolution/gmd:MD_Resolution/gmd:distance/gco:Distance

    && gmd:language/gmd:LanguageCode

    && gmd:topicCategory/gmd:MD_TopicCategoryCode
    """

    code: str
    keyword: str
    integer: float
    distance: float
    language_code: str
    topic_category_code: str


@dataclass
class InspireDistributionInfoTemplate:
    """
    gmd:distributionInfo/gmd:MD_Distribution

    && gmd:transferOptions/gmd:MD_DigitalTransferOptions/gmd:onLine/gmd:CI_OnlineResource/gmd:linkage/gmd:URL # noqa

    """

    url: str


@dataclass
class InspireDataqualityTemplate:
    """
    gmd:dataQualityInfo/gmd:DQ_DataQuality

    && gmd:scope/gmd:DQ_Scope/gmd:level/gmd:MD_ScopeCode

    && gmd:report/gmd:DQ_DomainConsistency/gmd:result/gmd:DQ_ConformanceResult

    && gmd:lineage/gmd:LI_Lineage/gmd:statement
    """

    # gmd:CI_Citation
    title: str  # use Anchor element with  xlink:href=
    date: str
    # CI_DateTypeCode & codeListValue= publication / revision / creation
    publication: bool
    revision: bool
    creation: bool

    linage_statement: str


@dataclass
class InspireDistributionTemplate:
    """ """

    resource_type = InspireResourceTypeTemplate
    identification_info = InspireIdentificationInfoTemplate
