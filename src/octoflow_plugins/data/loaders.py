from octoflow.data.loader import dataloader

try:
    from pandas import read_csv as pd_read_csv
except ImportError:
    pd_read_csv = None

__all__ = [
    "read_csv",
]


@dataloader("csv", extensions=[".csv"], wraps=pd_read_csv, path_arg="filepath_or_buffer")
def read_csv(*args, **kwargs):
    return read_csv(*args, **kwargs)
