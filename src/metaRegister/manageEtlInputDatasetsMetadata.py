"""
Register all dataset distributions that are part of the current run.
This module helps to manage the available data and related metadata.
Distributions relate to a file resource that is part of the ETL process.
It must be determined if metadata is available or not.

Note: To determine the metadata availability an automated approach should be
used if possible
"""

from pathlib import Path

from settings import BASE_PATH, ETL_PROCESSES


def collect_metadata_path_for_etl_processes(
    processes: list = ETL_PROCESSES,
) -> set[tuple[str, Path]]:
    """
    Collects the metadata paths for all ETL processes.

    Args:
        processes (list): List of ETL process configurations.

    Returns:
        set[tuple[str, Path]]: Set of tuples containing
        process ID and metadata file path.
    """
    meta_file_paths = set()
    for process_config in processes:
        # read the process name
        etl_process_id = process_config["process_id"]

        # Combine metadata_storage_path and metadata_document_name
        metadata_file_path: str = (
            f"{process_config['metadata_storage_path']}"
            f"{process_config['metadata_document_name']}.xml"
        )

        meta_file_paths.add((etl_process_id, Path(BASE_PATH / metadata_file_path)))

    return meta_file_paths


def collect_inspire_metadata_input(config: dict) -> dict:
    inspire_metadata_info = config["inspire_metadata_info"]
    return inspire_metadata_info
