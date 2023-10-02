import random
from enum import Enum
from typing import Optional, Tuple

from yaramo.base_element import BaseElement
from yaramo.edge import Edge


class DatapointDirection(Enum):
    """The SignalDirection determines whether or not a Signal points in or against the direction of it's Edge."""

    IN = 1
    GEGEN = 2

    def __str__(self):
        return self.name.lower()

class Datapoint(BaseElement):
    """Datapoints are used to define the location of Balises on the track."""
    def __init__(self, edge: Edge, offset: float, etcs_level: str, length: float|int, direction: str, datapoint_types: int, etcs_address: dict, **kwargs):
        """
        Parameters
        ----------
        edge: Edge
            The edge the datapoint is on
        offset: float
            position of the datapoint from the start of the edge
        etcs_level: str
            ETCS level of the datapoint
        length: float
            length of the datapoint (distance between balises in L2)
        direction: str
            direction of the datapoint
        datapoint_types: int
            type of the datapoint (types of packets)
        etcs_address: dict
            ETCS header values
            "Kennung": None,
            "NID_C": None,
            "NID_BG": None,
        """
        super().__init__(**kwargs)
        self.edge = edge
        self.offset = offset
        self.etcs_level = etcs_level
        self.length = length
        self.datapoint_types = datapoint_types

        # TODO direction can be one of "gegen", "in" or "keine". What does "keine" mean?
        self.direction = DatapointDirection.GEGEN if direction.lower() == "gegen" else DatapointDirection.IN

        # ETCS Address is this dictionary right now, can also be changed to class properties
        # or its own class
        """ self.etcs_address = {
            "Kennung": None,
            "NID_C": None,
            "NID_BG": None,
        } """
        self.etcs_address = etcs_address

    def to_serializable(self) -> Tuple[dict, dict]:
        return self.__dict__, {}

class Balise(BaseElement):
    def __init__(self, index: int, datapoint: Datapoint, **kwargs):
        super().__init__(**kwargs)
        self.index = index
        self.datapoint = datapoint
        # ATTENTION The offset works only for L2 PlanPro files
        # it's assumed there is no more and no less than 2 balises per datapoint, seperated by the datapoint length
        self.offset = datapoint.offset if index == 1 else datapoint.offset + datapoint.length

    def to_serializable(self) -> Tuple[dict, dict]:
        return self.__dict__, {}

class BaliseGroup(BaseElement):
    """A BaliseGroup is a group of Balises that are on the same Datapoint"""
    def __init__(self, balises: list[Balise], **kwargs):
        super().__init__(**kwargs)
        self.balises = balises
        self.datapoint = balises[0].datapoint

    def add_balise(self, balise: Balise):
        self.balises.append(balise)

    def to_serializable(self) -> Tuple[dict, dict]:
        return self.__dict__, {}
