"""
=========================================================
Pipeline Manager

Controls execution of every module
for the Lunar Ice Detection Framework.

Author:
Team __________

=========================================================
"""

import time

from src.utils.logger import logger


class Pipeline:

    def __init__(self):

        self.modules = []

    def add_module(self, module):

        self.modules.append(module)

        logger.info(f"Added {module.module_name}")

    def run(self):

        logger.info("=" * 60)
        logger.info("PIPELINE STARTED")
        logger.info("=" * 60)

        total_start = time.time()

        for module in self.modules:

            start = time.time()

            logger.info(f"Starting {module.module_name}")

            module.run()

            end = time.time()

            logger.info(
                f"{module.module_name} completed "
                f"in {end-start:.2f} seconds"
            )

        total_end = time.time()

        logger.info("=" * 60)
        logger.info("PIPELINE FINISHED")
        logger.info(
            f"Total Time : {total_end-total_start:.2f} seconds"
        )
        logger.info("=" * 60)