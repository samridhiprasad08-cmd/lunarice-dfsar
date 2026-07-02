import streamlit as st

st.set_page_config(
    page_title="ANVIKSHA",
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
<h1>ANVIKSHA</h1>
<h3>A Confidence-Driven Lunar Exploration and Mission Planning Framework</h3>
<p class="small-text">
Chandrayaan-2 DFSAR + OHRC + DEM/TMC + Diviner + Bayesian Evidence Fusion
</p>
<p>
ANVIKSHA is built around one simple question: if a future lunar mission is going to spend years of planning
and resources on a crater, how do we know if that crater is actually worth exploring?
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

st.markdown("## Project Overview")
st.markdown("""
<div class="card">
ANVIKSHA is not just designed to create another lunar ice map. The aim is to understand a crater from
multiple perspectives and then decide whether it can become a meaningful target for future exploration.
<br><br>
The framework brings together radar observations, terrain conditions, illumination patterns and thermal
stability. These evidence layers are then used for confidence assessment, exploration opportunity ranking,
ice volume estimation, landing site evaluation and rover traverse planning.
<br><br>
In simple words, ANVIKSHA tries to turn scientific observations into exploration decisions.
</div>
""", unsafe_allow_html=True)

st.markdown("## Research Methodology")
st.markdown("""
<div class="card">
Our methodology started with the idea that no single observation can fully explain what is happening inside
a lunar crater. Radar data can give important clues about possible subsurface ice, but it cannot tell the
complete story alone. A crater also has to be understood through its terrain, illumination conditions and
thermal stability.
<br><br>
So, the workflow begins by studying different evidence layers separately. DFSAR radar data is used to look
for possible ice-related signatures. OHRC imagery helps in understanding surface features, craters and
boulders. DEM and terrain data help estimate slope, roughness and landing safety. Thermal and illumination
information helps check whether the region can preserve ice over time.
<br><br>
After this, ANVIKSHA moves into confidence assessment. Instead of directly saying that a region contains ice,
the framework asks how reliable the evidence is. It checks whether different observations support each other
and where uncertainty may still exist.
<br><br>
Once the scientific evidence is understood, the focus shifts to mission planning. The framework ranks regions
based on scientific value, safety and accessibility. These ranked regions are then used for landing site
selection and rover traverse planning.
<br><br>
The goal is not just to detect ice. The goal is to understand whether a crater deserves future exploration,
where a lander can safely operate, and how a rover can reach the target region.
</div>
""", unsafe_allow_html=True)

st.markdown("## How to Explore This Portal")
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

st.markdown("## Official Problem Alignment")
st.table({
    "Required Outcome": [
        "Ice detection",
        "Scientific characterization",
        "Landing site selection",
        "Rover traverse planning",
        "Quantitative estimation"
    ],
    "Our Approach": [
        "DFSAR CPR, DOP, Stokes parameters and polarimetric analysis",
        "Radar evidence combined with terrain, illumination and thermal stability",
        "Weighted scoring using ice potential, slope, illumination, boulder risk and communication",
        "Cost-map based A* / Dijkstra route planning",
        "Ice volume and mass estimation with uncertainty"
    ]
})

st.markdown("## Current Implementation Status")
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

st.markdown("## Why This Project Is Different")
st.markdown("""
<div class="gold-card">
Most solutions focus mainly on finding possible ice signatures.
<br><br>
ANVIKSHA goes one step further. It asks whether the evidence is reliable, whether the region is scientifically
valuable, whether a lander can operate safely nearby, and whether a rover can realistically reach the target.
<br><br>
It answers not only:
<br>
<b>“Where might ice exist?”</b>
<br><br>
but also:
<br>
<b>“Is this crater worth exploring, and how can we explore it safely?”</b>
</div>
""", unsafe_allow_html=True)

st.success("""
ANVIKSHA documents the complete proposed system architecture, research methodology,
mission-planning logic and current implementation status in one interactive portal.
""")

st.markdown("---")
st.caption("ANVIKSHA | Chandrayaan-2 based lunar ice assessment and mission planning framework")