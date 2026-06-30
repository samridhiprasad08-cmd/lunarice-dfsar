import streamlit as st

st.set_page_config(
    page_title="LunarIce-DFSAR",
    layout="wide"
)

st.markdown("""
<style>
.stApp {
    background:
        radial-gradient(circle at top left, rgba(56,189,248,0.18), transparent 28%),
        radial-gradient(circle at bottom right, rgba(168,85,247,0.12), transparent 30%),
        linear-gradient(180deg, #020617 0%, #050b16 50%, #020617 100%);
    color: #e5f0ff;
}

h1, h2, h3 {
    color: #f8fafc;
    letter-spacing: -0.02em;
}

.hero {
    padding: 36px;
    border-radius: 28px;
    background: rgba(15, 23, 42, 0.72);
    border: 1px solid rgba(56, 189, 248, 0.45);
    box-shadow:
        0 0 35px rgba(56, 189, 248, 0.18),
        inset 0 0 30px rgba(15, 23, 42, 0.65);
    backdrop-filter: blur(18px);
    margin-bottom: 28px;
}

.card {
    padding: 22px;
    border-radius: 22px;
    background: rgba(15, 23, 42, 0.70);
    border: 1px solid rgba(148, 163, 184, 0.30);
    box-shadow: 0 8px 28px rgba(2, 6, 23, 0.45);
    backdrop-filter: blur(16px);
    margin-bottom: 18px;
}

.gold-card {
    padding: 22px;
    border-radius: 22px;
    background: rgba(30, 41, 59, 0.72);
    border: 1px solid rgba(251, 191, 36, 0.45);
    box-shadow: 0 0 24px rgba(251, 191, 36, 0.12);
    backdrop-filter: blur(16px);
    margin-bottom: 18px;
}

.small-text {
    color: #93c5fd;
    font-size: 16px;
}

[data-testid="stMetric"] {
    background: rgba(15, 23, 42, 0.72);
    border: 1px solid rgba(56, 189, 248, 0.28);
    border-radius: 18px;
    padding: 16px;
    box-shadow: 0 0 18px rgba(56, 189, 248, 0.08);
}

[data-testid="stMetricValue"] {
    color: #38bdf8;
}

[data-testid="stMetricLabel"] {
    color: #cbd5e1;
}

section[data-testid="stSidebar"] {
    background: rgba(2, 6, 23, 0.95);
    border-right: 1px solid rgba(56, 189, 248, 0.18);
}

div[data-testid="stTable"] {
    background: rgba(15, 23, 42, 0.70);
    border-radius: 18px;
    border: 1px solid rgba(148, 163, 184, 0.25);
    padding: 8px;
}

hr {
    border-color: rgba(56, 189, 248, 0.22);
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero">
<h1> LunarIce-DFSAR</h1>
<h3>Subsurface Lunar Water Ice Detection and Exploration Planning Framework</h3>
<p class="small-text">
Chandrayaan-2 DFSAR + OHRC + DEM/TMC + Diviner + Bayesian Scientific Fusion
</p>
<p>
A research-grade architecture for detecting, characterizing, validating and planning access to
subsurface water ice in lunar south polar permanently shadowed regions.
</p>
</div>
""", unsafe_allow_html=True)

st.image(
    "dashboard/assets/lunar_south_pole.png",
    caption="Lunar South Pole overview: Shackleton crater, PSRs and Chandrayaan-2 observation zones",
    use_container_width=True
)

c1, c2, c3, c4, c5, c6 = st.columns(6)
c1.metric("Scientific Modules", "18")
c2.metric("Research Papers", "4")
c3.metric("Datasets", "4+")
c4.metric("Mission Deliverables", "5")
c5.metric("Scientific Models", "12+")
c6.metric("Current Progress", "25%")

st.markdown("##  Project Overview")

st.markdown("""
<div class="card">
This project proposes a multi-modal scientific framework for detecting, characterizing and estimating
subsurface lunar water ice in permanently shadowed regions of the lunar south pole.
<br><br>
Unlike simple CPR-threshold approaches, this system combines radar polarimetry, optical terrain analysis,
topographic shadow modeling, thermal stability physics, Bayesian fusion, landing site scoring and rover
traverse planning.
</div>
""", unsafe_allow_html=True)

st.markdown("##  How to Explore This Portal")

st.info("""
Recommended order:

1. **Architecture** — understand the full system  
2. **Module Explorer** — explore all 18 modules  
3. **DFSAR Science** — understand radar processing  
4. **Mathematical Models** — see equations used  
5. **Bayesian Fusion** — see how evidence is combined  
6. **Landing Site + Rover Traverse** — see mission planning logic  
7. **Implementation Status** — see what has already been built  
""")

st.markdown("##  Official Problem Alignment")

st.table({
    "Required Outcome": [
        "Ice detection",
        "Scientific characterization",
        "Landing site selection",
        "Rover traverse planning",
        "Quantitative estimation"
    ],
    "Our Approach": [
        "DFSAR CPR, DOP, Stokes and decomposition",
        "Thermal stability + PSR + polarimetric analysis",
        "Weighted scoring using ice, slope, illumination, boulders and communication",
        "Cost-map based A* / Dijkstra route planning",
        "Ice volume and mass estimation with uncertainty"
    ]
})

st.markdown("##  Current Implementation Status")

st.table({
    "Component": [
        "Scientific architecture",
        "Literature review",
        "Research paper integration",
        "Configuration system",
        "Dataset model",
        "PDS4 XML parser",
        "Pipeline manager",
        "Module 01",
        "Module 02",
        "Module 03",
        "Dashboard portal",
        "Dataset integration readiness"
    ],
    "Status": [
        "Completed",
        "Completed",
        "4 papers integrated",
        "Complete",
        "Complete",
        "Complete",
        "Complete",
        "Implemented",
        "Framework + tests",
        "Integrated skeleton",
        "Active",
        "Ready for Chandrayaan-2 data"
    ]
})

st.markdown("##  Why This Project Is Different")

st.markdown("""
<div class="gold-card">
Most solutions stop at <b>radar anomaly detection</b>.
This framework continues toward <b>mission-ready exploration planning</b>.
<br><br>
It answers not only:
<br>
<b>“Where might ice exist?”</b>
<br><br>
but also:
<br>
<b>“Is it scientifically defensible, thermally stable, accessible, quantifiable and reachable by a rover?”</b>
</div>
""", unsafe_allow_html=True)

st.success("""
This portal documents the complete proposed system architecture, scientific methodology,
research-paper mapping, mathematical models and current implementation status.
""")

st.markdown("---")
st.caption("LunarIce-DFSAR | Chandrayaan-2 based multi-modal lunar ice characterization framework")