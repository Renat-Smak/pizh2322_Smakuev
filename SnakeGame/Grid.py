from Cell import Cell
from pygame import Surface


class Grid:
    """Represents a 2D grid of cells for game board implementation.

    The grid handles creation and management of cells, and provides convenient
    access to individual cells through indexing.

    Attributes:
        width (int): Number of cells horizontally.
        height (int): Number of cells vertically.
        cell_size (int): Size of each cell in pixels.
        screen (Surface): Pygame surface for rendering.
        cells (list[list[Cell]]): 2D list containing all cells.
    """

    def __init__(
        self,
        screen: Surface,
        width: int = 16,
        height: int = 16,
        cell_size: int = 40
    ) -> None:
        """Initialize the grid with specified dimensions.

        Args:
            screen: Pygame surface for rendering.
            width: Number of horizontal cells. Defaults to 16.
            height: Number of vertical cells. Defaults to 16.
            cell_size: Size of each cell in pixels. Defaults to 40.
        """
        self.width = width
        self.height = height
        self.cell_size = cell_size
        self.screen = screen
        self.cells = self._create_cells()

    def _create_cells(self) -> list[list[Cell]]:
        """Create and return a 2D grid of Cell objects.

        Returns:
            A 2D list of Cell instances with proper positioning.
        """
        return [
            [
                Cell(
                    pos_x=x * self.cell_size,
                    pos_y=y * self.cell_size,
                    screen=self.screen,
                    cell_size=self.cell_size
                )
                for x in range(self.width)
            ]
            for y in range(self.height)
        ]

    def __getitem__(self, index: int) -> list[Cell]:
        """Enable grid[y][x] indexing to access cells.

        Args:
            index: Row index of the grid.

        Returns:
            List of cells in the specified row.

        Raises:
            IndexError: If index is out of grid bounds.
        """
        return self.cells[index]