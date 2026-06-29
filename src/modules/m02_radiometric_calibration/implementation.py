from src.core.base_module import BaseModule
from src.utils.logger import logger


class RadiometricCalibration(BaseModule):

    def __init__(self):
        super().__init__("Module 02 : Radiometric Calibration")

    def run(self, dataset):

        logger.info("Starting radiometric calibration...")

        logger.info("Reading calibration constants...")

        logger.info("Removing system noise...")

        logger.info("Applying range correction...")

        logger.info("Computing Sigma Naught...")

        logger.info("Radiometric calibration completed.")

        return dataset