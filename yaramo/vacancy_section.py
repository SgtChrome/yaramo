from typing import Tuple
from yaramo.base_element import BaseElement

class VacancyComponent(BaseElement):
    """Vacany components sit at the ends of vacancy sections. They can have one vacancy section on each side.

    Usually only used if the vacancy section has axle counters"""
    def __init__(self, edge_uuid: str, offset: float, vacancy_section_a_uuid: str = None, vacancy_section_b_uuid: str = None, **kwargs) -> None:
        """
        Parameters
        ----------
            vacancy_section_a_uuid: str
                UUID of the vacancy section on the left side of the vacancy component
            vacancy_section_b_uuid: str
                UUID of the vacancy section on the right side of the vacancy component
            edge_uuid: str
                UUID of the edge the vacancy component is on
            offset: float
                Offset to the start of the edge as a float denoting the position of the vacancy component
        """
        super().__init__(**kwargs)
        self.vacancy_section_a_uuid = vacancy_section_a_uuid
        self.vacancy_section_b_uuid = vacancy_section_b_uuid
        self.edge_uuid = edge_uuid
        self.offset = offset

    def get_offset(self) -> str:
        return str(self.offset)

    def to_serializable(self) -> Tuple[dict, dict]:
        return self.__dict__, {}


class SubSection():
    """Track sections can be dived into subsections.
    These are usually used to define the length and location of a vacancy section."""

    def __init__(self, offset_a: float, offset_b: float, edge_uuid: str):
        """
        Parameters
        ----------
            offset_a: float
                Offset to the start of the edge as a float denoting the start of the subsection
            offset_b: float
                Offset to the start of the edge as a float denoting the end of the subsection
            edge_uuid: str
                UUID of the edge the subsection is on"""
        # both offsets are in reference to the start of the edge!
        self._offset_a = offset_a
        self._offset_b = offset_b
        self.edge_uuid = edge_uuid

    def get_offset_a(self) -> str:
        """Returns:
            Offset to the start of the edge as a string"""
        return str(self._offset_a)

    def get_offset_b(self) -> str:
        return str(self._offset_b)

class TrackSection(BaseElement):
    """"PlanPro includes "Gleisabschnitte" which are the smallest section of track for operational and technical purposes.

    They are used to define vacancy sections and are usually limited by vacancy components (axle counters)"""
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        self._subsections: list[SubSection] = []

    def add_subsection(self, offset_a: float, offset_b: float, edge_uuid: str):
        self._subsections.append(SubSection(offset_a, offset_b, edge_uuid))

    def get_subsections(self) -> list[SubSection]:
        return self._subsections

    def to_serializable(self) -> Tuple[dict, dict]:
        return self.__dict__, {}

class VacancySection(BaseElement):
    """VacancySection right now only nests TrackSections inside it and has no other purpose.
    This is just to imitate the PlanPro structure and can be changed if it turns out it's not needed.

    The track sections are referred to by the vacancy sections as track_section class property"""
    def __init__(self, track_section: TrackSection, **kwargs) -> None:
        super().__init__(**kwargs)
        self.track_section = track_section

    def to_serializable(self) -> Tuple[dict, dict]:
        return self.__dict__, {}
