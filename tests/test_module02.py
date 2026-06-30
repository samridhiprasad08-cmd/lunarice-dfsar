import numpy as np
from src.modules.m02_preprocessing import RadiometricPreprocessing


def test_digital_number_to_power():
    module = RadiometricPreprocessing()
    dn = np.array([1, 2, 3])
    power = module.digital_number_to_power(dn)

    assert np.allclose(power, np.array([1, 4, 9]))


def test_noise_removal():
    module = RadiometricPreprocessing()
    power = np.array([1.0, 5.0, 10.0])
    corrected = module.remove_noise(power, noise_floor=3.0)

    assert np.allclose(corrected, np.array([0.0, 2.0, 7.0]))


def test_incidence_angle_correction():
    module = RadiometricPreprocessing()
    power = np.array([1.0])
    sigma0 = module.incidence_angle_correction(power, 30)

    assert np.allclose(sigma0, np.array([2.0]))