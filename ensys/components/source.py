from typing import Dict
from oemof import solph

from ensys import EnsysFlow, EnsysConfigContainer


class EnsysSource(EnsysConfigContainer):
    label: str = "Default Source",
    outputs: Dict[str, EnsysFlow]

    def to_oemof(self, energysystem: solph.EnergySystem) -> solph.Source:
        """
        Return an oemof-object build with the args of the object.
        :return: oemof-Source-object
        :rtype: solph.Source
        :param energysystem: the oemof-energysystem to build the kwargs of the object
        :type energysystem: solph.Energysystem
        """
        kwargs = self.build_kwargs(energysystem)

        return solph.Source(**kwargs)
