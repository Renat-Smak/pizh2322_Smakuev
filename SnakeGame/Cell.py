from pygame import Surface, draw
from Position import Position


class Cell:
    """Represents a single cell in a grid-based game or simulation.

    Each cell can contain an object and handles its own rendering on a pygame surface.

    Attributes:
        size (int): Size of the cell in pixels (always square).
        position (Position): Position of the cell on the screen (x, y coordinates).
        color (tuple[int, int, int]): Default background color in RGB format.
        screen (Surface): Pygame surface where the cell is drawn.
        _content (object | None): Internal storage for cell's content.
    """

    def __init__(
        self,
        pos_x: int,
        pos_y: int,
        screen: Surface,
        cell_size: int = 20,
        content: object = None,
        default_color: tuple[int, int, int] = (173, 255, 47),
    ) -> None:
        """Initialize a Cell instance.

        Args:
            pos_x: X-coordinate of the cell's top-left corner.
            pos_y: Y-coordinate of the cell's top-left corner.
            screen: Pygame surface for drawing.
            cell_size: Width and height of the cell in pixels. Defaults to 20.
            content: Initial content of the cell. Defaults to None.
            default_color: Background color when cell is empty (RGB). Defaults to light green.
        """
        self.size = cell_size
        self._content = content
        self.position = Position(pos_x, pos_y)
        self.color = default_color
        self.screen = screen
        self.draw()

    @property
    def content(self) -> object | None:
        """Get the current content of the cell."""
        return self._content

    @content.setter
    def content(self, value: object | None) -> None:
        """Set the cell's content and trigger redraw.

        Args:
            value: New content for the cell.
        """
        self._content = value
        self.draw()

    def draw(self) -> None:
        """Draw the cell on the screen.

        Uses the content's color if present, otherwise uses the cell's default color.
        """
        color = self.content.color if self.content is not None else self.color
        draw.rect(
            self.screen,
            color,
            (self.position.x, self.position.y, self.size, self.size),
        )