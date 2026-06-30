import streamlit as st

st.set_page_config(
    page_title="Landing Site Planning",
    page_icon="",
    layout="wide"
)

st.title("Landing Site Suitability Framework")

st.markdown("""
The landing site should be close to scientifically valuable ice-bearing regions while also
remaining safe, illuminated, accessible and operationally feasible.

This page explains how the framework converts ice detection results into a ranked list of
candidate landing zones.
""")

st.markdown("---")

st.markdown("## Landing Site Scoring Model")

st.markdown("""
Selecting a landing site near the lunar south pole is a multi-objective decision problem.

A good landing site must satisfy both **scientific** and **engineering** requirements:

- It should be close to high-probability ice deposits.
- It should have low slope for safe descent and touchdown.
- It should have sufficient illumination for power and thermal control.
- It should avoid boulder-rich hazardous terrain.
- It should maintain acceptable communication visibility.

To balance these competing requirements, a weighted suitability score is computed.
""")

st.latex(r"""
Score =
0.30I +
0.25S +
0.20L +
0.15B +
0.10C
""")

st.markdown("### Variable Meaning")

st.table({
    "Term": ["I", "S", "L", "B", "C"],
    "Meaning": [
        "Ice probability or proximity to high-confidence ice target",
        "Slope safety score",
        "Solar illumination availability",
        "Boulder hazard score",
        "Communication visibility"
    ],
    "Weight": ["0.30", "0.25", "0.20", "0.15", "0.10"]
})
st.markdown("## How the Score Is Computed")

st.markdown("""
Each factor is first converted into a normalized score between **0 and 1**.

A value of:

- **1** means highly suitable
- **0** means unsuitable

The final landing score is then calculated as a weighted sum.
""")

st.latex(r"""
Score =
0.30I +
0.25S +
0.20L +
0.15B +
0.10C
""")

st.markdown("### 1. Ice Proximity Score")

st.latex(r"""
I =
P_{ice}
\times
\left(
1 -
\frac{d_{ice}}{d_{max}}
\right)
""")

st.markdown("""
Where:

- \(P_{ice}\) = ice probability from Bayesian fusion
- \(d_{ice}\) = distance from landing site to nearest high-probability ice region
- \(d_{max}\) = maximum acceptable rover distance

A site closer to high-probability ice receives a higher score.
""")

st.markdown("### 2. Slope Safety Score")

st.latex(r"""
S =
1 -
\frac{slope}{slope_{max}}
""")

st.markdown("""
Where:

- \(slope\) = local terrain slope from DEM/TMC
- \(slope_{max}\) = maximum acceptable landing slope

Flatter terrain gives a higher score.
""")

st.markdown("### 3. Illumination Score")

st.latex(r"""
L =
\frac{T_{sunlit}}{T_{total}}
""")

st.markdown("""
Where:

- \(T_{sunlit}\) = time the region receives useful illumination
- \(T_{total}\) = total observation period

More illuminated regions are preferred for power and thermal control.
""")

st.markdown("### 4. Boulder Safety Score")

st.latex(r"""
B =
1 -
\frac{\rho_{boulder}}{\rho_{max}}
""")

st.markdown("""
Where:

- \(\rho_{boulder}\) = boulder density estimated from OHRC imagery
- \(\rho_{max}\) = maximum acceptable boulder density

Low-boulder regions receive higher scores.
""")

st.markdown("### 5. Communication Visibility Score")

st.latex(r"""
C =
\frac{T_{visible}}{T_{total}}
""")

st.markdown("""
Where:

- \(T_{visible}\) = time with Earth/orbiter communication visibility
- \(T_{total}\) = total mission-relevant time window

Sites with better communication access receive higher scores.
""")

st.markdown("## Final Candidate Selection")

st.markdown("""
After computing all five scores, every candidate landing pixel or zone receives a final score.

The candidates are then sorted:

1. Remove unsafe regions using hard constraints  
2. Compute normalized scores  
3. Apply weighted scoring equation  
4. Rank candidate sites  
5. Select top landing zones  
6. Pass best sites to rover traverse planning  
""")

st.markdown("## Scientific and Engineering Justification")

st.markdown("""
The weights are chosen to reflect the balance between **scientific return** and **mission safety**.

### Ice Accessibility — 0.30

Ice accessibility receives the highest weight because the main objective of the mission is
to identify and access scientifically meaningful water-ice deposits. A landing site far from
a high-confidence ice target would reduce the value of the mission, even if the site is safe.

### Terrain Safety — 0.25

Slope safety receives the second-highest weight because landing stability is non-negotiable.
A scientifically interesting site is not useful if the lander cannot safely touch down or if a
rover cannot leave the landing zone.

### Solar Illumination — 0.20

Illumination is important for power generation and thermal management. Lunar south polar
missions often prefer regions near PSRs that still receive useful sunlight, such as crater rims
or nearby elevated terrain.

### Boulder Hazard — 0.15

Boulders and rough terrain increase the risk of landing damage and rover mobility problems.
This factor penalizes rocky or blocky regions visible in OHRC imagery.

### Communication Visibility — 0.10

Communication is important, but it is weighted slightly lower because relay support or
mission design choices may partially compensate for limited direct visibility.
""")

st.markdown("---")

st.markdown("## Landing Site Selection Workflow")

st.graphviz_chart("""
digraph {

rankdir=LR;

graph [bgcolor="transparent"];

node [
shape=box,
style="rounded,filled",
fillcolor="#0f172a",
fontcolor="white",
color="#38bdf8",
fontsize=12
];

A [label="Ice Probability\\nfrom Bayesian Fusion"];
B [label="Slope Safety\\nfrom DEM/TMC"];
C [label="Illumination\\nnear PSR boundary"];
D [label="Boulder Density\\nfrom OHRC"];
E [label="Communication\\nvisibility"];

F [
label="Weighted Landing\\nSuitability Score",
fillcolor="#312e81",
color="#a78bfa"
];

G [
label="Ranked Candidate\\nLanding Zones",
fillcolor="#064e3b",
color="#34d399"
];

H [
label="Input to Rover\\nTraverse Planning",
fillcolor="#1e3a8a",
color="#60a5fa"
];

A -> F;
B -> F;
C -> F;
D -> F;
E -> F;

F -> G;
G -> H;

}
""")

st.markdown("## Candidate Ranking Strategy")

st.markdown("""
Each potential landing zone is evaluated independently.

For every candidate zone, the framework computes normalized scores for ice proximity,
terrain slope, illumination, boulder hazard and communication visibility. These scores are
then combined using the weighted equation.

The best candidates are those that satisfy both science and safety requirements:

- High ice probability nearby
- Low slope terrain
- Low boulder density
- Useful illumination access
- Acceptable communication geometry
- Reasonable rover distance to ice target

The top-ranked landing zones are passed to the rover traverse planning module.
""")

st.markdown("---")

st.markdown("## Engineering Constraints")

st.table({
    "Constraint": [
        "Maximum landing slope",
        "Preferred illumination availability",
        "Maximum boulder hazard",
        "Maximum distance to ice target",
        "Preferred terrain type"
    ],
    "Example Threshold": [
        "< 15 degrees",
        "> 60% relative illumination score",
        "Low to moderate boulder density",
        "< 10 km rover traverse distance",
        "Stable, relatively smooth terrain"
    ],
    "Reason": [
        "Reduces touchdown and rover mobility risk",
        "Improves power and thermal conditions",
        "Avoids landing damage and wheel hazards",
        "Keeps rover mission feasible",
        "Improves landing survivability"
    ]
})

st.markdown("## Output Products")

st.table({
    "Output": [
        "Landing suitability map",
        "Ranked candidate landing sites",
        "Safety constraint mask",
        "Science-accessibility score",
        "Rover planning start point"
    ],
    "Purpose": [
        "Shows spatial suitability across the region",
        "Provides final candidate list for mission review",
        "Removes unsafe terrain",
        "Balances ice value and engineering safety",
        "Feeds into rover traverse planning"
    ]
})

st.success("""
This module converts lunar ice detection into an actionable exploration decision:
where to safely land so that high-value ice targets remain reachable.
""")

st.markdown("---")
st.caption("LunarIce-DFSAR | Landing site suitability and exploration planning framework")