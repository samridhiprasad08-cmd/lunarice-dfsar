Module 2 – Radiometric Calibration
Objective

Convert raw DFSAR digital numbers into physically meaningful radar backscatter values suitable for quantitative lunar surface analysis.

Scientific Motivation

Radar echoes received by Chandrayaan-2 DFSAR are influenced by:

Instrument gain
Receiver noise
Antenna characteristics
Propagation loss
Range spreading

Directly using raw digital numbers would produce misleading CPR values and incorrect polarimetric decomposition.

Radiometric calibration standardizes the radar response so that measurements from different acquisitions can be compared quantitatively.

Inputs
Raw DFSAR binary data
XML metadata
Calibration constants
Outputs
Sigma Naught (σ⁰)
Beta Naught (β⁰)
Gamma Naught (γ⁰)

These calibrated products are forwarded to Module 3.