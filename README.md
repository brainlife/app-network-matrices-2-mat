<h1 align="center">Convert network neuro matrix to conmat</h1>

<p align="center">
  A <code>neuro/conmat</code> connectivity matrix from one measure of the Network Neuro <code>raw/networkmatrices</code> output and its parcellation.
</p>

<p align="center">
  <a href="https://github.com/brainlife/abcd-spec"><img src="https://img.shields.io/badge/ABCD_Spec-v1.1-green.svg" alt="ABCD Spec v1.1"></a>
  <a href="https://doi.org/10.25663/brainlife.app.335"><img src="https://img.shields.io/badge/Brainlife-brainlife.app.335-blue.svg" alt="Run on brainlife.io"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-lightgrey.svg" alt="MIT license"></a>
</p>

## 🧠 At a glance

<!-- brainlife-app:begin (generated from the App manifest; edit the manifest, not this block) -->

> **Converts one measure's matrix from the Network Neuro raw networkmatrices output, with its parcellation key, into a conmat datatype.**

Copies <measure>.csv from the networkmatrices output into cm/csv/correlation.csv and builds label.json from the parcellation key (plus 14 FreeSurfer subcortical labels) and index.json. Temporary bridge until Network Neuro outputs conmat directly; may be deprecated.

| | |
|---|---|
| 📥 **Inputs** | `raw` · `neuro/parcellation/volume` |
| 📤 **Outputs** | `neuro/conmat` |
| 🐳 **Container** | `faskowit/app-fmri-2-mat` |
| ⚙️ **Resources** | 1 CPUs · 0.5 h walltime |
| 🔗 **Run it** | [doi.org/10.25663/brainlife.app.335](https://doi.org/10.25663/brainlife.app.335) |

#### 📥 Inputs

| Input | Datatype | Required | Description |
|---|---|---|---|
| `raw` | `raw` (networkmatrices) | yes | The path to the top directory of the network matrices app |
| `parc` | `neuro/parcellation/volume` | yes | The path to the parcellation/volume datatype used to generate the network matrices |

#### 📤 Outputs

| Output | Datatype | Description |
|---|---|---|
| `cm` | `neuro/conmat` | The conmat data output |

<details>
<summary><b>⚙️ Parameters</b> (1)</summary>

| Parameter | Type | Default | Description |
|---|---|---|---|
| `measure` | enum |  | Which network matrix to convert (the CSV <measure>.csv in the networkmatrices output), for example density or count. Options: `density`, `count`, `fa_mean`, `fa_std`, `length`, `curv`, `tors`, `fa_tp`, `denlen`, `centers`, `md_mean`, `rd_mean`, `ad_mean`, `ndi_mean`, `odi_mean`, `isovf_mean`, `ad_mean_density`, `fa_mean_density`, `md_mean_density`, `rd_mean_density`, `ndi_mean_density`, `odi_mean_density`, `isovf_mean_density`, `sphmean_mean`, `sphmean_mean_density`. |

</details>

<!-- brainlife-app:end -->

## 🔬 How it works

The Network Neuro App writes its network matrices as a `raw` dataset (tag `networkmatrices`), one csv per measure. Most network Apps on brainlife.io take the `neuro/conmat` datatype instead. This App bridges the two:

1. It copies `<measure>.csv` from the networkmatrices output to `cm/csv/correlation.csv`.
2. It builds `label.json` from the parcellation `key.txt`, adding the 14 FreeSurfer subcortical labels (left and right thalamus, caudate, putamen, pallidum, hippocampus, amygdala and accumbens).
3. It writes `index.json` describing the matrix.

The code is adapted from [`generate_cm_datatype.py`](https://github.com/faskowit/app-fmri-2-mat/blob/0.1.1/generate_cm_datatype.py) in Josh Faskowitz's app-fmri-2-mat. It is a temporary App until Network Neuro outputs a conmat datatype directly, and may be deprecated in the future.

Available measures include `density`, `count`, `length`, `curv`, `tors`, `centers`, `denlen`, the mean and standard deviation of FA (`fa_mean`, `fa_std`, `fa_tp`), the means of MD, RD, AD, NDI, ODI, ISOVF and sphmean (`md_mean`, …), and their versions scaled by the inverse volume of the nodes (`fa_mean_density`, …).

## 🚀 Running the App

### ☁️ On brainlife.io

Open the App at [doi.org/10.25663/brainlife.app.335](https://doi.org/10.25663/brainlife.app.335), choose the `raw` networkmatrices output of Network Neuro and the `neuro/parcellation/volume` dataset used to generate it, pick the `measure` to convert and press **Execute**. The matrix is archived to your project as a `neuro/conmat` dataset tagged `networkmatrices` and `preprocessed`.

### 💻 Locally

You need [Singularity/Apptainer](https://apptainer.org/). `main` runs `make-datatype.py` inside the `faskowit/app-fmri-2-mat` container; without Singularity, Python 3 is enough.

1. Clone this repository and check out the App's branch: `git checkout v1.0.0`.
2. Create `config.json` with the path to the networkmatrices output, the parcellation key and the measure:

   ```json
   {
       "matrices": "/input/raw",
       "parc": "/input/parc/parc.nii.gz",
       "key": "/input/parc/key.txt",
       "label": "/input/parc/label.json",
       "measure": "density"
   }
   ```

   The App reads `<matrices>/output/<measure>.csv`.

3. Run the App:

   ```bash
   ./main
   ```

## 📦 Outputs

```text
cm/
├── csv/
│   └── correlation.csv   the connectivity matrix of the chosen measure
├── label.json            node labels from key.txt plus the FreeSurfer subcortical labels
└── index.json            description of the matrix
```

## 📚 Citing

> [!TIP]
> If you use this App in your work, please cite the App, the software it builds on and brainlife.io (below). GitHub's **Cite this repository** button gives the App citation in APA and BibTeX.

- Convert network neuro matrix to conmat. brainlife.io App. [doi:10.25663/brainlife.app.335](https://doi.org/10.25663/brainlife.app.335)
- Avesani P, McPherson B, Hayashi S, et al. The open diffusion data derivatives, brain data upcycling via integrated publishing of derivatives and reproducible open cloud services. Sci Data 6, 69 (2019). [doi:10.1038/s41597-019-0073-y](https://doi.org/10.1038/s41597-019-0073-y)
- Fischl. FreeSurfer. *NeuroImage* 62:774-781 (2012). [doi:10.1016/j.neuroimage.2012.01.021](https://doi.org/10.1016/j.neuroimage.2012.01.021)
- Hayashi S, Caron BA, Heinsfeld AS, et al. brainlife.io: a decentralized and open-source cloud platform to support neuroscience research. *Nature Methods* 21:809–813 (2024). [doi:10.1038/s41592-024-02237-2](https://doi.org/10.1038/s41592-024-02237-2)

## 👥 Authors

- Brad Caron

**Contributors:** Soichi Hayashi

## 💰 Funding

[![Wellcome-226486/Z/22/Z](https://img.shields.io/badge/Wellcome-226486%2FZ%2F22%2FZ-purple.svg)](https://wellcome.org/)
[![NIH-NINDS-U24NS140384](https://img.shields.io/badge/NIH_NINDS-U24NS140384-green.svg)](https://reporter.nih.gov/project-details/11261037)
[![NIH-NINDS-UM1NS132207](https://img.shields.io/badge/NIH_NINDS-UM1NS132207-green.svg)](https://reporter.nih.gov/project-details/11411328)
[![NIH-NIBIB-R01EB029272](https://img.shields.io/badge/NIH_NIBIB-R01EB029272-green.svg)](https://reporter.nih.gov/project-details/10262925)
[![NIH-NIBIB-R01EB030896](https://img.shields.io/badge/NIH_NIBIB-R01EB030896-green.svg)](https://reporter.nih.gov/project-details/10428625)
[![NIH-NIMH-R01MH126699](https://img.shields.io/badge/NIH_NIMH-R01MH126699-green.svg)](https://reporter.nih.gov/project-details/10460628)
[![NIH-NIDCD-R01DC020088](https://img.shields.io/badge/NIH_NIDCD-R01DC020088-green.svg)](https://reporter.nih.gov/project-details/11140284)
[![NSF-BCS-1734853](https://img.shields.io/badge/NSF_BCS-1734853-blue.svg)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=1734853)
[![NSF-BCS-2203524](https://img.shields.io/badge/NSF_BCS-2203524-blue.svg)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=2203524)
[![NSF-IIS-1636893](https://img.shields.io/badge/NSF_IIS-1636893-blue.svg)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=1636893)
[![NSF-OAC-2148729](https://img.shields.io/badge/NSF_OAC-2148729-blue.svg)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=2148729)
[![NSF-IIS-1912270](https://img.shields.io/badge/NSF_IIS-1912270-blue.svg)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=1912270)
[![NSF-IIS-2148700](https://img.shields.io/badge/NSF_IIS-2148700-blue.svg)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=2148700)
[![NSF-OAC-1916518](https://img.shields.io/badge/NSF_OAC-1916518-blue.svg)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=1916518)

<sub>brainlife.io is publicly funded, and acknowledging that support helps keep it running. This App was developed with support from Wellcome, the U.S. National Institutes of Health (including the BRAIN Initiative BRAIN CONNECTS program: The Axonal Projectome EXchange, U24NS140384, and the Center for Mesoscale Connectomics, UM1NS132207) and the U.S. National Science Foundation.</sub>

## ⚖️ License

[MIT](LICENSE).
