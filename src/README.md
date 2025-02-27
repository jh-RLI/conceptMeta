# ConceptMeta

Use `conceptMeta.py` to run setup.

Find configurations to edit the metadata outputs in the `config` directory

Find the implementation of the INSPIRE TG for datasets and dataset series in `inspire/createNewDatasetSeries.py` and for services in `inspire/createNewDatasetService.py`

The `metaRegister` is used to manage multiple dataset-metadata specifications in the config directory. Users can describe multiple datasets in multiple config files.

The `xmlWrap` is simple wrapper for xml paring functionality.

The `validation` is used to implement any validation of the generated results. It is not setup yet but it is planned to integrate the official INSPIRE metadata validation service.
