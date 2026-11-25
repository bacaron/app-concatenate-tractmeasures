<h1 align="center">Compile parc-stats csvs across project into one dataframe</h1>

<p align="center">
  Concatenates a chosen parc-stats CSV from many subjects into one group table with pandas, adding subject, session and tag columns, for group analysis.
</p>

<p align="center">
  <a href="https://github.com/brainlife/abcd-spec"><img src="https://img.shields.io/badge/ABCD_Spec-v1.1-green.svg" alt="ABCD Spec v1.1"></a>
  <a href="https://doi.org/10.25663/brainlife.app.821"><img src="https://img.shields.io/badge/Brainlife-brainlife.app.821-blue.svg" alt="Run on brainlife.io"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-see_LICENSE-lightgrey.svg" alt="License"></a>
</p>

## At a glance

<!-- brainlife-app:begin (generated from the App manifest; edit the manifest, not this block) -->

> **Concatenates a chosen parc-stats CSV from many subjects into one group table with pandas, adding subject, session and tag columns, for group analysis.**

For every selected parc-stats dataset, reads <csv_name>.csv, adds subjectID, sessionID, tags and datatype_tags columns from the dataset metadata when missing, and stacks all rows into parc_stats.csv. Use it to gather per-subject parcellation statistics across a project before group statistics.

| | |
|---|---|
| **Inputs** | `neuro/parc-stats` |
| **Outputs** | `neuro/parc-stats` |
| **Container** | `brainlife/freesurfer-stats:1.2` |
| **Resources** | 1 CPUs · 14 GB memory · 0.5 h walltime |
| **Run it** | [doi.org/10.25663/brainlife.app.821](https://doi.org/10.25663/brainlife.app.821) |

#### Inputs

| Input | Datatype | Required | Description |
|---|---|---|---|
| `parc-stats` | `neuro/parc-stats` | yes | Parcellation statistics datasets (multi), one per subject or session. Each must contain a CSV named <csv_name>.csv. |

#### Outputs

| Output | Datatype | Description |
|---|---|---|
| `parc-stats` | `neuro/parc-stats` | Group table parc_stats.csv combining the rows of all inputs with subject, session and tag columns. |

<details>
<summary><b>Parameters</b> (1)</summary>

| Parameter | Type | Default | Description |
|---|---|---|---|
| `csv_name` | string |  | Base name (without .csv) of the CSV file to read from each parc-stats input. |

</details>

<!-- brainlife-app:end -->

## Running the App

### On brainlife.io

Open the App at [doi.org/10.25663/brainlife.app.821](https://doi.org/10.25663/brainlife.app.821), choose `neuro/parc-stats` from your project, set the parameters and press **Execute**. The results are saved to your project as `neuro/parc-stats`.

### Locally

You need [Singularity/Apptainer](https://apptainer.org/) (the App runs in `brainlife/freesurfer-stats:1.2`), [`jq`](https://jqlang.github.io/jq/).

1. Clone this repository.
2. Create `config.json` with the paths to your inputs and the parameters:

   ```json
   {
       "parc-stats": "/path/to/parc-stats/parc-stats",
       "csv_name": ""
   }
   ```

3. Run `./main`.

## Citing

If you use this App, please cite it, the software it builds on and brainlife.io:

- Compile parc-stats csvs across project into one dataframe. brainlife.io App. [doi:10.25663/brainlife.app.821](https://doi.org/10.25663/brainlife.app.821)
- Fischl. FreeSurfer. *NeuroImage* 62:774-781 (2012). [doi:10.1016/j.neuroimage.2012.01.021](https://doi.org/10.1016/j.neuroimage.2012.01.021)
- Hayashi S, Caron BA, Heinsfeld AS, et al. brainlife.io: a decentralized and open-source cloud platform to support neuroscience research. *Nature Methods* 21:809–813 (2024). [doi:10.1038/s41592-024-02237-2](https://doi.org/10.1038/s41592-024-02237-2)
- Avesani P, McPherson B, Hayashi S, et al. The open diffusion data derivatives, brain data upcycling via integrated publishing of derivatives and reproducible open cloud services. *Scientific Data* 6:69 (2019). [doi:10.1038/s41597-019-0073-y](https://doi.org/10.1038/s41597-019-0073-y)

## Authors

Maintained by [@bacaron](https://github.com/bacaron).

## License

See [LICENSE](LICENSE).
