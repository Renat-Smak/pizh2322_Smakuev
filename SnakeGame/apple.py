from random import choice, randint
from Grid import Grid


class Apple:
    """Represents an apple in the game with random color and position.

    The apple is placed on a grid and can be removed. Each apple has a randomly
    generated color with constraints to ensure pleasant colors.
    """

    def __init__(self, grid: Grid) -> None:
        """Initialize the apple and place it on the grid.

        Args:
            grid: The game grid where the apple will be placed.
        """
        self.game_grid = grid
        self.color = (0, 0, 0)
        self.cell = None
        self.place()

    def place(self) -> None:
        """Place the apple on a random empty cell in the grid.

        Generates a random color for the apple and selects an empty cell
        from the grid to place the apple. If no empty cells are available,
        prints a warning message.
        """
        red = randint(50, 255)
        blue = randint(50, 255)
        max_green = min(red, blue)
        green = randint(0, max_green)

        self.color = (red, green, blue)

        empty_cells = [
            cell
            for row in self.game_grid.cells
            for cell in row
            if cell.content is None
        ]

        if empty_cells:
            chosen_cell = choice(empty_cells)
            chosen_cell.content = self
            self.cell = chosen_cell
        else:
            print("No empty cells available for apple placement!")

    def remove(self) -> None:
        """Remove the apple from its current cell."""
        if self.cell is not None:
            self.cell.content = None
            self.cell = None