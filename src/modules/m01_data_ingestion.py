"""
==========================================================
MODULE 01
Scientific Data Ingestion Engine
==========================================================

Reads:

• DFSAR XML Metadata
• DFSAR Binary Radar File

Outputs:

DFSARDataset object

==========================================================
"""

from pathlib import Path

from src.core.base_module import BaseModule
from src.models.dataset import DFSARDataset
from src.utils.logger import logger
from src.utils.pds_parser import PDSParser


class DataIngestion(BaseModule):

    def __init__(self):
        super().__init__("Module 01 : Data Ingestion")

    # =====================================================
    # Check whether required files exist
    # =====================================================

    def validate_files(self, xml_file: str, data_file: str):

        logger.info("Checking input files...")

        xml_path = Path(xml_file)
        data_path = Path(data_file)

        if not xml_path.exists():
            raise FileNotFoundError(f"XML file not found: {xml_file}")

        if not data_path.exists():
            raise FileNotFoundError(f"Radar file not found: {data_file}")

        logger.info("Input files verified successfully.")

    # =====================================================
    # Read XML and create dataset
    # =====================================================

    def load_dataset(self, xml_file: str, data_file: str):

        logger.info("Reading PDS4 XML...")

        parser = PDSParser(xml_file)

        metadata = parser.extract_metadata()

        logger.info("Metadata extracted successfully.")

        dataset = DFSARDataset()

        dataset.mission = "Chandrayaan-2"

        dataset.instrument = "DFSAR"

        dataset.product_type = metadata.get("product_type", "")

        dataset.frequency_band = metadata.get("frequency_band", "")

        dataset.polarization = metadata.get("polarization", "Unknown")

        dataset.orbit_number = int(metadata.get("orbit_number", 0))

        dataset.acquisition_time = metadata.get("scene_start_time", "")

        dataset.incidence_angle = float(metadata.get("incidence_angle", 0))

        dataset.look_direction = metadata.get("look_direction", "")

        dataset.spacecraft_altitude = float(
            metadata.get("spacecraft_altitude", 0)
        )

        dataset.center_latitude = float(
            metadata.get("centre_latitude", 0)
        )

        dataset.center_longitude = float(
            metadata.get("centre_longitude", 0)
        )

        dataset.xml_path = Path(xml_file)

        dataset.data_path = Path(data_file)

        dataset.metadata = metadata

        dataset.mark_loaded()

        logger.info("Dataset object created successfully.")

        return dataset

    # =====================================================
    # Print Summary
    # =====================================================

    def print_dataset_summary(self, dataset):

        dataset.summary()

    # =====================================================
    # Main Module Execution
    # =====================================================

    def run(self, xml_file=None, data_file=None):

        logger.info("===================================")
        logger.info("MODULE 01 : DATA INGESTION STARTED")
        logger.info("===================================")

        if xml_file is None or data_file is None:

            logger.warning(
                "No dataset supplied."
            )

            logger.info(
                "Module initialized successfully."
            )

            return None

        self.validate_files(xml_file, data_file)

        dataset = self.load_dataset(
            xml_file,
            data_file
        )

        dataset.validate()

        self.print_dataset_summary(dataset)

        logger.info("Module 01 completed successfully.")

        return dataset