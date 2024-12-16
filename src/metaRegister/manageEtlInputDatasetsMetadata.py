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
    META_FILE_PATHS = set()
    for process_config in processes:
        # read the process name
        etl_process_id = process_config["process_id"]

        # Combine metadata_storage_path and metadata_document_name
        metadata_file_path: str = (
            f"{process_config['metadata_storage_path']}"
            f"{process_config['metadata_document_name']}.xml"
        )

        META_FILE_PATHS.add((etl_process_id, Path(BASE_PATH / metadata_file_path)))

    return META_FILE_PATHS


def etl_processes_collection_metadata():
    pass
