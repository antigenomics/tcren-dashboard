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

Use **Side (x/z)** or **Top (x/y)** to switch the projection. Zoom with the
wheel, the zoom buttons, or the slider. Depth fading and point outlines
are optional. Chain roles use distinct shapes, and point color represents
the supplied model label.

The structure selector shows the outcome label first, so it stays visible
when a long model name is clipped. Hover over a model in the list to see
its full name.

Use the label menu for binary outcomes or the minimum and maximum controls
for continuous outcomes when the export includes label metadata.

Select a residue to inspect its heavy atoms and recorded interchain contacts.
Select a contact to highlight its atom endpoints. Use **Pin reference** and
the `[` and `]` keys to compare matching structures within the same reference
group. Contact heatmaps have residue headers on both axes. Surface plots
have x/y axes in ångströms.

Highlight multiple models in one reference group and choose **Add
highlighted** to retain them while changing label or confidence filters.
Use **Add random matches** to sample filtered models without replacement,
and **Clear selection** to start over. Color the molecular overlay by
model, label, ipTM or mean pLDDT. Chain roles use point shapes.

In the table view, open **Compare multiple models**. The binary map is the
cell-wise label 1 mean minus the label 0 mean where both have observations.
For a numeric label, ipTM or pLDDT, the weighted map is the mean of each
available cell value multiplied by its model's population z-score across
the selected scored models. Hover a cell to see its support. Contact grids
compare sequence positions within the same facet and reference group.

Run `node tests/viewer.mjs` with Node 22 or newer to check viewer
cancellation, label filters, atom contact lookup, and heatmap cell states. The files under `assets/` are the distributable template.
Version tags identify compatible template snapshots for TCRen.

The molecular viewer initially loads the selected group. Existing exports
without a group index and bookmarks containing only a model ID still resolve
through the full index. After selection, viewer links carry both the model ID
and its group. The partition download list loads when opened.

Both viewers and the generated ranking page share `assets/dashboard.css`.
The molecular and table rules are scoped to their page types. Installations
supply their own datasets and deployment configuration separately.
