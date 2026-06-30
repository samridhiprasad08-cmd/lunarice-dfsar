import streamlit as st

st.set_page_config(page_title="Rover Traverse", layout="wide")

st.title("Rover Traverse Planning Workflow")

st.markdown("""
The rover traverse system converts scientific ice maps into an operational path from
a safe landing zone to a high-priority ice target.
""")

st.image(
    "dashboard/assets/rover_traverse_workflow.png",
    caption="Rover traverse workflow from landing site to ice target",
    use_container_width=True
)

st.markdown("## Cost Function")

st.latex(r"""
Cost =
w_s Slope +
w_b BoulderDensity +
w_d Distance +
w_i IlluminationRisk
""")

st.table({
    "Factor": ["Slope", "Boulder density", "Distance", "Illumination risk"],
    "Purpose": [
        "Avoid steep terrain",
        "Avoid rocky hazardous zones",
        "Reduce energy usage",
        "Maintain solar and thermal safety"
    ]
})

st.markdown("## Mission Value")

st.info("""
This transforms the project from only “where is ice?” into
“where should we land and how can a rover safely reach the target?”
""")