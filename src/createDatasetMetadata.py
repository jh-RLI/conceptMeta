# Minimal metadata according to https://pro.arcgis.com/de/pro-app/latest/help/metadata/create-iso-19115-and-iso-19139-metadata.htm # noqa E501
# MD_DataIdentification.citation.CI_Citation.title
# MD_DataIdentification.abstract
# MD_DataIdentification.extent.EX_Extent.geographicElement.EX_GeographicBoundingBox
# MD_DataIdentification.topicCategory
# MD_DataIdentification.citation.CI_Citation.title
# MD_DataIdentification.citation.CI_Citation.date
# MD_Metadata.language
# MD_Metadata.hierarchyLevel # We will use datasets/data series
# MD_Metadata.hierarchyLevelName
# MD_Metadata.parentIdentifier
# MD_Metadata.contact
# MD_DataIdentification.language
# MD_DataIdentification.characterSet
# MD_DataIdentification.extent.EX_Extent.geographicElement
# EX_GeographicBoundingBox
# EX_GeographicDescription


# INSPIRE XML Schemas
# https://github.com/INSPIRE-MIF/application-schemas

# Minimal to pass the official inspire v2 validator
# <?xml version="1.0" encoding="UTF-8"?> (starting with)
# gmd:MD_Metadata (This must always be there)
# Add namespaces (they might change depending on you use case, we will use a fixed set) # noqa E501
# with -> namespaces:
#   xmlns:gmd="http://www.isotc211.org/2005/gmd"
#   xmlns:gmx="http://www.isotc211.org/2005/gmx"
#   xmlns:gml="http://www.opengis.net/gml/3.2"
#   xmlns:gco="http://www.isotc211.org/2005/gco"
#   xmlns:xlink="http://www.w3.org/1999/xlink"
#   xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
#   xmlns:srv="http://www.isotc211.org/2005/srv"
# And schema
#     xsi:schemaLocation="http://www.isotc211.org/2005/gmd http://schemas.opengis.net/csw/2.0.2/profiles/apiso/1.0.0/apiso.xsd # noqa E501
#                       http://www.isotc211.org/2005/srv http://schemas.opengis.net/iso/19119/20070417/srv/srv.xsd"> # noqa E501
# Then the content follows:
# gmd:fileIdentifier
# with:
#   gco:CharacterString
# gmd:language
# with:
#   gmd:LanguageCode codeList="http://www.loc.gov/standards/iso639-2/" codeListValue="eng" # noqa E501
# gmd:characterSet
# with:
#   gmd:MD_CharacterSetCode codeListValue="utf8" codeList="http://standards.iso.org/iso/19139/resources/gmxCodelists.xml#MD_CharacterSetCode">UTF-8</gmd:MD_CharacterSetCode # noqa E501
# gmd:hierarchyLevel
# with:
#   gmd:MD_ScopeCode codeList="http://www.isotc211.org/2005/resources/codeList.xml#MD_ScopeCode" codeListValue="dataset" # noqa E501
# gmd:hierarchyLevelName
# with:
#   gco:CharacterString xmlns:gco="http://www.isotc211.org/2005/gco" # noqa E501
# gmd:contact
# with:
#   gmd:CI_ResponsibleParty
#       gmd:organisationName
#           gco:CharacterString
#       gmd:contactInfo
#           gmd:CI_Contact
#               gmd:address
#                   gmd:CI_Address
#                       gmd:electronicMailAddress
#                           gco:CharacterString
#       gmd:role
#           gmd:CI_RoleCode codeList="http://www.isotc211.org/2005/resources/codeList.xml#CI_RoleCode" codeListValue="pointOfContact"> # noqa E501
# gmd:dateStamp
# with:
#   gco:Date
# gmd:referenceSystemInfo
# with:
#   gmd:MD_ReferenceSystem
#       gmd:referenceSystemIdentifier
#           gmd:RS_Identifier
#               gmd:code
#                   gmx:Anchor xlink:href="http://www.opengis.net/def/crs/EPSG/0/4258" # noqa E501
# gmd:identificationInfo
# with:
#   gmd:MD_DataIdentification
#       gmd:citation
#           gmd:CI_Citation
#               gmd:title
#                   gco:CharacterString
#               gmd:date
#                   gmd:CI_Date
#                       gmd:date
#                           gco:Date
#                       gmd:dateType
#                           gmd:CI_DateTypeCode codeList="http://www.isotc211.org/2005/resources/codeList.xml#CI_DateTypeCode" codeListValue="publication">publication # noqa E501
#               gmd:identifier
#                   gmd:MD_Identifier
#                       gmd:code
#                           gmx:Anchor xlink:href="https://registry.gdi-de.org/id/de.nw/inspire-cpalkis" # noqa E501
#       gmd:abstract
#           gco:CharacterString
#       gmd:pointOfContact
#           gmd:CI_ResponsibleParty
#               gmd:organisationName
#                   gco:CharacterString
#               gmd:contactInfo
#                   gmd:CI_Contact
#                       gmd:address
#                           gmd:CI_Address
#                               gmd:electronicMailAddress
#                                   gco:CharacterString
#       gmd:role
#           gmd:CI_RoleCode codeList="http://www.isotc211.org/2005/resources/codeList.xml#CI_RoleCode" codeListValue="owner" # noqa E501
#   gmd:descriptiveKeywords
#       gmd:MD_Keywords
#           gmd:keyword
#               gco:CharacterString
#           gmd:thesaurusName
#               gmd:CI_Citation
#                   gmd:title
#                       gco:CharacterString
#                   gmd:date
#                       gmd:CI_Date
#                           gmd:date
#                               gco:Date
#                       gmd:dateType
#                           gmd:CI_DateTypeCode codeList="http://www.isotc211.org/2005/resources/codeList.xml#CI_DateTypeCode" codeListValue="publication" # noqa E501
