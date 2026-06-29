"""
=========================================================
SCIENTIFIC CONSTANTS

Lunar Ice Detection Framework

All physical constants used throughout the project.

References

Apollo Sample Database

Schorghofer & Taylor (2007)

Campbell et al. (2006)

Nozette et al. (2010)

Colaprete et al. (2010)

=========================================================
"""

import numpy as np

# =====================================================
# UNIVERSAL CONSTANTS
# =====================================================

PI = np.pi

SPEED_OF_LIGHT = 299792458.0          # m/s

BOLTZMANN = 1.380649e-23              # J/K

STEFAN_BOLTZMANN = 5.670374419e-8     # W/m²/K⁴

GRAVITATIONAL_CONSTANT = 6.67430e-11

# =====================================================
# MOON PARAMETERS
# =====================================================

MOON_RADIUS = 1737400.0               # metres

MOON_GRAVITY = 1.62                   # m/s²

MOON_ESCAPE_VELOCITY = 2380           # m/s

# =====================================================
# RADAR PARAMETERS
# =====================================================

L_BAND_FREQUENCY = 1.25e9

S_BAND_FREQUENCY = 2.50e9

L_BAND_WAVELENGTH = SPEED_OF_LIGHT / L_BAND_FREQUENCY

S_BAND_WAVELENGTH = SPEED_OF_LIGHT / S_BAND_FREQUENCY

# =====================================================
# MATERIAL PROPERTIES
# =====================================================

RHO_ICE = 917.0

RHO_REGOLITH = 1800.0

RHO_MIXTURE = 1200.0

# =====================================================
# DIELECTRIC CONSTANTS
# =====================================================

EPSILON_ICE = 3.15

EPSILON_REGOLITH = 2.70

LOSS_TANGENT = 0.005

# =====================================================
# CPR MODEL
# =====================================================

CPR_BACKGROUND = 0.30

CPR_THRESHOLD = 1.00

K_CBOE = 2.10

# =====================================================
# DOP
# =====================================================

DOP_THRESHOLD = 0.13

# =====================================================
# BAYESIAN MODEL
# =====================================================

ICE_PROBABILITY_THRESHOLD = 0.50

# =====================================================
# SCHORGHOFER MODEL
# =====================================================

THERMAL_GRAIN_SIZE = 50e-6

MAX_STABLE_DEPTH = 5.0

# =====================================================
# PIXEL PARAMETERS
# =====================================================

PIXEL_SIZE = 75

PIXEL_AREA = PIXEL_SIZE * PIXEL_SIZE

# =====================================================
# MONTE CARLO
# =====================================================

N_MONTE_CARLO = 10000

# =====================================================
# UNCERTAINTIES
# =====================================================

SIGMA_CPR = 0.30

SIGMA_DEPTH = 0.20

SIGMA_DENSITY = 0.15

SIGMA_AREA = 0.10