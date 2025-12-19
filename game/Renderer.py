import os

from Player import (
    Player
)
from Maze import (
    Maze
)


class Renderer:
    """Класс для отрисовки игрового состояния."""
    
    def draw(self, maze: Maze, player: Player) -> None:
        """
        Отрисовывает текущее состояние игры.
        
        Args:
            maze (Maze): Объект лабиринта для отрисовки
            player (Player): Объект игрока для отрисовки его позиции
        """
        
        os.system("cls")
        for y, row in enumerate(maze.grid):
            for x, cell in enumerate(row):
                if player.x == x and player.y == y:
                    print(Player.SYMBOL, end="")
                else:
                    print(cell, end="")
            print()

