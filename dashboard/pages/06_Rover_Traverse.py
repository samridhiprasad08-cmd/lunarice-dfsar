import streamlit as st

st.set_page_config(
    page_title="Rover Traverse",
    page_icon="",
    layout="wide"
)

st.title("Rover Traverse Planning Framework")

st.markdown("""
After a suitable landing site is selected, the next question is:

**How can the rover safely reach the highest-priority ice target?**

This module converts terrain, hazard and science layers into a rover traversability map.
The goal is not simply to find the shortest path, but the safest and most energy-efficient
path that still reaches a scientifically valuable ice-bearing region.
""")

st.markdown("---")

st.image(
    "dashboard/assets/rover_traverse_workflow.png",
    caption="Rover traverse workflow from landing site to ice target",
    use_container_width=True
)

st.markdown("---")

st.markdown("## Traversability Cost Function")

st.markdown("""
The rover path is planned using a **cost surface**.

Each pixel in the terrain map is assigned a movement cost. A low-cost pixel is easier and
safer to cross, while a high-cost pixel is risky, steep, rough or inefficient.

The rover does not move directly toward the ice target. Instead, it searches for the route
with the lowest accumulated traversal cost.
""")

st.latex(r"""
Cost =
0.40S +
0.30B +
0.20D +
0.10R
""")

st.markdown("### Variable Meaning")

st.table({
    "Term": ["S", "B", "D", "R"],
    "Meaning": [
        "Slope cost",
        "Boulder hazard cost",
        "Distance / path length cost",
        "Radar-derived surface roughness cost"
    ],
    "Weight": ["0.40", "0.30", "0.20", "0.10"]
})

st.markdown("---")

st.markdown("## How Each Cost Term Is Computed")

st.markdown("""
Each cost component is normalized between **0 and 1**.

- **0** means easy or safe to traverse
- **1** means difficult or unsafe to traverse

The final cost is a weighted sum of these normalized values.
""")

st.markdown("### 1. Slope Cost")

st.latex(r"""
S =
\frac{\theta}{\theta_{max}}
""")

st.markdown("""
Where:

- \(\\theta\) = local terrain slope from DEM/TMC
- \(\\theta_{max}\) = maximum traversable slope

Steeper terrain increases the cost because it affects rover stability, wheel traction,
power consumption and rollover risk.

If the slope exceeds the safe threshold, that region can be marked as a forbidden zone.
""")

st.markdown("### 2. Boulder Hazard Cost")

st.latex(r"""
B =
\frac{\rho_{boulder}}{\rho_{max}}
""")

st.markdown("""
Where:

- \(\\rho_{boulder}\) = boulder density estimated from OHRC imagery
- \(\\rho_{max}\) = maximum acceptable boulder density

A region with more boulders receives a higher traversal cost because it increases the
risk of wheel damage, path blockage and navigation difficulty.
""")

st.markdown("### 3. Distance Cost")

st.latex(r"""
D =
\frac{d}{d_{max}}
""")

st.markdown("""
Where:

- \(d\) = distance travelled through a candidate path segment
- \(d_{max}\) = maximum acceptable traverse distance

Distance is included because longer paths consume more time, power and operational
resources.

However, distance is not assigned the highest weight because a longer safe path is usually
preferred over a shorter hazardous route.
""")

st.markdown("### 4. Radar Roughness Cost")

st.latex(r"""
R =
\frac{\sigma_{rough}}{\sigma_{max}}
""")

st.markdown("""
Where:

- \(\\sigma_{rough}\) = local radar-derived roughness or backscatter variability
- \(\\sigma_{max}\) = maximum observed roughness value

Radar roughness is used as a secondary terrain-risk indicator. It can highlight rough,
blocky or irregular surfaces that may not be fully captured by slope alone.
""")

st.markdown("---")

st.markdown("## Scientific and Engineering Justification of Weights")

st.markdown("""
The weights are assigned using rover mobility priority logic.

The cost function gives highest importance to the physical factors most likely to stop or
damage a rover.
""")

st.table({
    "Factor": [
        "Slope Cost",
        "Boulder Hazard Cost",
        "Distance Cost",
        "Radar Roughness Cost"
    ],
    "Weight": [
        "0.40",
        "0.30",
        "0.20",
        "0.10"
    ],
    "Why this priority was chosen": [
        "Slope directly affects rover stability, traction and energy consumption",
        "Boulders can block paths or damage wheels and suspension",
        "Distance affects time and energy but may be sacrificed for safety",
        "Radar roughness is useful but indirect, so it receives the lowest weight"
    ]
})

st.markdown("### Weight Normalization")

st.latex(r"""
0.40 + 0.30 + 0.20 + 0.10 = 1
""")

st.markdown("""
The weights sum to 1, so the final traversal cost remains interpretable as a normalized
risk score.

The priority order is:

**Slope > Boulder Hazard > Distance > Radar Roughness**
""")

st.markdown("""
### Why Slope Receives the Highest Weight

Slope is the most direct mobility constraint because it affects:

- rover traction
- center-of-mass stability
- motor torque requirement
- rollover risk
- downhill braking risk

Even if an ice target is scientifically valuable, a rover cannot safely reach it through
excessively steep terrain.
""")

st.markdown("""
### Why Boulder Hazard Receives the Second-Highest Weight

Boulders and blocky ejecta can create local obstacles that are not always represented
fully by a DEM. OHRC imagery helps estimate boulder density and identify hazardous
regions.

A high-boulder region can force detours or become completely non-traversable.
""")

st.markdown("""
### Why Distance Is Weighted Lower Than Safety

The shortest path is not always the best path.

A longer route with lower slope and fewer boulders is generally more realistic than a
shorter route through dangerous terrain.
""")

st.markdown("""
### Why Radar Roughness Is Included But Weighted Lowest

Radar roughness is useful because it provides information about surface irregularity and
blockiness. However, it is an indirect indicator. Therefore, it supports the cost model but
does not dominate the decision.
""")

st.markdown("---")

st.markdown("## Forbidden Zone Logic")

st.markdown("""
Some terrain should not be assigned a high cost; it should be removed completely from
the search space.

A pixel is marked as forbidden if it violates hard mobility constraints.
""")

st.latex(r"""
Forbidden =
\begin{cases}
1, & \theta > \theta_{max} \\
1, & \rho_{boulder} > \rho_{max} \\
1, & illumination < illumination_{min} \\
0, & otherwise
\end{cases}
""")

st.markdown("""
Forbidden zones are excluded before path planning. This prevents the algorithm from
choosing a dangerous route simply because it is shorter.
""")

st.markdown("---")

st.markdown("## Path Planning Algorithm")

st.markdown("""
After generating the cost surface, the rover path is computed using graph search.

Each map pixel is treated as a node, and movement between neighboring pixels is treated
as an edge with a traversal cost.
""")

st.markdown("### A* Search Function")

st.latex(r"""
f(n) = g(n) + h(n)
""")

st.markdown("""
Where:

- \(g(n)\) = accumulated traversal cost from the landing site to node \(n\)
- \(h(n)\) = estimated remaining cost from node \(n\) to the ice target
- \(f(n)\) = total estimated path cost

A* is preferred because it uses a heuristic to move efficiently toward the target while
still accounting for terrain cost.
""")

st.markdown("### Why A* Instead of Only Dijkstra?")

st.table({
    "Algorithm": ["Dijkstra", "A*"],
    "Strength": [
        "Guarantees minimum-cost path when all costs are known",
        "Uses a heuristic to reach the target faster"
    ],
    "Limitation": [
        "Can explore too many unnecessary pixels",
        "Depends on a reasonable heuristic"
    ],
    "Use in This Project": [
        "Useful fallback for small regions",
        "Preferred for larger terrain maps"
    ]
})

st.markdown("---")

st.markdown("## Rover Traverse Workflow")

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

A [label="Selected Landing Site"];
B [label="Slope Map\\nDEM/TMC"];
C [label="Boulder Map\\nOHRC"];
D [label="Distance Layer"];
E [label="Radar Roughness\\nDFSAR"];

F [
label="Cost Surface\\nGeneration",
fillcolor="#312e81",
color="#a78bfa"
];

G [
label="Forbidden Zone\\nMasking",
fillcolor="#7f1d1d",
color="#fca5a5"
];

H [
label="A* / Dijkstra\\nPath Search",
fillcolor="#1e3a8a",
color="#60a5fa"
];

I [
label="Lowest-Cost Safe\\nRover Traverse",
fillcolor="#064e3b",
color="#34d399"
];

J [
label="High-Priority\\nIce Target",
fillcolor="#164e63",
color="#67e8f9"
];

A -> F;
B -> F;
C -> F;
D -> F;
E -> F;

F -> G;
G -> H;
H -> I;
I -> J;

}
""")

st.markdown("---")

st.markdown("## Output Products")

st.table({
    "Output": [
        "Traversability cost map",
        "Forbidden zone mask",
        "Optimized rover path",
        "Distance and risk summary",
        "Ice target accessibility report"
    ],
    "Purpose": [
        "Shows terrain difficulty across the region",
        "Removes unsafe terrain from planning",
        "Provides the final route to the ice target",
        "Quantifies mission feasibility",
        "Connects science target to operational planning"
    ]
})

st.markdown("## Future Improvements")

st.markdown("""
Future versions can improve this module using:

- dynamic replanning
- rover wheel-soil interaction models
- energy-aware path planning
- reinforcement learning
- real-time hazard avoidance
- multi-target traverse planning
""")

st.success("""
This module converts ice detection into an operational mobility plan:
not only where ice may exist, but how a rover can safely reach it.
""")

st.markdown("---")
st.caption("LunarIce-DFSAR | Rover traverse planning and mobility-cost framework")