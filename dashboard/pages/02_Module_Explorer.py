import streamlit as st

st.set_page_config(
    page_title="Module Explorer",
    page_icon="",
    layout="wide"
)

st.markdown("""
<style>
.module-hero {
    padding: 26px;
    border-radius: 18px;
    background: linear-gradient(135deg, #071426, #0f172a);
    border: 1px solid #2563eb;
    margin-bottom: 18px;
}
.module-card {
    padding: 20px;
    border-radius: 16px;
    background: #0f172a;
    border: 1px solid #334155;
    margin-bottom: 16px;
}
.selector-card {
    padding: 18px;
    border-radius: 16px;
    background: linear-gradient(135deg, #111827, #0f172a);
    border: 1px solid #38bdf8;
    margin-bottom: 22px;
}
.small-note {
    color: #93c5fd;
    font-size: 15px;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="module-hero">
<h1>18-Module Architecture Explorer</h1>
<p>
This section explains the complete technical architecture of the proposed lunar ice detection system.
Each module is designed as a scientific subsystem, not just as a Python file.
</p>
<p class="small-note">
The aim is to show how raw Chandrayaan-2 and supporting datasets move through calibration,
terrain analysis, polarimetry, thermal modelling, probabilistic fusion and finally mission planning.
</p>
</div>
""", unsafe_allow_html=True)

c1, c2, c3, c4 = st.columns(4)
c1.metric("Total Modules", "18")
c2.metric("Running Pipeline", "M01–M03")
c3.metric("Core Science Papers", "4")
c4.metric("Final Products", "5+")

modules = {
    "M01 — Scientific Data Acquisition Engine": {
        "status": "Implemented",
        "short": "Brings all datasets into one consistent project structure.",
        "objective": "Load, validate and organize DFSAR, OHRC, DEM/TMC, Diviner and validation datasets before scientific processing begins.",
        "why": "The datasets used in this problem come from different instruments, formats and coordinate systems. If they are not standardized at the beginning, every later result becomes difficult to reproduce or compare.",
        "science": "This module does not perform ice detection directly. Its scientific value is in preserving metadata integrity: acquisition geometry, orbit information, incidence angle, frequency band, image dimensions and spatial footprint.",
        "engineering": "Creates a unified internal data object so every later module receives clean and traceable inputs.",
        "inputs": ["DFSAR PDS4 XML", "DFSAR radar data", "OHRC image", "DEM/TMC", "Diviner map"],
        "outputs": ["Unified dataset object", "Metadata summary", "Input validation logs"],
        "equation": r"D_{unified}=\{D_{DFSAR},D_{OHRC},D_{DEM},D_{Thermal}\}",
        "workflow": ["Read files", "Parse metadata", "Check geometry", "Standardize paths", "Create dataset object"],
        "papers": [["All four papers", "Provides organized inputs required by the scientific modules"]],
        "deliverables": ["Validated dataset object", "Metadata report", "Pipeline-ready inputs"],
        "isro": "This makes the system ready to accept the actual Chandrayaan-2 dataset once provided."
    },
    "M02 — Radiometric Calibration Engine": {
        "status": "Framework + Tests",
        "short": "Turns raw radar measurements into usable backscatter products.",
        "objective": "Convert raw DFSAR radar values into calibrated radar intensity/backscatter products suitable for polarimetric analysis.",
        "why": "Raw SAR values are not directly comparable across scenes because they include system gain, noise, incidence angle effects and acquisition geometry.",
        "science": "Radiometric calibration is essential before deriving CPR, DOP or scattering features. Without it, a bright radar pixel may be caused by instrument effects rather than a real surface property.",
        "engineering": "Implements DN-to-power conversion, noise correction and incidence-angle normalization as the first reproducible preprocessing layer.",
        "inputs": ["Raw DFSAR radar values", "Incidence angle", "Calibration metadata"],
        "outputs": ["Radar power image", "Noise-corrected image", "Sigma0-like calibrated product"],
        "equation": r"\sigma^0 \approx \frac{P}{\sin(\theta)}",
        "workflow": ["Digital numbers", "Power conversion", "Noise correction", "Incidence correction", "Calibrated output"],
        "papers": [["Mini-RF radar literature", "Supports physically meaningful radar interpretation"]],
        "deliverables": ["Calibrated radar layer", "Preprocessing log", "Tested calibration functions"],
        "isro": "This module ensures that later radar-based ice indicators are based on corrected measurements rather than raw values."
    },
    "M03 — Permanent Shadow and Terrain Analysis Engine": {
        "status": "Integrated Skeleton",
        "short": "Finds cold-trap compatible terrain and unsafe regions.",
        "objective": "Identify permanently shadowed regions, slope hazards and terrain constraints using DEM/TMC and OHRC-derived information.",
        "why": "Radar anomalies outside thermally stable shadowed regions are weaker ice candidates. Terrain also controls landing safety and rover movement.",
        "science": "The lunar poles receive sunlight at very low angles. Crater interiors can remain permanently shadowed, allowing volatile preservation over long timescales.",
        "engineering": "Generates slope, aspect, shadow and PSR masks that constrain downstream ice probability estimation.",
        "inputs": ["DEM/TMC", "OHRC image", "Solar geometry", "PSR boundary data"],
        "outputs": ["Slope map", "Aspect map", "Shadow mask", "PSR candidate mask"],
        "equation": r"S=\tan^{-1}\left(\sqrt{\left(\frac{\partial z}{\partial x}\right)^2+\left(\frac{\partial z}{\partial y}\right)^2}\right)",
        "workflow": ["Load DEM", "Compute gradients", "Estimate slope/aspect", "Apply illumination logic", "Generate PSR mask"],
        "papers": [["Schorghofer & Taylor", "Cold-trap stability motivation"], ["LCROSS", "Validation target in a cold PSR environment"]],
        "deliverables": ["PSR mask", "Slope map", "Terrain constraint layer"],
        "isro": "This module links ice detection to real landing and rover feasibility."
    },
    "M04 — Polarimetric Feature Extraction Engine": {
        "status": "Designed",
        "short": "Extracts CPR, DOP, Stokes parameters and phase information.",
        "objective": "Compute radar polarimetric observables needed for identifying possible volume scattering and reducing roughness-related false positives.",
        "why": "High CPR alone cannot prove ice. Polarimetric features provide additional evidence about the scattering behaviour of the surface and shallow subsurface.",
        "science": "The polarization state of the returned radar signal changes depending on whether scattering is dominated by surface roughness, double-bounce structures or volume-like media.",
        "engineering": "Produces CPR, DOP, Stokes parameters, phase and ellipticity maps for later fusion.",
        "inputs": ["Calibrated DFSAR channels", "Polarimetric metadata"],
        "outputs": ["S1-S4", "CPR map", "DOP map", "Phase map", "Ellipticity map"],
        "equation": r"DOP=\frac{\sqrt{S_2^2+S_3^2+S_4^2}}{S_1}",
        "workflow": ["Prepare radar channels", "Compute Stokes vector", "Derive CPR/DOP", "Generate feature maps"],
        "papers": [["Kumari & Bhardwaj", "Stokes and child parameters"], ["Nozette et al.", "Hybrid polarimetry and CPR interpretation"]],
        "deliverables": ["CPR map", "DOP map", "Polarimetric feature stack"],
        "isro": "This module provides the primary radar evidence layer for ice probability estimation."
    },
    "M05 — Scattering Mechanism Analysis Engine": {
        "status": "Designed",
        "short": "Separates surface, double-bounce and volume scattering.",
        "objective": "Classify the dominant radar scattering mechanism for each candidate region.",
        "why": "Rough crater walls and blocky ejecta can mimic ice-like radar signatures. Decomposition helps reduce this ambiguity.",
        "science": "Polarimetric decomposition interprets the radar return as a mixture of surface, double-bounce and volume scattering components.",
        "engineering": "Generates a scattering class map that weights or rejects candidate ice detections.",
        "inputs": ["Stokes parameters", "DOP", "Relative phase", "Ellipticity"],
        "outputs": ["Scattering class map", "Volume scattering score", "False-positive mask"],
        "equation": r"Class=f(m,\delta,\chi,H,\alpha)",
        "workflow": ["Load polarimetric features", "Apply decomposition", "Classify mechanism", "Generate confidence layer"],
        "papers": [["Kumari & Bhardwaj", "m-delta and m-chi decomposition"], ["Nozette et al.", "CPR ambiguity and volume scattering"]],
        "deliverables": ["Scattering map", "Volume score", "False-positive reduction layer"],
        "isro": "This directly addresses the major scientific weakness of CPR-only ice detection."
    },
    "M06 — Dual-Frequency Depth-Zone Analysis Engine": {
        "status": "Designed",
        "short": "Uses L-band and S-band differences to infer shallow/deeper response.",
        "objective": "Compare DFSAR L-band and S-band responses to classify shallow, deeper or mixed radar anomalies.",
        "why": "A single frequency cannot reliably indicate whether the response is surface roughness or subsurface material.",
        "science": "Longer wavelengths generally interact with deeper structures, while shorter wavelengths are more sensitive to near-surface roughness.",
        "engineering": "Creates a depth-zone layer used later in volume and accessibility estimates.",
        "inputs": ["L-band radar features", "S-band radar features"],
        "outputs": ["Depth-zone map", "L/S response ratio", "Buried candidate mask"],
        "equation": r"Response=f(\lambda,\epsilon,loss)",
        "workflow": ["Compare L-band", "Compare S-band", "Estimate response contrast", "Classify depth zone"],
        "papers": [["Nozette et al.", "Radar wavelength and polarimetric interpretation"]],
        "deliverables": ["Depth-zone map", "L/S comparison layer"],
        "isro": "This helps convert detection into characterization."
    },
    "M07 — Thermal Stability Modeling Engine": {
        "status": "Designed",
        "short": "Checks whether candidate ice can survive thermally.",
        "objective": "Estimate whether candidate ice deposits are thermally stable under lunar polar conditions.",
        "why": "Radar evidence must be physically possible. If a location is too warm, long-term ice survival is unlikely.",
        "science": "Water molecules in cold traps can remain for long times when sublimation rates are low and residence times are high.",
        "engineering": "Uses temperature constraints to remove thermally unrealistic candidates.",
        "inputs": ["Diviner temperature map", "PSR mask", "Depth assumption"],
        "outputs": ["Thermal stability map", "Residence time layer", "Stable depth estimate"],
        "equation": r"\tau(T)=\frac{\theta}{E(T)}",
        "workflow": ["Load temperature", "Estimate sublimation tendency", "Compute residence time", "Classify stability"],
        "papers": [["Schorghofer & Taylor", "Subsurface migration and cold-trap residence time"]],
        "deliverables": ["Thermal stability map", "Stable ice candidate mask"],
        "isro": "This makes detections scientifically defensible rather than purely radar-based."
    },
    "M08 — Ice Origin Classification Engine": {
        "status": "Conceptual",
        "short": "Interprets whether an ice candidate is physically plausible.",
        "objective": "Classify candidate deposits as possible migrated ice, impact-delivered ice, cometary ice or roughness false positives.",
        "why": "Different origins imply different concentration, depth and accessibility.",
        "science": "Cold-trap ice may form through ballistic migration, impact delivery or transient volatile deposition.",
        "engineering": "Adds interpretability to the detection results.",
        "inputs": ["Thermal stability", "CPR/DOP", "Concentration estimate", "Scattering class"],
        "outputs": ["Origin class map", "Physical plausibility score"],
        "equation": r"Origin=f(T,CPR,DOP,C)",
        "workflow": ["Combine evidence", "Apply origin rules", "Assign class", "Generate explanation layer"],
        "papers": [["Schorghofer & Taylor", "Migration pathways"], ["LCROSS", "Direct volatile detection"]],
        "deliverables": ["Origin map", "Interpretation report"],
        "isro": "This helps prioritize scientifically meaningful targets."
    },
    "M09 — Ice Concentration Estimation Engine": {
        "status": "Conceptual",
        "short": "Turns detection into approximate abundance.",
        "objective": "Estimate approximate water ice concentration for candidate regions.",
        "why": "Exploration planning requires quantity, not just location.",
        "science": "LCROSS provides a direct benchmark for lunar polar water abundance, while radar provides spatially distributed evidence.",
        "engineering": "Produces approximate wt% concentration maps with uncertainty.",
        "inputs": ["Ice probability", "Radar features", "LCROSS benchmark"],
        "outputs": ["Concentration map", "Abundance class", "Calibration report"],
        "equation": r"C_{ice}=f(P_{ice},CPR,confidence)",
        "workflow": ["Use probability", "Apply calibration", "Estimate concentration", "Assign uncertainty"],
        "papers": [["Colaprete et al.", "LCROSS 5.6 ± 2.9 wt% benchmark"]],
        "deliverables": ["Ice concentration map", "wt% estimate"],
        "isro": "This connects scientific detection to ISRU relevance."
    },
    "M10 — Bayesian Multi-Evidence Fusion Engine": {
        "status": "Designed",
        "short": "Combines all evidence into a final ice probability.",
        "objective": "Fuse radar, terrain, shadow and thermal evidence into one probability map.",
        "why": "No single observation can confirm ice. A probabilistic model is needed to combine uncertain evidence.",
        "science": "Bayesian inference updates a prior belief about ice using independent evidence layers.",
        "engineering": "Produces the final ice probability map and confidence layer.",
        "inputs": ["CPR", "DOP", "PSR mask", "Thermal stability", "Slope", "Scattering class"],
        "outputs": ["Ice probability map", "Confidence map", "Candidate ranking"],
        "equation": r"P(Ice|D)=\frac{P(D|Ice)P(Ice)}{P(D)}",
        "workflow": ["Normalize evidence", "Estimate likelihoods", "Compute posterior", "Generate probability map"],
        "papers": [["All four papers", "Fuses radar, thermal, validation and concentration evidence"]],
        "deliverables": ["Final ice probability map", "Confidence-weighted candidate zones"],
        "isro": "This is the central decision engine of the project."
    },
    "M11 — Volumetric Ice Estimation Engine": {
        "status": "Designed",
        "short": "Estimates accessible ice volume and mass.",
        "objective": "Estimate possible ice volume and mass within candidate regions.",
        "why": "Mission teams need to know how much ice may be available, not just where it is.",
        "science": "Volume depends on area, stable depth, estimated concentration and confidence.",
        "engineering": "Turns probability maps into resource estimates.",
        "inputs": ["Ice probability", "Area", "Depth estimate", "Concentration"],
        "outputs": ["Volume map", "Mass estimate", "Resource class"],
        "equation": r"V_{ice}=A\times d\times C\times P_{ice}",
        "workflow": ["Compute area", "Apply depth", "Apply concentration", "Weight by probability"],
        "papers": [["Schorghofer & Taylor", "Depth stability"], ["LCROSS", "Concentration benchmark"]],
        "deliverables": ["Volume estimate", "Mass estimate"],
        "isro": "This supports ISRU planning."
    },
    "M12 — Uncertainty Quantification Engine": {
        "status": "Designed",
        "short": "Reports confidence and uncertainty.",
        "objective": "Estimate uncertainty from calibration, temperature, depth and concentration assumptions.",
        "why": "Scientific maps without confidence values are incomplete.",
        "science": "Uncertainty propagation helps identify robust versus weak detections.",
        "engineering": "Creates confidence intervals and uncertainty maps.",
        "inputs": ["Sensor uncertainty", "Model parameters", "Calibration error"],
        "outputs": ["Uncertainty map", "Confidence interval", "Risk class"],
        "equation": r"\sigma_{total}=\sqrt{\sum_i\sigma_i^2}",
        "workflow": ["Define uncertainty sources", "Propagate errors", "Generate confidence layer"],
        "papers": [["All modules", "Supports scientific reliability"]],
        "deliverables": ["Confidence map", "Uncertainty report"],
        "isro": "This helps mission planners avoid overconfident decisions."
    },
    "M13 — Scientific Validation Engine": {
        "status": "Designed",
        "short": "Checks outputs against known observations.",
        "objective": "Validate model outputs against LCROSS, Mini-RF, Diviner and published literature.",
        "why": "Direct lunar ground truth is limited, so cross-mission validation is necessary.",
        "science": "Validation compares predicted ice probability and concentration with independent mission observations.",
        "engineering": "Generates validation scores and comparison plots.",
        "inputs": ["LCROSS benchmark", "Mini-RF products", "Diviner temperatures"],
        "outputs": ["Validation report", "Comparison metrics", "Agreement score"],
        "equation": r"Error=\frac{|Estimate-Reference|}{Uncertainty}",
        "workflow": ["Load references", "Compare outputs", "Compute agreement", "Report validation"],
        "papers": [["LCROSS", "Ground-truth concentration"], ["Nozette et al.", "Mini-RF radar comparison"]],
        "deliverables": ["Validation report", "Benchmark comparison"],
        "isro": "This shows the model is not just theoretical."
    },
    "M14 — Scientific Visualization Engine": {
        "status": "Designed",
        "short": "Creates maps and figures.",
        "objective": "Generate maps, plots, cross-sections and presentation-ready figures.",
        "why": "Good scientific visualization helps interpret complex multi-layer evidence.",
        "science": "Spatial relationships between ice, temperature and terrain must be visible.",
        "engineering": "Exports figures for reports, portal and PPT.",
        "inputs": ["All output rasters", "Tables", "Validation metrics"],
        "outputs": ["Maps", "Charts", "Cross-sections"],
        "equation": "N/A",
        "workflow": ["Load results", "Style layers", "Generate figures", "Export"],
        "papers": [["All papers", "Used for communication"]],
        "deliverables": ["Scientific figures", "PPT visuals"],
        "isro": "This makes results interpretable to reviewers."
    },
    "M15 — Interactive Dashboard Engine": {
        "status": "Active",
        "short": "Hosts the live project portal.",
        "objective": "Provide an interactive portal for architecture, methods, equations and implementation status.",
        "why": "A live portal makes the project more transparent and easier to review.",
        "science": "Allows evidence layers and methods to be explored interactively.",
        "engineering": "Built using Streamlit as a lightweight technical documentation interface.",
        "inputs": ["Documentation", "Figures", "Module status"],
        "outputs": ["Live portal", "Technical documentation website"],
        "equation": "N/A",
        "workflow": ["Collect content", "Render pages", "Display diagrams", "Publish portal"],
        "papers": [["All papers", "Documented in portal"]],
        "deliverables": ["Streamlit portal", "Demo link"],
        "isro": "This gives judges a way to inspect the complete methodology beyond the PPT."
    },
    "M16 — Scientific Report Generator": {
        "status": "Planned",
        "short": "Creates report outputs automatically.",
        "objective": "Generate structured PDF/HTML technical reports from module outputs.",
        "why": "A reproducible pipeline should also produce reproducible reporting.",
        "science": "Documents assumptions, maps, equations and validation in one report.",
        "engineering": "Automates final documentation.",
        "inputs": ["Maps", "Tables", "Figures", "References"],
        "outputs": ["PDF report", "HTML report"],
        "equation": "N/A",
        "workflow": ["Collect outputs", "Fill template", "Generate report"],
        "papers": [["All papers", "Referenced in final report"]],
        "deliverables": ["Scientific report"],
        "isro": "This supports formal review and submission."
    },
    "M17 — Export and Interoperability Engine": {
        "status": "Planned",
        "short": "Exports GIS-ready products.",
        "objective": "Export scientific outputs in formats usable by GIS and mission planning tools.",
        "why": "A result is more useful if it can be opened in QGIS, ArcGIS or other planning software.",
        "science": "Preserves geospatial structure of maps and masks.",
        "engineering": "Exports GeoTIFF, CSV, JSON, PDF and shapefiles.",
        "inputs": ["Maps", "Tables", "Masks"],
        "outputs": ["GeoTIFF", "CSV", "JSON", "PDF", "Shapefile"],
        "equation": "N/A",
        "workflow": ["Load products", "Convert formats", "Attach metadata", "Export"],
        "papers": [["Reproducibility", "Supports external reuse"]],
        "deliverables": ["GIS-ready outputs"],
        "isro": "This makes outputs usable beyond the demo."
    },
    "M18 — Mission Pipeline Orchestrator": {
        "status": "Framework Active",
        "short": "Runs the full pipeline.",
        "objective": "Control the end-to-end execution of all modules.",
        "why": "A complex architecture needs a controlled workflow so results remain reproducible.",
        "science": "Ensures every scientific step is executed in the correct order.",
        "engineering": "Manages configuration, logging, module execution and status tracking.",
        "inputs": ["Config file", "Module list", "Datasets"],
        "outputs": ["Complete processing run", "Pipeline log", "Status report"],
        "equation": "N/A",
        "workflow": ["Load config", "Initialize modules", "Run sequence", "Collect outputs"],
        "papers": [["System design", "Supports reproducibility"]],
        "deliverables": ["Pipeline run", "Execution logs"],
        "isro": "This turns the idea into an executable scientific workflow."
    }
}

st.markdown("""
<div class="selector-card">
<h3>Select a module</h3>
<p>
Use the dropdown below to inspect each subsystem. The first few modules are already connected to
the running codebase; the remaining modules are architected for dataset-driven implementation.
</p>
</div>
""", unsafe_allow_html=True)

selected = st.selectbox("Module", list(modules.keys()), index=0)

m = modules[selected]

st.markdown("---")

left, right = st.columns([2, 1])

with left:
    st.markdown(f"## {selected}")
    st.markdown(f"**Short description:** {m['short']}")

with right:
    st.metric("Status", m["status"])

st.markdown("---")

col1, col2 = st.columns(2)

with col1:
    st.markdown('<div class="module-card">', unsafe_allow_html=True)
    st.subheader("Objective")
    st.write(m["objective"])
    st.subheader("Why this module exists")
    st.write(m["why"])
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="module-card">', unsafe_allow_html=True)
    st.subheader("Scientific explanation")
    st.write(m["science"])
    st.subheader("Engineering role")
    st.write(m["engineering"])
    st.markdown('</div>', unsafe_allow_html=True)

st.subheader("Inputs and Outputs")

io1, io2 = st.columns(2)

with io1:
    st.table({"Inputs": m["inputs"]})

with io2:
    st.table({"Outputs": m["outputs"]})

st.subheader("Internal Workflow")

workflow_nodes = m["workflow"]
graph = "digraph { rankdir=LR; graph [bgcolor=\"transparent\"]; "
graph += "node [shape=box, style=\"rounded,filled\", fillcolor=\"#0f172a\", fontcolor=\"white\", color=\"#38bdf8\"]; "
graph += "edge [color=\"#93c5fd\", penwidth=2]; "
for i, step in enumerate(workflow_nodes):
    graph += f'N{i} [label="{step}"]; '
for i in range(len(workflow_nodes) - 1):
    graph += f"N{i} -> N{i+1}; "
graph += "}"

st.graphviz_chart(graph)

st.subheader("Mathematical model")

if m["equation"] == "N/A":
    st.info("This module is primarily architectural or operational and does not introduce a new mathematical model.")
else:
    st.latex(m["equation"])

st.subheader("Research mapping")

st.table({
    "Paper / Source": [p[0] for p in m["papers"]],
    "How it supports this module": [p[1] for p in m["papers"]]
})

st.subheader("Expected deliverables")
st.table({"Deliverable": m["deliverables"]})

st.subheader("Relevance to ISRO problem statement")
st.success(m["isro"])

st.subheader("Implementation-style pseudocode")

st.code(f"""
START {selected}

1. Load module-specific inputs
2. Check metadata, coordinate consistency and data quality
3. Apply the scientific method defined for this module
4. Generate intermediate products
5. Validate output against physical or engineering constraints
6. Save outputs for downstream modules
7. Pass products to the next stage of the pipeline

END {selected}
""")

st.markdown("---")
st.caption("LunarIce-DFSAR | Module architecture explorer")