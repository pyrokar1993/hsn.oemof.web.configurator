from typing import Dict, Union

from pydantic import validator, Field
from InRetEnsys import InRetEnsysConfigContainer, InRetEnsysEnergysystem
from InRetEnsys.types import Solver


##  Container which contains the params for an InRetEnsys-Model
#   
#   @param energysystem The Energysystem which should be optimized.
#   @param solver The Solvername for the optimization.
#   @param solver_verbose Set true if the solver should print his output and steps.
class InRetEnsysModel(InRetEnsysConfigContainer):
    energysystem: InRetEnsysEnergysystem = Field(
        ...,
        title='Energysystem',
        description='Energysystem to solve',
        lvl_visible=21,
        lvl_edit=42
    )

    solver: Solver = Field(
        Solver.gurobi,
        title='Solver',
        description='Solver',
        lvl_visible=21,
        lvl_edit=42
    )

    solver_verbose: bool = Field(
        True,
        title='Solver verbose',
        description='Print output from the Solver',
        lvl_visible=21,
        lvl_edit=42
    )

    solver_kwargs: Dict[str, Union[bool, str, int, float]] = Field(
        None,
        title='Solver Extra Arguments',
        description='Extra arguments for the Solver (MIP_GAP etc.)',
        lvl_visible=21,
        lvl_edit=42
    )

    @classmethod
    @validator('energysystem')
    def es_is_not_none(cls, v):
        if v is None:
            raise ValueError("Energysystem can not be 'None'.")

        return v