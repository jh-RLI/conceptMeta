# What is config used for

This module is used to collect user inputs. It is not fully functional but can already be used to provide specific input information to create a new INSPIRE metadata document.

The config YAML files provide a structured way to document all ETL processes or resources that will be included in the next "run" of conceptMeta Program.
For Each ETL process included you can add information that relates specifically to one process. There you can specific things like the name of a dataset and the path to existing metadata and more.

## conceptMeta vs pygeometa

Two variants of YAML files that can be used to provide metadata information which will be added to the generated metadata documents.

config.yml

Used by conceptMeta to generate INSPIRE metadata. But the implementation status is work in progress.

pygeometa.yml

Used to configure the external package pygeometa which can generate ISO 19139 xml metadata documents.
