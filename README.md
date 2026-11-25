<!-- brainlife-app:begin (generated from the App manifest; edit the manifest, not this block) -->

> **Concatenates a chosen parc-stats CSV from many subjects into one group table with pandas, adding subject, session and tag columns, for group analysis.**

For every selected parc-stats dataset, reads <csv_name>.csv, adds subjectID, sessionID, tags and datatype_tags columns from the dataset metadata when missing, and stacks all rows into parc_stats.csv. Use it to gather per-subject parcellation statistics across a project before group statistics.

| | |
|---|---|
| 📥 **Inputs** | `neuro/parc-stats` |
| 📤 **Outputs** | `neuro/parc-stats` |
| 🐳 **Container** | `brainlife/freesurfer-stats:1.2` |
| ⚙️ **Resources** | 1 CPUs · 14 GB memory · 0.5 h walltime |
| 🔗 **Run it** | [doi.org/10.25663/brainlife.app.821](https://doi.org/10.25663/brainlife.app.821) |

#### 📥 Inputs

| Input | Datatype | Required | Description |
|---|---|---|---|
| `parc-stats` | `neuro/parc-stats` | yes | Parcellation statistics datasets (multi), one per subject or session. Each must contain a CSV named <csv_name>.csv. |

#### 📤 Outputs

| Output | Datatype | Description |
|---|---|---|
| `parc-stats` | `neuro/parc-stats` | Group table parc_stats.csv combining the rows of all inputs with subject, session and tag columns. |

<details>
<summary><b>⚙️ Parameters</b> (1)</summary>

| Parameter | Type | Default | Description |
|---|---|---|---|
| `csv_name` | string |  | Base name (without .csv) of the CSV file to read from each parc-stats input. |

</details>

<!-- brainlife-app:end -->

# app-concatenate-tractmeasures