from src.core.base_module import BaseModule
from src.utils.logger import logger


class PermanentShadowAnalysis(BaseModule):

    def __init__(self):
        super().__init__(
            "Module 03 : Permanent Shadow Analysis Engine"
        )

    def validate_input(self):
        logger.info("Validating DEM inputs...")

    def process(self):
        logger.info("Generating shadow maps...")

    def validate_output(self):
        logger.info("Validating PSR products...")

    def save_results(self):
        logger.info("Saving PSR outputs...")