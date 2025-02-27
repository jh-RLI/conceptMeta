# Results

Currently two implementations are evaluated, which outputs are listed above:

- Pygeometa (external package) can create ISO 19139 XML metadata documents based on the config file in `src/config/pygeometa.yml`.

- conceptMeta will create (See [TG-INSPIRE](https://knowledge-base.inspire.ec.europa.eu/publications/technical-guidance-implementation-inspire-dataset-and-service-metadata-based-isots-191392007_en)) but is not fully compliant so far. The output is based on `src/config/config.yml`

Note: Before i learned about tools like pygeometa i came to the conclusion that there are no libs`s which can produce INSPIRE metadata from configuration out of the box. Even Pygeometa will not produce fully schema compliant INSPIRE metadata. (See [TG-INSPIRE](https://knowledge-base.inspire.ec.europa.eu/publications/technical-guidance-implementation-inspire-dataset-and-service-metadata-based-isots-191392007_en))

## Future work

- Another required but missing output would show Inspire service metadata. The functionality is not implemented yet.
