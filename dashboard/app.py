import streamlit as st

# ==================================================
# PAGE CONFIG
# ==================================================

st.set_page_config(
    page_title="Lunar Ice Detection System",
    page_icon="🌕",
    layout="wide"
)

# ==================================================
# HEADER
# ==================================================

st.title("🌕 Lunar Ice Detection System")

st.subheader(
    "Detection and Characterization of Subsurface Lunar Ice "
    "Using Chandrayaan-2 DFSAR"
)

st.markdown("---")

# ==================================================
# PROJECT INFO
# ==================================================

col1, col2 = st.columns(2)

with col1:
    st.info(
        """
        **Mission:** Chandrayaan-2
        
        **Instrument:** DFSAR
        
        **Target Region:** Lunar South Pole
        
        **Objective:** Detect and quantify subsurface water ice
        """
    )

with col2:
    st.success(
        """
        **Status:** Development
        
        **Version:** 1.0
        
        **Modules:** 18
        
        **Pipeline:** Active
        """
    )

st.markdown("---")

# ==================================================
# MODULE STATUS
# ==================================================

st.header("Pipeline Status")

modules = [
    ("M01", "Scientific Data Acquisition Engine", True),
    ("M02", "Radiometric Calibration Engine", False),
    ("M03", "Permanent Shadow Analysis Engine", False),
    ("M04", "Polarimetric Feature Extraction Engine", False),
    ("M05", "Scattering Mechanism Analysis Engine", False),
    ("M06", "Depth Zone Analysis Engine", False),
    ("M07", "Thermal Stability Analysis Engine", False),
    ("M08", "Ice Origin Classification Engine", False),
    ("M09", "Ice Concentration Estimation Engine", False),
    ("M10", "Bayesian Fusion Engine", False),
    ("M11", "Volumetric Ice Estimation Engine", False),
    ("M12", "Uncertainty Quantification Engine", False),
    ("M13", "Scientific Validation Engine", False),
    ("M14", "Visualization Engine", False),
    ("M15", "Interactive Dashboard Engine", False),
    ("M16", "Scientific Report Generator", False),
    ("M17", "Export Engine", False),
    ("M18", "Mission Pipeline Orchestrator", False),
]

for code, name, status in modules:

    if status:
        st.success(f"✅ {code} — {name}")

    else:
        st.warning(f"⬜ {code} — {name}")

# ==================================================
# SYSTEM STATUS
# ==================================================

st.markdown("---")

st.header("System Status")

st.success("System Ready")

st.info(
    """
    Current Capability:

    • Parse DFSAR PDS4 XML

    • Create DFSAR Dataset Objects

    • Validate Mission Metadata

    • Manage Configuration System
    """
)