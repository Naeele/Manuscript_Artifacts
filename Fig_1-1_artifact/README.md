# Reproducing Figure 1.1

This repository contains the data and scripts used to analyze research trends in the field of side-channel security and produce **Figure 1.1**.

## Repository Structure

* `analysis.ipynb` – Jupyter notebook containing the complete analysis workflow, including data processing, statistics, and figure generation.
* `dblp_dataset.jsonl` – Dataset used for the analysis, extracted from DBLP and stored in JSON Lines format.
* `side_channel_trend.pdf` – Final report containing the figure.
* `requirements.txt` – Python dependencies required to run the notebook.

## Requirements

Install the required packages with:

```bash
pip install -r requirements.txt
```

## Reproducing the Analysis

1. Clone the repository.
2. Install the dependencies listed in `requirements.txt` (in a virtual environment if needed).
3. Launch Jupyter Notebook:

```bash
jupyter notebook
```

4. Open `analysis.ipynb`.
5. Run all cells to reproduce the analysis and figures.
