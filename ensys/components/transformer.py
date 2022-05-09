from ensys import EnsysFlow, EnsysConfigContainer


class EnsysTransformer(EnsysConfigContainer):
    label: str = "Default Transformer",
    inputs: dict = None,
    outputs: dict = None,
    conversion_factors: dict = None

    def __init__(self,
                 label: str = "Default Transformer",
                 inputs: dict[EnsysFlow] = None,
                 outputs: dict[EnsysFlow] = None,
                 conversion_factors=None
                 ):
        """Init the EnsysTransformer object."""
        super().__init__()
        self.label = label
        self.inputs = inputs
        self.outputs = outputs
        self.conversion_factors = conversion_factors
