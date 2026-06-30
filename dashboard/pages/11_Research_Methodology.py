import streamlit as st

st.set_page_config(
    page_title="Research Methodology",
    page_icon="🌕",
    layout="wide"
)

st.title("Research Methodology")

st.markdown("""
This page describes the complete scientific workflow of the proposed framework.

The methodology combines radar polarimetry, thermal physics, terrain analysis,
probabilistic fusion and mission planning into a single end-to-end architecture.
""")

st.markdown("## End-to-End Scientific Workflow")

st.graphviz_chart("""
digraph {
    rankdir=TB;
    graph [bgcolor="transparent"];

    node [
        shape=box,
        style="rounded,filled",
        fillcolor="#0f172a",
        fontcolor="white",
        color="#38bdf8"
    ];

    A [label="Data Acquisition"];
    B [label="Radiometric Calibration"];
    C [label="PSR & Terrain Analysis"];
    D [label="Polarimetric Features"];
    E [label="Scattering Analysis"];
    F [label="Depth-Zone Analysis"];
    G [label="Thermal Stability"];
    H [label="Bayesian Fusion"];
    I [label="Ice Volume Estimation"];
    J [label="Scientific Validation"];
    K [label="Landing Site Selection"];
    L [label="Rover Traverse Planning"];

    A -> B -> C -> D -> E -> F -> G -> H -> I -> J -> K -> L;
}
""")

st.markdown("---")

st.markdown("## Stage 1 — Scientific Data Acquisition")

st.markdown("""
The framework begins by collecting and organizing all required mission datasets.

### Primary Inputs

- DFSAR Radar Data
- OHRC Optical Images
- DEM / TMC Topography
- Diviner Temperature Data
- LCROSS and Mini-RF Validation Data

### Purpose

Create a unified scientific dataset that can be processed consistently by all later modules.
""")

st.markdown("## Stage 2 — Radiometric Calibration")

st.markdown("""
Raw radar measurements cannot be interpreted directly.

Calibration removes system effects and converts observations into physically meaningful radar products.

### Outputs

- Calibrated radar power
- Noise-corrected radar imagery
- Georeferenced radar products
""")

st.markdown("## Stage 3 — Permanent Shadow and Terrain Analysis")

st.markdown("""
Ice is expected to survive mainly in permanently shadowed regions.

Terrain analysis provides:

- Slope
- Aspect
- Illumination geometry
- Boulder hazard information
- PSR masks
""")

st.latex(r"""
Slope =
\tan^{-1}
\left(
\sqrt{
\left(\frac{\partial z}{\partial x}\right)^2 +
\left(\frac{\partial z}{\partial y}\right)^2
}
\right)
""")

st.markdown("## Stage 4 — Polarimetric Feature Extraction")

st.markdown("""
DFSAR polarimetry is used to derive:

- Stokes Parameters
- CPR
- DOP
- Relative Phase
- Ellipticity

These features provide information about the scattering behaviour of the target surface.
""")

st.latex(r"""
DOP =
\frac{
\sqrt{S_2^2+S_3^2+S_4^2}
}
{S_1}
""")

st.markdown("## Stage 5 — Scattering Mechanism Analysis")

st.markdown("""
High CPR alone does not imply ice.

This stage separates:

- Surface scattering
- Double-bounce scattering
- Volume scattering

using polarimetric decomposition methods.
""")

st.markdown("## Stage 6 — Dual-Frequency Depth Analysis")

st.markdown("""
DFSAR provides both L-band and S-band observations.

By comparing the behaviour of the two frequencies, the framework estimates whether
radar anomalies are likely to originate from:

- Surface layers
- Shallow subsurface layers
- Deeper subsurface zones
""")

st.markdown("## Stage 7 — Thermal Stability Modeling")

st.markdown("""
Radar evidence is constrained using thermal physics.

Following Schorghofer & Taylor:

- Water molecules migrate through ballistic transport
- Cold traps accumulate volatiles
- Stable temperatures increase residence time
""")

st.latex(r"""
\tau(T)
=
\frac{\theta}{E(T)}
""")

st.markdown("## Stage 8 — Bayesian Multi-Evidence Fusion")

st.markdown("""
Evidence from all previous stages is fused into a single ice probability estimate.

Inputs:

- CPR
- DOP
- Thermal stability
- Terrain safety
- PSR membership
- Depth-zone behaviour
""")

st.latex(r"""
P(Ice|D)
=
\frac{
P(D|Ice)P(Ice)
}
{
P(D)
}
""")

st.markdown("## Stage 9 — Volumetric Ice Estimation")

st.markdown("""
The framework estimates potential ice volume and mass.

This converts scientific detection into exploration-relevant resource estimates.
""")

st.latex(r"""
V_{ice}
=
A \times d \times C \times P_{ice}
""")

st.markdown("## Stage 10 — Scientific Validation")

st.markdown("""
Outputs are compared against:

- LCROSS observations
- Mini-RF products
- Diviner temperature constraints
- Published literature
""")

st.markdown("## Stage 11 — Landing Site Selection")

st.markdown("""
Candidate landing sites are evaluated using:

- Ice proximity
- Terrain slope
- Illumination
- Boulder density
- Communication visibility
""")

st.latex(r"""
Score
=
0.30I
+
0.25S
+
0.20L
+
0.15B
+
0.10C
""")

st.markdown("## Stage 12 — Rover Traverse Planning")

st.markdown("""
The final stage generates an optimized route between the landing site and high-priority ice targets.

The rover path minimizes:

- Hazard exposure
- Energy consumption
- Terrain difficulty
- Traversal distance
""")

st.markdown("---")

st.success("""
The proposed methodology transforms raw Chandrayaan-2 observations into mission-ready
scientific products, including ice probability maps, volume estimates, landing site
recommendations and rover traverse plans.
""")

st.caption("LunarIce-DFSAR | End-to-End Research Methodology")