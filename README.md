# ConceptMeta

A Python library and CLI tool to manage metadata for data distributions using the INSPIRE metadata profile.

## State

Currently under construction, expect breaking changes. Usage as python library is implemented the CLI functionality is not yet available.

The goal is to be able to generate INSPIRE dataset/series metadata as well as service metadata based on the config file/s in `src/config/config.yml`. The config file will hold metadata information based on user input for a single dataset.

You can find pre-generated examples for the outputs in the `output` directory.

## Installation

Clone this repository.

Generate INSPIRE metadata using the custom implementation in conceptMeta:

- Setup a python environment `python -m venv .venv`
- Activate env `source env/bin/activate`
- Install the tool uv `pip install uv`
- Install the project dependency in the python environment `uv sync`

## Usage

- Edit the `src/config/config.yml` file according to your needs

`uv run src/conceptMeta.py`

For pygeometa:

- Edit the `src/config/pygeometa.yml` file according to your needs

`uv run pygeometa metadata generate src/config/pygeometa.yml --schema=iso19139`

For both approaches the results will be saved to the output directory. You can change this behavior in `src/settings.py`

## Technology

- Python
- [lxml](https://lxml.de/): To process xml data in Python
- [pygeometa](https://github.com/geopython/pygeometa): Similar to conceptMeta - a tool to generate metadata documents based on config files, supports ISO 19139 but not fully supports INSPIRE

Not implemented:

- [INSPIRE validation service](https://inspire.ec.europa.eu/validator/home/index.html) (WebAPI)
