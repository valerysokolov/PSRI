# Political System Resilience Index (PSRI)
**Version:** 1.1.0  
**Methodology:** Expert-Driven Algebraic Stability Modeling  
**Author:** [Your Name]  
**Year:** 2026

## 1. Overview
The **PSRI** is a modular analytical tool designed to quantify the resilience of political systems. The core philosophy of this project is the **Separation of Concerns**:
- **The Engine (`psri_core.py`):** Immutable mathematical logic based on Saaty's Analytic Hierarchy Process (AHP).
- **The Expert Data (`config.json`):** A flexible configuration file where the researcher (expert) inputs their subjective weights and current field metrics.

## 2. The Expert's Role
The system's accuracy depends on the expert's input. The expert must provide:
1. **Pairwise Comparisons:** Defining which pillar of stability (Institutions, Economy, or Society) is dominant in a specific national context.
2. **Current Metrics:** Real-time values (0-100) reflecting the current state of each pillar.

By isolating these inputs in `config.json`, the model allows for **transparent peer review** and **scenario auditing**.

## 3. Mathematical Core
The resilience score ($S$) is the dot product of the normalized priority vector ($\mathbf{w}$) and the metrics vector ($\mathbf{x}$):
$$S = \mathbf{w}^T \mathbf{x}$$

The priority vector is the principal eigenvector of the expert's judgment matrix $\mathbf{A}$, where $a_{ij}$ represents the importance of factor $i$ over factor $j$.

## 4. Installation & Usage
1. **Requirements:** `numpy`
2. **Configuration:** Edit `config.json` with your expert judgments.
3. **Execution:** ```bash
   python run_analysis.py
