# What is the metaRegister module

As each run first needs to collect all metadata documents that are used in the ETL processes this module offers functionality to collect these resources. I focuses on the etl process name and the metadata document storage path and stores this information for each process as a tuple inside of a list so other python code can easily process this structure.

Since it was not clear where the metadata documents are stored this module is intended to theoretically also store metadata as json files. This functionality is not yet implemented and becomes obsolete a we agreed on using a database / CKAN to store the metadata.
