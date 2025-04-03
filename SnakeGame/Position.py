from dataclasses import dataclass


@dataclass
class Position:
    """Represents a 2D position with x and y coordinates.

    This class provides a simple way to store and manipulate 2D positions
    using dataclass functionality for automatic method generation.

    Attributes:
        x: The horizontal coordinate.
        y: The vertical coordinate.
    """
    x: int
    y: int