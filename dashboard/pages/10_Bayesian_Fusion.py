import streamlit as st

st.set_page_config(
    page_title="Bayesian Fusion",
    page_icon="🌕",
    layout="wide"
)

st.title("Bayesian Multi-Evidence Fusion")

st.markdown("""
One of the biggest challenges in lunar ice detection is that no individual indicator can
prove the existence of water ice.

High CPR can be caused by rough terrain.

Low temperatures alone do not guarantee ice.

Permanent shadow does not necessarily imply volatile accumulation.

Therefore, multiple independent evidence streams must be combined into a single
probabilistic framework.
""")

st.image(
    "dashboard/assets/bayesian_fusion.png",
    caption="Bayesian multi-evidence fusion architecture",
    use_container_width=True
)

st.markdown("## Why Bayesian Fusion?")

st.info("""
Bayesian fusion provides a mathematically rigorous way to combine uncertain observations.

Instead of making binary decisions, the framework estimates the probability that
a location contains subsurface ice.
""")

st.markdown("## Evidence Streams")

st.table({
    "Evidence Source": [
        "DFSAR CPR",
        "DFSAR DOP",
        "Polarimetric Decomposition",
        "Permanent Shadow Mask",
        "Thermal Stability",
        "Terrain Safety",
        "Depth-Zone Analysis"
    ],
    "Scientific Meaning": [
        "Potential ice-related scattering",
        "Depolarization behaviour",
        "Surface vs volume scattering",
        "Cold-trap condition",
        "Long-term preservation potential",
        "False-positive reduction",
        "Shallow vs deeper response"
    ]
})

st.markdown("## Bayesian Framework")

st.latex(r"""
P(Ice|D)
=
\frac{
P(D|Ice)\times P(Ice)
}
{
P(D)
}
""")

st.markdown("""
Where:

- P(Ice|D) = posterior probability of ice
- P(D|Ice) = likelihood of observed evidence
- P(Ice) = prior probability
- P(D) = evidence normalization term
""")

st.markdown("## Workflow")

st.code("""
Radar Evidence
       +
Terrain Evidence
       +
Thermal Evidence
       +
PSR Evidence
       +
Depth Evidence
          ↓
Likelihood Estimation
          ↓
Bayesian Fusion
          ↓
Posterior Ice Probability
          ↓
Confidence Map
""")

st.markdown("## Why This Improves Reliability")

st.success("""
The fusion engine reduces false positives by requiring agreement between
multiple independent physical indicators.

A region is considered a strong ice candidate only when:

• Radar evidence is favourable
• Terrain conditions are consistent
• Thermal stability exists
• Permanent shadow conditions are present
• Depth behaviour is physically plausible
""")

st.markdown("## Output Products")

st.table({
    "Output": [
        "Ice Probability Map",
        "Confidence Map",
        "Candidate Ice Zones",
        "Fusion Report"
    ],
    "Purpose": [
        "Primary scientific product",
        "Uncertainty estimation",
        "Mission planning input",
        "Traceable evidence summary"
    ]
})

st.markdown("---")
st.caption("LunarIce-DFSAR | Bayesian multi-evidence fusion framework")