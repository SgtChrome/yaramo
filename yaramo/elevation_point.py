from yaramo.base_element import BaseElement
from yaramo.edge import Edge

class ElevationPoint(BaseElement):
    """This class represents a point in the elevation profile.

    Angle or height can be None
    """
    def __init__(self, edge_uuid: str, offset: float, angle: float = None, height: float = None, **kwargs):
        """
        Parameters
        ----------
            edge_uuid: str
                UUID of the edge the elevation point is on
            offset: float
                Offset to the start of the edge as a float denoting the position of the elevation point
            angle: float
                Angle of the elevation point
            height: float
                Height of the elevation point
        """
        super().__init__(**kwargs)
        self.edge_uuid = edge_uuid
        self.offset = str(float(offset))
        self._angle = str(float(angle)) if angle is not None else None
        self._height = str(float(height)) if height is not None else None

    def get_angle(self):
        return self._angle if self._angle is not None else ''

    def get_height(self):
        return self._height if self._height is not None else ''
