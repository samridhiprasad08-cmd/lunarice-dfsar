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

This module converts ice detection results into a ranked list of candidate landing zones.
""")

st.markdown("---")

st.markdown("## Landing Site Scoring Model")

st.markdown("""
Landing site selection near the lunar south pole is a multi-criteria decision problem.
A good site must balance scientific value with engineering safety.
""")

st.latex(r"""
Score =
0.30I +
0.25S +
0.20L +
0.15B +
0.10C
""")
st.markdown("""
The numbers are assigned as an initial decision model to make the ranking explainable.
They are not derived from training data because the official hackathon dataset has not yet been released.
""")

st.markdown("### Variable Meaning")

st.table({
    "Term": ["I", "S", "L", "B", "C"],
    "Meaning": [
        "Ice probability or proximity to high-confidence ice target",
        "Slope safety score",
        "Solar illumination availability",
        "Boulder hazard safety score",
        "Communication visibility"
    ],
    "Weight": ["0.30", "0.25", "0.20", "0.15", "0.10"]
})

st.markdown("## How Each Score Is Computed")

st.markdown("""
Each factor is normalized between **0 and 1**.

- **1** means highly suitable
- **0** means unsuitable

The final score is a weighted sum of the normalized values.
""")

st.markdown("### 1. Ice Proximity Score")

st.latex(r"""
I =
P_{ice}
\left(
1 -
\frac{d_{ice}}{d_{max}}
\right)
""")

st.markdown("""
Where:

- \(P_{ice}\) = ice probability from Bayesian fusion
- \(d_{ice}\) = distance to nearest high-probability ice region
- \(d_{max}\) = maximum acceptable rover distance

A site closer to high-confidence ice receives a higher score.
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

Flatter terrain receives a higher score.
""")

st.markdown("### 3. Illumination Score")

st.latex(r"""
L =
\frac{T_{sunlit}}{T_{total}}
""")

st.markdown("""
Where:

- \(T_{sunlit}\) = useful illumination duration
- \(T_{total}\) = total observation duration

Higher illumination improves power generation and thermal control.
""")

st.markdown("### 4. Boulder Safety Score")

st.latex(r"""
B =
1 -
\frac{\rho_{boulder}}{\rho_{max}}
""")

st.markdown("""
Where:

- \(\rho_{boulder}\) = boulder density from OHRC imagery
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

- \(T_{visible}\) = time with Earth/orbiter visibility
- \(T_{total}\) = total mission-relevant duration

Better communication access increases the score.
""")

st.markdown("---")

st.markdown("## Weight Selection Methodology")

st.markdown("""
The weights are assigned using a **mission-priority approach**, not randomly.

The scoring model prioritizes the main mission objective first, then safety and operational
feasibility. The weights are normalized so the total contribution equals 1.
""")

st.latex(r"""
\sum_{i=1}^{5} w_i = 1
""")

st.table({
    "Factor": [
        "Ice Accessibility",
        "Terrain Safety",
        "Solar Illumination",
        "Boulder Hazard",
        "Communication Visibility"
    ],
    "Weight": [
        "0.30",
        "0.25",
        "0.20",
        "0.15",
        "0.10"
    ],
    "Why this priority was chosen": [
        "Primary scientific objective of the mission",
        "Critical for safe landing and rover deployment",
        "Important for power and thermal survival",
        "Important for landing safety and rover mobility",
        "Important, but can sometimes be supported by relay assets"
    ]
})

st.markdown("""
### Priority Logic

The ranking follows this mission logic:

**Ice access > Landing safety > Illumination > Boulder risk > Communication**

Ice accessibility receives the highest weight because the purpose of the mission is to reach
scientifically valuable ice-bearing regions.

Terrain safety is nearly as important because a site with high scientific value is unusable
if the lander cannot safely touch down.

Illumination is weighted next because polar missions depend on power availability and
thermal control.

Boulder hazard is included to reduce landing and rover mobility risk.

Communication visibility receives the lowest weight because communication constraints
may be partly mitigated through relay orbiters or mission design choices.
""")

st.markdown("""
### Future Improvement

In later stages, these knowledge-driven weights can be replaced or refined using:

- Analytic Hierarchy Process
- Multi-Criteria Decision Analysis
- Bayesian Decision Theory
- Expert-derived ISRO mission priorities

This makes the scoring model adaptable to different mission objectives.
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

A [label="Ice Probability\\nBayesian Fusion"];
B [label="Slope Safety\\nDEM/TMC"];
C [label="Illumination\\nSolar Access"];
D [label="Boulder Density\\nOHRC"];
E [label="Communication\\nVisibility"];

F [
label="Weighted Suitability\\nScoring Engine",
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
The framework evaluates every candidate landing zone using the following sequence:

1. Remove unsafe regions using hard constraints  
2. Normalize all scoring factors between 0 and 1  
3. Compute the weighted suitability score  
4. Rank all candidate sites  
5. Select the highest-scoring landing zones  
6. Pass the best site to the rover traverse planning module  
""")

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
st.warning("""
Important note on weights:

The current weights are not claimed to be final mission-certified values.
They are initial, knowledge-driven weights chosen for ideation-stage scoring.

They are based on relative mission priority:
scientific value, safety, operational feasibility and mobility risk.

In the next implementation stage, these weights can be refined using:
AHP, MCDA, expert review, sensitivity analysis, or mission-specific constraints.
""")