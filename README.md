
# Plant Cell & Stomatal Observation

A quantitative botanical microscopy study analyzing stomatal distribution, stomatal density, and stomatal index across monocot and dicot leaf epidermis.

## Overview

Stomata are microscopic pores located on plant leaf surfaces, regulated by pairs of specialized guard cells to balance photosynthetic carbon dioxide uptake and transpirational water loss. This project investigates:

1. Stomatal frequency and distribution patterns across different plant species.
2. Comparison between lower (abaxial) and upper (adaxial) leaf surfaces.
3. Quantitative stomatal metrics calculated using standard botanical equations.

### Species Studied

* **Tradescantia zebrina** (Wandering Dude): Monocot herbaceous plant with distinct guard cells.
* **Rhoeo discolor** (Tradescantia spathacea / Moses-in-the-Cradle): Monocot with pigmented anthocyanin epidermal cells.
* **Spinacia oleracea** (Spinach): Dicot with amphistomatic leaves.
* **Ficus elastica** (Rubber Plant): Dicot xerophyte with hypostomatic adaptation.

## Microscopy Protocol & Data Collection

1. **Epidermal Peel Preparation**: Fresh leaves were bent and peeled using fine forceps to obtain a transparent epidermal layer.
2. **Mounting**: Strips were placed in a drop of water or dilute safranin stain on a clean glass slide and covered with a coverslip without air bubbles.
3. **Microscopic Examination**: Slides were viewed under a compound light microscope at 40x objective magnification (400x total magnification).
4. **Field of View (FOV) Calibration**: The field diameter was measured using an ocular micrometer calibrated against a stage micrometer ($FOV\text{ diameter} = 0.45\text{ mm}$, Area $\approx 0.159\text{ mm}^2$).
5. **Replication**: 5 distinct non-overlapping fields of view were recorded per leaf surface per species.

## Mathematical Formulas

### Stomatal Density

$$\text{Stomatal Density (stomata/mm}^2\text{)} = \frac{\text{Number of Stomata in Field of View}}{\text{Area of Field of View (mm}^2\text{)}}$$

### Stomatal Index (Salisbury's Formula)

$$\text{Stomatal Index (I)} = \frac{S}{S + E} \times 100$$

Where:
* $S$ = Number of stomata per unit area
* $E$ = Number of epidermal cells in the same area

## Project Structure

```text
plant-cell-stomatal-observation/
|
|-- data/
|   |-- stomatal_observations.csv
|   |-- stomatal_observations.xlsx
|-- figures/
|   |-- stomatal_density_comparison.png
|   |-- stomatal_index_distribution.png
|-- results/
|   |-- calculated_stomatal_indices.csv
|   |-- species_summary_statistics.csv
|-- analyze_stomata.py
|-- requirements.txt
|-- .gitignore
|-- README.md
```

## Running the Analysis

Ensure Python is installed along with the required libraries:

```bash
git clone https://github.com/your-username/plant-cell-stomatal-observation.git
cd plant-cell-stomatal-observation
pip install -r requirements.txt
python analyze_stomata.py
```

## Findings Summary

| Species | Surface Type | Mean Stomatal Density ($\text{mm}^{-2}$) | Mean Stomatal Index (%) | Leaf Anatomy Type |
| :--- | :--- | :--- | :--- | :--- |
| *Tradescantia zebrina* | Abaxial | $157.2 \pm 14.1$ | $18.5 \pm 1.1\%$ | Hypostomatic |
| *Tradescantia zebrina* | Adaxial | $22.6 \pm 7.2$ | $2.9 \pm 0.8\%$ | Very low density |
| *Rhoeo discolor* | Abaxial | $163.5 \pm 14.1$ | $17.8 \pm 0.7\%$ | Hypostomatic |
| *Rhoeo discolor* | Adaxial | $15.1 \pm 7.2$ | $1.8 \pm 0.9\%$ | Very low density |
| *Spinacia oleracea* | Abaxial | $137.1 \pm 12.1$ | $18.4 \pm 0.9\%$ | Amphistomatic |
| *Spinacia oleracea* | Adaxial | $69.2 \pm 9.9$ | $9.6 \pm 0.9\%$ | Moderate density |
| *Ficus elastica* | Abaxial | $234.0 \pm 16.3$ | $20.4 \pm 0.5\%$ | Strictly hypostomatic |
| *Ficus elastica* | Adaxial | $0.0 \pm 0.0$ | $0.0 \pm 0.0\%$ | Completely absent |

### Biological Inferences

* **Hypostomatic vs Amphistomatic Adaptations**: Broad leaves exposed to direct sunlight (such as *Ficus elastica*) restrict stomata strictly to the shaded lower epidermis, reducing excessive transpirational water loss. In contrast, fast-growing herbaceous crops like spinach (*Spinacia oleracea*) exhibit stomata on both surfaces to maximize gas exchange.
* **Consistency of Stomatal Index**: While absolute stomatal counts vary with cell expansion and light intensity, the stomatal index remains constant within a species, highlighting its utility in taxonomic classification and paleobotanical studies.


=======

