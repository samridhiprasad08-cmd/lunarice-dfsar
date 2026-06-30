import streamlit as st

st.set_page_config(page_title="Project Novelty", layout="wide")

st.title("Why Our Solution Is Different")

st.markdown("""
Most lunar ice detection approaches stop at radar anomaly detection.  
Our framework converts radar observations into a complete **exploration-planning pipeline**.
""")

st.markdown("## Comparison With Typical Approaches")

st.table({
    "Feature": [
        "Radar analysis",
        "Ice detection",
        "Thermal physics",
        "Terrain safety",
        "Uncertainty",
        "Validation",
        "Mission planning",
        "Final output"
    ],
    "Typical Solution": [
        "CPR threshold only",
        "Binary ice / no ice",
        "Often ignored",
        "Not integrated",
        "Not reported",
        "Limited comparison",
        "Not included",
        "Ice candidate map"
    ],
    "Our Framework": [
        "CPR + DOP + Stokes + decomposition",
        "Probability-based ice characterization",
        "Schorghofer thermal stability model",
        "OHRC + DEM slope and boulder analysis",
        "Monte Carlo confidence intervals",
        "LCROSS + Mini-RF + Diviner validation",
        "Landing site + rover traverse planning",
        "Mission-ready exploration products"
    ]
})

st.markdown("## Core Innovations")

c1, c2, c3 = st.columns(3)

with c1:
    st.success("""
    **Multi-Modal Fusion**
    
    DFSAR, OHRC, DEM/TMC, Diviner and validation data are combined instead of relying on radar alone.
    """)

with c2:
    st.info("""
    **Physics-Grounded Depth Model**
    
    Ice depth is constrained using radar penetration and thermal stability instead of assuming a flat 5 m depth everywhere.
    """)

with c3:
    st.warning("""
    **Exploration Planning**
    
    The system outputs landing zones and rover paths, not just scientific maps.
    """)

st.markdown("## Why This Helps ISRO")

st.markdown("""
This framework supports both **science** and **mission design**.

It helps answer:

- Where is ice most likely present?
- Is the signal really ice or rough terrain?
- Is the ice thermally stable?
- How much ice may be accessible?
- Where should a lander go?
- How should a rover reach the target safely?
""")

st.success("""
The novelty is not one single algorithm.  
The novelty is the complete chain from **remote sensing evidence → physics-based validation → probability map → mission planning output**.
""")