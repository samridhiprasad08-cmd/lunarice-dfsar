"""
====================================================
GLOBAL CONFIGURATION

Lunar Ice Detection Framework

Author:
Team _______

ISRO Bharatiya Antariksh Hackathon

====================================================
"""

from pathlib import Path

# --------------------------------------------------
# Project Directories
# --------------------------------------------------

PROJECT_ROOT = Path(__file__).parent

DATA_DIR = PROJECT_ROOT / "data"

RAW_DATA = DATA_DIR / "raw"

PROCESSED_DATA = DATA_DIR / "processed"

EXTERNAL_DATA = DATA_DIR / "external"

OUTPUT_DATA = DATA_DIR / "outputs"

FIGURE_DIR = PROJECT_ROOT / "figures"

DOCUMENTATION = PROJECT_ROOT / "docs"

# --------------------------------------------------
# Radar Parameters
# --------------------------------------------------

L_BAND_FREQ = 1.25e9

S_BAND_FREQ = 2.5e9

SPEED_OF_LIGHT = 299792458

L_BAND_WAVELENGTH = SPEED_OF_LIGHT / L_BAND_FREQ

S_BAND_WAVELENGTH = SPEED_OF_LIGHT / S_BAND_FREQ

# --------------------------------------------------
# Pixel Resolution
# --------------------------------------------------

PIXEL_SIZE = 75

PIXEL_AREA = PIXEL_SIZE ** 2

# --------------------------------------------------
# Ice Detection Thresholds
# --------------------------------------------------

CPR_THRESHOLD = 1.0

DOP_THRESHOLD = 0.13

P_ICE_THRESHOLD = 0.50

# --------------------------------------------------
# Monte Carlo
# --------------------------------------------------

MC_SIMULATIONS = 10000

RANDOM_SEED = 42