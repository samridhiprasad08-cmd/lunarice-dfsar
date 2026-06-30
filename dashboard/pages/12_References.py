import streamlit as st

st.set_page_config(
    page_title="References",
    page_icon="🌕",
    layout="wide"
)

st.title("Scientific References")

st.markdown("""
The proposed framework is built upon peer-reviewed research, Chandrayaan-2 instrument
documentation and lunar polar exploration studies.
""")

st.markdown("## Core Research Papers")

st.table({
    "Paper": [
        "Schorghofer & Taylor (2007)",
        "Kumari & Bhardwaj (2021)",
        "Nozette et al. (2010)",
        "Colaprete et al. (2010)"
    ],
    "Primary Contribution": [
        "Thermal stability and subsurface migration of lunar water",
        "Polarimetric analysis using Stokes parameters and decomposition",
        "Mini-RF radar interpretation and CPR limitations",
        "LCROSS water detection and concentration estimates"
    ],
    "Modules Used": [
        "M07, M09, M11, M12",
        "M04, M05, M08",
        "M05, M06, M10, M13",
        "M09, M11, M13"
    ]
})

st.markdown("---")

st.markdown("## Reference 1")

st.markdown("""
**Schorghofer, N., & Taylor, G. J. (2007)**

Subsurface migration of H₂O at lunar cold traps.

### Used In

- Thermal Stability Modeling
- Ice Preservation Analysis
- Volumetric Estimation

### Contribution

Provides the physical basis for understanding how water molecules migrate,
accumulate and survive in permanently shadowed lunar environments.
""")

st.markdown("---")

st.markdown("## Reference 2")

st.markdown("""
**Kumari, N., & Bhardwaj, A. (2021)**

Polarimetric analysis of lunar radar observations.

### Used In

- Stokes Parameters
- Degree of Polarization
- Polarimetric Decomposition

### Contribution

Provides the polarimetric framework used to characterize scattering behaviour
and distinguish surface from volume scattering.
""")

st.markdown("---")

st.markdown("## Reference 3")

st.markdown("""
**Nozette et al. (2010)**

Mini-RF Technology Demonstration.

### Used In

- CPR interpretation
- Volume scattering analysis
- False-positive reduction

### Contribution

Demonstrates why CPR alone is insufficient for identifying lunar ice.
""")

st.markdown("---")

st.markdown("## Reference 4")

st.markdown("""
**Colaprete et al. (2010)**

Detection of Water in the LCROSS Ejecta Plume.

### Used In

- Concentration estimation
- Validation framework
- Ice abundance calibration

### Contribution

Provides one of the strongest direct observations of lunar polar water.
""")

st.markdown("---")

st.markdown("## Research-to-Module Mapping")

st.table({
    "Module": [
        "M04",
        "M05",
        "M06",
        "M07",
        "M09",
        "M10",
        "M11",
        "M13"
    ],
    "Primary Literature Source": [
        "Kumari & Bhardwaj",
        "Kumari & Bhardwaj, Nozette",
        "Nozette",
        "Schorghofer & Taylor",
        "Colaprete",
        "All four papers",
        "Schorghofer + Colaprete",
        "Nozette + Colaprete"
    ]
})

st.success("""
All major scientific modules are grounded in peer-reviewed literature rather than
ad-hoc assumptions.
""")

st.caption("LunarIce-DFSAR | Scientific Literature and Reference Framework")
