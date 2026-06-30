"""
Module 02: Radiometric Calibration and Preprocessing Engine

Purpose:
Convert raw radar intensity values into calibrated radar backscatter
products that can later be used for CPR, DOP, Stokes parameters,
and polarimetric decomposition.
"""

import numpy as np

from src.core.base_module import BaseModule
from src.utils.logger import logger


class RadiometricPreprocessing(BaseModule):
    def __init__(self):
        super().__init__("Module 02 : Radiometric Calibration and Preprocessing")

    def validate_input(self):
        logger.info("Validating radar input for preprocessing...")

    def digital_number_to_power(self, dn_array):
        """
        Convert digital number values to radar power.

        Power = |DN|²
        """
        return np.abs(dn_array) ** 2

    def remove_noise(self, power_array, noise_floor=0.0):
        """
        Remove estimated receiver/system noise.
        """
        corrected = power_array - noise_floor
        corrected[corrected < 0] = 0
        return corrected

    def incidence_angle_correction(self, power_array, incidence_angle_deg):
        """
        Convert beta-naught-like power to sigma-naught approximation.

        sigma0 = power / sin(theta)
        """
        theta = np.deg2rad(incidence_angle_deg)
        return power_array / np.sin(theta)

    def process(self):
        logger.info("Radiometric preprocessing module is ready.")

    def validate_output(self):
        logger.info("Validating calibrated output...")

    def save_results(self):
        logger.info("Module 02 preprocessing outputs saved.")