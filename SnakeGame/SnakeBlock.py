from dataclasses import dataclass
from typing import Tuple, List


@dataclass
class SnakeBlock:
    """Represents a single segment/block of the snake in the game.

    Each block has a color, movement direction, and position on the grid.
    This is used to construct and manage the snake's body segments.

    Attributes:
        color: RGB color tuple for the block (values 0-255)
        direction: Current movement direction ('up', 'down', 'left', 'right')
        grid_pos: Position on game grid as [x, y] coordinates
    """
    color: Tuple[int, int, int]
    direction: str
    grid_pos: List[int]