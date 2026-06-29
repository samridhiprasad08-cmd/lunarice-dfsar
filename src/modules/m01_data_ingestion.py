from pathlib import Path

from src.core.base_module import BaseModule

from src.models.dataset import DFSARDataset

from src.utils.logger import logger

from src.utils.pds_parser import PDSParser


class DataIngestion(BaseModule):

    def __init__(self):

        super().__init__("Module 01 : Data Ingestion")


    def validate_files(self, xml_file, data_file):

        logger.info("Checking input files...")

        if not Path(xml_file).exists():

            raise FileNotFoundError(xml_file)

        if not Path(data_file).exists():

            raise FileNotFoundError(data_file)

        logger.info("Input files verified.")


    def load_dataset(self, xml_file, data_file):

        parser = PDSParser(xml_file)

        metadata = parser.extract_metadata()

        dataset = DFSARDataset(

            mission="Chandrayaan-2",

            instrument="DFSAR",

            frequency_band=metadata["frequency_band"],

            polarization="Unknown",

            orbit_number=int(metadata["orbit_number"]),

            acquisition_time="",

            incidence_angle=float(metadata["incidence_angle"]),

            look_direction=metadata["look_direction"],

            product_type=metadata["product_type"],

            data_path=Path(data_file),

            xml_path=Path(xml_file),

            metadata=metadata

        )

        return dataset


    def run(self):

        logger.info("Waiting for DFSAR dataset...")

        logger.info("Module ready.")
    
    def print_dataset_summary(self, dataset):

    logger.info("------------- DFSAR SUMMARY -------------")

    logger.info(f"Mission : {dataset.mission}")

    logger.info(f"Instrument : {dataset.instrument}")

    logger.info(f"Band : {dataset.frequency_band}")

    logger.info(f"Orbit : {dataset.orbit_number}")

    logger.info(f"Incidence : {dataset.incidence_angle}")

    logger.info(f"Latitude : {dataset.center_latitude}")

    logger.info(f"Longitude : {dataset.center_longitude}")

    logger.info("-----------------------------------------")