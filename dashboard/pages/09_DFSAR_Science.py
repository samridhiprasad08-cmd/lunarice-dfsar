import streamlit as st

st.set_page_config(
    page_title="DFSAR Science",
    page_icon="🌕",
    layout="wide"
)

st.title("DFSAR Science and Radar Processing")

st.markdown("""
The Dual Frequency Synthetic Aperture Radar (DFSAR) onboard Chandrayaan-2 is the primary
radar dataset for this framework. Unlike optical sensors, radar can actively illuminate
permanently shadowed lunar regions and provide information about surface and possible
subsurface scattering behavior.
""")

st.image(
    "dashboard/assets/dfsar_pipeline.png",
    caption="DFSAR processing pipeline from raw SAR data to CPR/DOP ice indicators",
    use_container_width=True
)

st.markdown("## Why DFSAR Is Central to This Project")

st.markdown("""
Permanently shadowed regions cannot be studied reliably using optical images alone because
they receive little or no direct sunlight. DFSAR solves this problem by transmitting radar
pulses and measuring the returned signal.

Radar is useful because:

- It provides its own illumination.
- It can operate in shadowed polar terrain.
- It is sensitive to surface roughness, dielectric properties and scattering structure.
- Dual-frequency observations help distinguish shallow and deeper responses.
- Polarimetric information helps separate rough terrain from possible volume scattering.
""")

st.markdown("## L-Band and S-Band Scientific Role")

st.table({
    "Band": ["L-band", "S-band"],
    "Approximate Role": [
        "Longer wavelength; more sensitive to deeper/subsurface scattering",
        "Shorter wavelength; more sensitive to shallow surface and near-surface scattering"
    ],
    "Use in Framework": [
        "Detect possible buried or deeper ice-related radar response",
        "Compare with L-band to classify shallow vs deeper scattering zones"
    ]
})

st.markdown("## Radar Processing Chain")

st.code("""
Raw DFSAR SAR Data
        ↓
Radiometric Calibration
        ↓
Noise Removal and Speckle Reduction
        ↓
Polarimetric Channel Preparation
        ↓
Stokes Parameter Generation
        ↓
CPR, DOP, Phase and Ellipticity Products
        ↓
Polarimetric Decomposition
        ↓
Ice Evidence Layers for Bayesian Fusion
""")

st.markdown("## Circular Polarization Ratio")

st.markdown("""
Circular Polarization Ratio is one of the most commonly used radar indicators for possible
lunar ice. High CPR may indicate multiple scattering or coherent backscatter from low-loss
media such as ice-bearing regolith.

However, CPR is not unique to ice. Rough blocky terrain, crater ejecta and wavelength-scale
surface roughness can also produce high CPR. Therefore, CPR is treated as only one evidence
stream, not as a final decision.
""")

st.latex(r"""
CPR =
\frac{
\sigma_{SC}
}
{
\sigma_{OC}
}
""")

st.markdown("""
Where:

- \(\\sigma_{SC}\) = same-circular polarization return
- \(\\sigma_{OC}\) = opposite-circular polarization return
""")

st.markdown("## Degree of Polarization")

st.markdown("""
Degree of Polarization helps determine how ordered or depolarized the radar return is.
Ice-like volume scattering can reduce polarization coherence, while deterministic rough
surface scattering may preserve stronger polarization structure.
""")

st.latex(r"""
DOP =
\frac{
\sqrt{S_2^2 + S_3^2 + S_4^2}
}
{S_1}
""")

st.markdown("## Why CPR Alone Is Not Enough")

st.warning("""
A CPR-only pipeline can confuse rough crater walls with ice-bearing material.
This is why the proposed framework also includes DOP, Stokes parameters, scattering
decomposition, PSR confirmation, thermal stability and Bayesian fusion.
""")

st.markdown("## DFSAR Outputs Used by Later Modules")

st.table({
    "Output": [
        "Calibrated radar image",
        "CPR map",
        "DOP map",
        "Stokes parameters",
        "Scattering decomposition",
        "L/S-band comparison"
    ],
    "Used By": [
        "M04, M05",
        "M09, M10",
        "M05, M10",
        "M04, M05",
        "M08, M10",
        "M06, M11"
    ],
    "Scientific Purpose": [
        "Base radar product",
        "Ice-sensitive radar anomaly",
        "False-positive reduction",
        "Polarization state representation",
        "Surface/volume/double-bounce separation",
        "Depth-zone interpretation"
    ]
})

st.markdown("---")
st.caption("LunarIce-DFSAR | DFSAR radar science and polarimetric processing framework")