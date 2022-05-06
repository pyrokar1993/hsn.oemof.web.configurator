import logging

from pydantic import BaseModel


class EnsysConfigContainer(BaseModel):
    def __init__(self):
        super().__init__()

    def to_oemof(self):
        pass


def BuildKwargs(obj):
    kwargs = {}

    args = vars(obj)

    for key in args:
        if key is not None:
            value = args[key]

            kwargs[key] = value

    return kwargs
