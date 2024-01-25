from typing import Literal, Union, overload

from octoflow.data.dataset import DEFAULT_FORMAT

@overload
def load_dataset(
    __loader: Union[Literal["csv"], Literal["CSV"]],
    __path: str,
    __format: str = DEFAULT_FORMAT,
    /,
    *args,
    **kwargs,
): ...
@overload
def load_dataset(
    __loader: Union[Literal["json"], Literal["JSON"]],
    __path: str,
    __format: str = DEFAULT_FORMAT,
    /,
): ...
