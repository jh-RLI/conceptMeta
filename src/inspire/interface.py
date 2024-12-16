from pathlib import Path

# from metaRegister.manageEtlInputDatasetsMetadata import (
#     collect_metadata_path_for_etl_processes,
# )
from xml.utils import save_metadata_document

from inspire.createDatasetSeries import create_inspire_metadata_document
from settings import BASE_PATH, ETL_PROCESSES


def register_etl_processes_and_create_metadata(processes: list = ETL_PROCESSES):
    """
    Collects all ETL processes, extracts metadata paths,
    and generates INSPIRE metadata documents.

    Args:
        processes (list): List of ETL process configurations.
    """

    metadata_register = []

    for process_config in processes:
        process_id = process_config["process_id"]
        metadata_info = {
            "dataset_name": process_config["dataset_name"],
            "metadata_storage_path": process_config["metadata_storage_path"],
            "metadata_document_name": process_config["metadata_document_name"],
        }

        # Generate the metadata XML document
        metadata_document = create_inspire_metadata_document(process_id, metadata_info)

        # Save the XML document
        metadata_path = Path(
            BASE_PATH
            / f"{process_config['metadata_storage_path']}"
            / f"{process_config['metadata_document_name']}.xml"
        )
        save_metadata_document(
            metadata_document, file_name=process_config["metadata_document_name"]
        )

        # Add to metadata register
        metadata_register.append(
            {
                "process_id": process_id,
                "metadata_file_path": str(metadata_path),
            }
        )

    return metadata_register
