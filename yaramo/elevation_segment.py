from yaramo.base_element import BaseElement
from yaramo.elevation_point import ElevationPoint

class ElevationSegment(BaseElement):
    """Elevation segments run between two elevation points and have a length."""
    def __init__(self, elevation_point_a: ElevationPoint, elevation_point_b: ElevationPoint, length: float, **kwargs):
        """
        Parameters
        ----------
        uuid: str
            UUID of the elevation segment
        elevation_point_a: ElevationPoint
            First elevation point of the segment
        elevation_point_b: ElevationPoint
            Second elevation point of the segment
        length: float
            Length of the elevation segment
        """
        super().__init__(**kwargs)
        self.elevation_point_a = elevation_point_a
        self.elevation_point_b = elevation_point_b
        self.length = length
