from octoflow.data import load_dataset

dset = load_dataset("csv", "examples/data/2014_usa_states.csv")

print(dset.count_rows())
