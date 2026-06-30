import streamlit as st

st.set_page_config(page_title="Research Papers", layout="wide")

st.title("Research Paper Integration")

papers = [
    {
        "title": "Schorghofer & Taylor (2007)",
        "focus": "Subsurface migration of H2O at lunar cold traps",
        "contribution": "Thermal stability, sublimation, residence time, subsurface migration pathways.",
        "modules": "M07, M09, M11, M12",
        "why": "Provides the physics for deciding whether radar-detected ice is thermally stable."
    },
    {
        "title": "Kumari & Bhardwaj (2021)",
        "focus": "Polarimetric Mini-SAR and Mini-RF datasets for lunar surface characterization",
        "contribution": "Stokes parameters, DOP, relative phase, Poincare ellipticity, m-delta and m-chi decomposition.",
        "modules": "M04, M05, M08",
        "why": "Provides polarimetric formulas and decomposition logic for scattering interpretation."
    },
    {
        "title": "Nozette et al. (2010)",
        "focus": "LRO Mini-RF technology demonstration",
        "contribution": "Hybrid polarimetry, CPR ambiguity, volume scattering, coherent backscatter opposition effect.",
        "modules": "M05, M06, M10, M13",
        "why": "Justifies why CPR alone is not enough and why multi-evidence fusion is required."
    },
    {
        "title": "Colaprete et al. (2010)",
        "focus": "Detection of water in the LCROSS ejecta plume",
        "contribution": "Ground-truth detection of water at Cabeus with 5.6 ± 2.9 wt% abundance.",
        "modules": "M09, M11, M13",
        "why": "Provides the strongest validation benchmark for lunar polar water ice concentration."
    }
]

for p in papers:
    with st.container():
        st.markdown(f"## {p['title']}")
        st.markdown(f"**Focus:** {p['focus']}")
        st.markdown(f"**Contribution:** {p['contribution']}")
        st.markdown(f"**Modules Used In:** {p['modules']}")
        st.info(p["why"])
        st.markdown("---")