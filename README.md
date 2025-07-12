#  Link Theory: A Geometric Model of Neural Collapse

This repository contains the full research paper, code notebooks, visual simulations, and supplementary materials for **Link Theory** — a structural model of brain failure grounded in network science, motif geometry, and trauma research.

## What is Link Theory?

**Link Theory** proposes that the smallest unit of neural stability is not a region, but a triangle — a 3-node motif of redundant, rigid connection. When these motifs collapse under chronic stress (e.g. trauma), the failure spreads non-linearly, leading to cognitive and emotional breakdown. The project simulates this using:

- Real/simulated EEG data
- Graph theory
- Geodesic 3D models
- Triangle-based motif detection and failure propagation

##  What's in this Repository?

link-theory/
├── LinkTheory_Paper.pdf # Full academic paper
├── notebooks/
│ └── link_theory_simulation.ipynb # Colab-ready code + visualizations
├── data/
│ └── sample_eeg.csv # EEG input for stress mapping
├── visuals/
│ ├── geodesic_dome.png
│ └── collapse_sim.gif # (optional) animated collapse
├── README.md # This file
├── LICENSE # Your chosen license (MIT recommended for code)
└── CITATION.cff # Citation metadata for academic use

markdown
Copy
Edit

## How to Run It

1. **Open** the `notebooks/link_theory_simulation.ipynb` file in [Google Colab](https://colab.research.google.com)
2. **Upload EEG data** or use the built-in synthetic model
3. **Run each cell** step by step to:
   - Build network graphs
   - Inject stress signals
   - Watch triangle motif failure cascade
   - Visualize dome collapse in 3D

##  Key Concepts

- **Triangle Motifs (3-cliques):** The smallest resilient structural unit
- **Cascade Failure:** Collapse spreads topologically, not spatially
- **Geodesic Dome:** A symbolic model of cortical redundancy
- **EEG Integration:** Maps delta wave activity to node-level stress
- **Failure Conditions:** Based on local collapse, neighbor loss, and motif breakdown

##  Paper and Theory

See `LinkTheory_Paper.pdf` for:
- Theoretical framework
- Mathematical modeling
- Simulation design
- Interpretation of results
- Academic references (Sporns, Giusti, Lanius, etc.)


🌐 License
Code: MIT License

Visuals & Paper: CC BY-NC-ND 4.0 (non-commercial academic use only)

Acknowledgments
This project is part of Lack of Grey Matter — an independent initiative for original research at the intersection of psychology, mathematics, trauma theory, and design.

For questions, collaborations, or press:
📧 lamhakausarahmed@gmail.com
🌐 OSF Project: [(https://osf.io/4qcr9/?view_only=f56920e385d645658c33ed17f98e49b3)]

