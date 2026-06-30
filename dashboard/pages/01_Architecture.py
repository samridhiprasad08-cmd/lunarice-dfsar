import streamlit as st

st.set_page_config(page_title="Architecture", page_icon="🏗", layout="wide")

st.title("🏗 Complete System Architecture")

st.markdown("""
This architecture integrates radar, optical, terrain and thermal evidence into a complete
lunar ice characterization and mission-planning pipeline.
""")

c1, c2, c3, c4, c5 = st.columns(5)
c1.metric("Modules", "18")
c2.metric("Data Sources", "4+")
c3.metric("Papers", "4")
c4.metric("Outputs", "5")
c5.metric("Core Method", "Bayesian Fusion")

st.markdown("## Simplified Evidence Fusion Flow")

st.graphviz_chart("""
digraph {
    rankdir=LR;
    graph [bgcolor="transparent"];
    node [shape=box, style="rounded,filled", fontname="Arial", fontsize=12,
          fillcolor="#0f172a", fontcolor="white", color="#38bdf8"];
    edge [color="#93c5fd", penwidth=2];

    DFSAR [label="DFSAR\\nRadar Polarimetry"];
    OHRC [label="OHRC\\nTerrain + Boulders"];
    DEM [label="DEM / TMC\\nSlope + Shadow"];
    DIV [label="Diviner\\nTemperature"];
    FUSION [label="Bayesian Fusion\\nP(Ice | Evidence)", fillcolor="#312e81", color="#a78bfa"];
    OUT [label="Mission Products\\nIce Map + Volume + Landing + Rover Path", fillcolor="#064e3b", color="#34d399"];

    DFSAR -> FUSION;
    OHRC -> FUSION;
    DEM -> FUSION;
    DIV -> FUSION;
    FUSION -> OUT;
}
""")

st.markdown("## Full Architecture Diagram")

with st.expander("View architecture diagram", expanded=True):
    st.image(
        "dashboard/assets/system_architecture.png",
        caption="Complete 18-module LunarIce-DFSAR architecture",
        use_container_width=True
    )

st.markdown("## Data Source Layer")

st.table({
    "Dataset": ["DFSAR", "OHRC", "DEM/TMC", "Diviner", "Mini-RF / LCROSS"],
    "Role": [
        "Radar polarimetry, CPR, DOP, subsurface scattering",
        "Surface morphology, boulder detection, terrain texture",
        "Elevation, slope, aspect, shadow geometry",
        "Temperature and thermal stability constraints",
        "Validation and benchmark comparison"
    ],
    "Used In": [
        "M02, M04, M05, M06, M10",
        "M03, M14, landing site planning",
        "M03, M06, rover traverse",
        "M07, M10, M11",
        "M13"
    ]
})

st.markdown("## Why This Architecture Is Strong")

st.success("""
High CPR alone can be caused by rough terrain, blocky ejecta or true volume scattering.
Our architecture reduces false positives by combining radar polarimetry, shadow condition,
thermal stability, terrain safety and validation evidence.
""")