from octoflow.data import load_dataset

dset = load_dataset("json", "examples/data/google_markers.json")

print(dset.count_rows())

print(dset[:])
