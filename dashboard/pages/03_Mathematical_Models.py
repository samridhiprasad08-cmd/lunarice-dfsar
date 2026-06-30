import streamlit as st

st.set_page_config(page_title="Mathematical Models", page_icon="📐", layout="wide")

st.title("📐 Scientific and Mathematical Models")

st.markdown("## 1. Terrain Slope from DEM")

st.latex(r"""
S =
\tan^{-1}
\left(
\sqrt{
\left(\frac{\partial z}{\partial x}\right)^2+
\left(\frac{\partial z}{\partial y}\right)^2
}
\right)
""")

st.write("Used for PSR geometry, landing safety and rover traversal.")

st.markdown("## 2. Stokes Parameters")

st.latex(r"S_1 = |E_H|^2 + |E_V|^2")
st.latex(r"S_2 = |E_H|^2 - |E_V|^2")
st.latex(r"S_3 = 2Re(E_HE_V^*)")
st.latex(r"S_4 = -2Im(E_HE_V^*)")

st.write("These describe the polarization state of the radar return.")

st.markdown("## 3. Degree of Polarization")

st.latex(r"""
DOP =
\frac{
\sqrt{S_2^2+S_3^2+S_4^2}
}
{S_1}
""")

st.write("DOP helps distinguish coherent surface scattering from depolarized volume scattering.")

st.markdown("## 4. Bayesian Ice Probability")

st.latex(r"""
P(Ice|D)=
\frac{
P(D|Ice)P(Ice)
}
{
P(D)
}
""")

st.write("D includes radar, terrain, thermal and PSR evidence.")

st.markdown("## 5. Ice Volume Estimation")

st.latex(r"""
V_{ice}=A \times d \times C \times P_{ice}
""")

st.write("Converts probability maps into exploration-relevant quantity estimates.")