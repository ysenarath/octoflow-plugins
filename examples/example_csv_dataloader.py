from octoflow.data import load_dataset

dset = load_dataset("examples/2014_usa_states.csv")

print(dset.count_rows())
