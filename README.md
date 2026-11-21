# TCRen dashboard template

Static browser assets for the molecular and table views produced by TCRen.
The template uses browser-native JavaScript and has no runtime package
dependencies. TCRen generates the ranking page and all model data, and
copies pinned viewer assets into the bundle.

Build a dashboard from one scoring cohort with TCRen 4.7 or later.

```sh
tcren dashboard import models.tsv --task tcr --label-kind binary -o dashboard
python -m http.server --bind 127.0.0.1 --directory dashboard
```

The TSV columns are `structure_id`, `structure_path`, `iptm`, `plddt`,
and `label`. Use `--task epitope` for peptide ranking and
`--label-kind continuous` for numeric assay measurements.
See the [TCRen browser guide](https://docs.isalgo.dev/tcren/complementarity.html).

Run `node tests/viewer.mjs` with Node 22 or newer to verify cancellation in
both viewers. The files under `assets/` are the distributable template.
Version tags identify compatible template snapshots for TCRen.
