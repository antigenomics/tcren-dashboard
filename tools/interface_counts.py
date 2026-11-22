"""Export per-model peptide contact counts from prepared molecular scenes."""

import argparse
import gzip
import json
from pathlib import Path


def interface_counts(directory: Path) -> dict[str, dict[str, int]]:
    directory = directory.resolve()
    entries = json.loads((directory / "index.json").read_text())
    counts = {}
    for entry in entries:
        source = (directory / entry["file"]).resolve()
        if not source.is_relative_to(directory):
            raise ValueError("Scene path leaves the prepared directory.")
        with gzip.open(source, "rt", encoding="utf-8") as handle:
            scene = json.load(handle)
        identity = entry["id"]
        if scene["id"] != identity or identity in counts:
            raise ValueError("Prepared scene and index identities must match uniquely.")
        role_pairs = scene["summary"]["contacts_by_role_pair"]
        counts[identity] = {
            role: role_pairs.get(role, 0) for role in ("alpha:peptide", "beta:peptide")
        }
    return counts


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("prepared_maps", type=Path)
    args = parser.parse_args()
    print(json.dumps(interface_counts(args.prepared_maps), separators=(",", ":")))
