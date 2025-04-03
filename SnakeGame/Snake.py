from tkinter import OFF
from Grid import Grid
from SnakeBlock import SnakeBlock
from typing import Tuple, List
from apple import Apple


class Snake:
    """Represents a snake in the game with movement and growth capabilities.

    The snake consists of multiple blocks (head + body segments) that move together.
    It can grow when eating apples and detects collisions with itself.

    Attributes:
        game_grid: Reference to the game grid
        head_color: RGB color of the snake's head
        body_color: RGB color of the snake's body
        game_apple: Reference to the apple object
        body: List of snake blocks making up the snake
    """

    def __init__(
        self,
        game_grid: Grid,
        game_apple: Apple,
        head_color: Tuple[int, int, int] = (70, 130, 180),
        body_color: Tuple[int, int, int] = (0, 206, 209),
    ) -> None:
        """Initialize the snake with starting position and colors.

        Args:
            game_grid: The game grid where snake exists
            game_apple: The apple object for collision detection
            head_color: RGB color for snake head (default: steel blue)
            body_color: RGB color for snake body (default: dark turquoise)
        """
        self.game_grid = game_grid
        self.head_color = head_color
        self.body_color = body_color
        self.game_apple = game_apple
        self.body = [SnakeBlock(self.head_color, "right", (0, 0))]
        self.game_grid[0][0].content = self.body[0]

    def move(self) -> None:
        """Move the snake forward based on current directions of each block.
        
        Handles:
        - Movement with grid wrapping
        - Apple eating and growth
        - Self-collision detection
        """
        head = self.body[0]
        new_head_pos = self._calculate_new_position(head.grid_pos, head.direction, 1)
        
        # Check for self-collision before moving
        collision_index = self._check_body_collision(new_head_pos)
        if collision_index is not None and collision_index > 0:
            self._bite_tail(collision_index)
            return

        # Clear current positions before moving
        for block in self.body:
            self.game_grid[block.grid_pos[0]][block.grid_pos[1]].content = None

        # Move each block
        prev_direction = ""
        for block in self.body:
            current_pos = block.grid_pos
            
            if block.color == self.head_color:
                prev_direction = block.direction
                block.grid_pos = new_head_pos
            else:
                block.grid_pos = self._calculate_new_position(current_pos, block.direction, 1)

            # Handle apple eating or normal movement
            target_cell = self.game_grid[block.grid_pos[0]][block.grid_pos[1]]
            if isinstance(target_cell.content, Apple):
                self._handle_apple_eaten(block)
            else:
                target_cell.content = block

            # Update directions
            block.direction, prev_direction = prev_direction, block.direction

    def _calculate_new_position(self, current_pos: Tuple[int, int], direction: str, offset: int) -> Tuple[int, int]:
        """Calculate new position after movement with grid wrapping.

        Args:
            current_pos: (x, y) current position
            direction: Movement direction

        Returns:
            New (x, y) position after movement
        """
        y, x = current_pos #ИСПРАВИЛ БЫЛО X, Y
        if direction == "right":
            return (y, x + offset) if x < self.game_grid.width - 1 else (y, 0)
        elif direction == "left":
            return (y, x - offset) if x > 0 else (y, self.game_grid.width - 1)
        elif direction == "up":
            return (y - offset, x) if y > 0 else (self.game_grid.height - 1, x)
        elif direction == "down":
            return (y + offset, x) if y < self.game_grid.height - 1 else (0, x)
        return current_pos

    def _check_body_collision(self, new_head_pos: Tuple[int, int]) -> int | None:
        """Check if new head position collides with body.

        Args:
            new_head_pos: Position to check

        Returns:
            Index of colliding body block or None
        """
        for i, block in enumerate(self.body):
            if block.grid_pos == new_head_pos:
                return i
        return None

    def _bite_tail(self, collision_index: int) -> None:
        """Remove tail starting from collision point.

        Args:
            collision_index: Index where to start removing
        """
        # Clear blocks from grid
        for block in self.body[collision_index:]:
            self.game_grid[block.grid_pos[0]][block.grid_pos[1]].content = None
        
        # Shorten snake body
        self.body = self.body[:collision_index]

    def _handle_apple_eaten(self, block: SnakeBlock) -> None:
        """Handle logic when snake eats an apple."""
        self.game_apple.remove()
        self.game_apple.place()
        self.grow()
        self.game_grid[block.grid_pos[0]][block.grid_pos[1]].content = block

    def grow(self) -> None:
        """Add new segment to snake's body when eating an apple."""
        last_block = self.body[-1]
        last_pos = last_block.grid_pos
        last_dir = last_block.direction

        offset = 2 if len(self.body) == 1 else 1

        new_pos = self._calculate_new_position(
            last_pos,
            self._reverse_direction(last_dir),
            offset)
        
        new_block = SnakeBlock(self.body_color, last_dir, new_pos)
        self.body.append(new_block)

    def _reverse_direction(self, direction: str) -> str:
        """Get opposite direction for positioning new segments."""
        return {
            "right": "left",
            "left": "right",
            "up": "down",
            "down": "up"
        }[direction]

    def change_direction(self, new_direction: str) -> None:
        """Change the snake's head direction if valid.
        
        Args:
            new_direction: One of ['up', 'down', 'left', 'right']
        """
        current_direction = self.body[0].direction
        if (current_direction, new_direction) not in [
            ("up", "down"), ("down", "up"),
            ("left", "right"), ("right", "left")
        ]:
            self.body[0].direction = new_direction