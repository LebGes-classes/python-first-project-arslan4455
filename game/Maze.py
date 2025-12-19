import random


class Maze:
    """Класс для генерации и управления лабиринтом."""
    
    WALL = "⬛️"
    PATH = "⬜️"
    EXIT = "🏁"

    def __init__(self, width: int, height: int):
        """
        Инициализирует лабиринт заданных размеров.
        
        Args:
            width (int): Ширина лабиринта 
            height (int): Высота лабиринта
        """
        self.width = width
        self.height = height
        self.grid = self._generate()

    def _generate(self) -> list[list[str]]:
        """
        Генерирует случайный лабиринт.
        
        Returns:
            list[list[str]]: Двумерный список, представляющий лабиринт
        """
        grid = [[self.WALL for _ in range(self.width)]
                for _ in range(self.height)]

        def carve(x: int, y: int):
            """
            Рекурсивно создает проходы в лабиринте.
            
            Args:
                x (int): Текущая x-координата
                y (int): Текущая y-координата
            """
            directions = [(2, 0), (-2, 0), (0, 2), (0, -2)]
            random.shuffle(directions)
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 1 <= nx < self.width - 1 and 1 <= ny < self.height - 1:
                    if grid[ny][nx] == self.WALL:
                        grid[ny][nx] = self.PATH
                        grid[y + dy // 2][x + dx // 2] = self.PATH
                        carve(nx, ny)

        grid[1][1] = self.PATH
        carve(1, 1)

        grid[self.height - 2][self.width - 2] = self.EXIT
        return grid

    def is_walkable(self, x: int, y: int) -> bool:
        """
        Проверяет, можно ли пройти по указанным координатам.
        
        Args:
            x (int): X-координата для проверки
            y (int): Y-координата для проверки
            
        Returns:
            bool: True если клетка проходима, False если это стена
        """
        return self.grid[y][x] != self.WALL

    def is_exit(self, x: int, y: int) -> bool:
        """
        Проверяет, является ли указанная клетка выходом из лабиринта.
        
        Args:
            x (int): X-координата для проверки
            y (int): Y-координата для проверки
            
        Returns:
            bool: True если клетка является выходом, иначе False
        """
        return self.grid[y][x] == self.EXIT

